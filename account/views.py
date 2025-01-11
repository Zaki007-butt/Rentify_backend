#Django Imports
from django.shortcuts import render
from django.contrib.auth import authenticate

#Rest Framework Imports
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

#Rest Framework Simple JWT Imports
from rest_framework_simplejwt.authentication import JWTAuthentication

#Local Imports
from account.serializers import (
  UserRegistrationSerializer,
  UserLoginSerializer,
  UserProfileSerializer,
  UserChangePasswordSerializer,
  UserPasswordResetSerializer,
  UserProfileUpdateSerializer
)
from account.renderers import UserRenderer
from account.utils import get_tokens_for_user

class UserRegistrationView(APIView):
  renderer_classes = (UserRenderer,)
  def post(self, request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      tokens = get_tokens_for_user(user)
      return Response({'success': True, 'tokens': tokens}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
  renderer_classes = (UserRenderer,)
  def post(self, request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
      email = serializer.data.get('email')
      password = serializer.data.get('password')
      user = authenticate(request, email=email, password=password)
      if user is not None:
        tokens = get_tokens_for_user(user)
        return Response({'success': True, 'data': {
          "email": user.email
        }, 'tokens': tokens}, status=status.HTTP_200_OK)
      else:
        response = {
          'errors': {
            'non_field_errors': 'Username or password is invalid'
          }
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
  renderer_classes = (UserRenderer,)
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]

  def get(self, request):
    user = request.user
    serializer = UserProfileSerializer(user)
    return Response({
      'success': True, 
      'data': {
        **serializer.data,
        'avatar': request.build_absolute_uri(user.avatar.url) if user.avatar else None
      }
    }, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
  renderer_classes = (UserRenderer,)
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]

  def post(self, request):
    serializer = UserChangePasswordSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      self.update_user_password(request.user, serializer.data.get('new_password'))
      return Response({'success': True}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def update_user_password(self, user, password):
    user.set_password(password)
    user.save()

class UserUpdateView(APIView):
  renderer_classes = (UserRenderer,)
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]

  def put(self, request):
    user = request.user
    serializer = UserProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateProfileView(APIView):
    renderer_classes = (UserRenderer,)
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        serializer = UserProfileUpdateSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            # Handle avatar file upload
            if 'avatar' in request.FILES:
                # Delete old avatar if exists
                if user.avatar:
                    user.avatar.delete(save=False)
                user.avatar = request.FILES['avatar']
            
            serializer.save()
            return Response({
                'success': True,
                'data': {
                    **serializer.data,
                    'avatar': request.build_absolute_uri(user.avatar.url) if user.avatar else None
                }
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

