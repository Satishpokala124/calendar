from django.contrib import auth
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from .models import User
from django.db.models import Q


# Create your views here.

def test(request):
    return render(request, 'account/index.html')


@api_view(['POST'])
def user_login(request):
    try:
        username_or_email = request.data['username']
        password = request.data['password']
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    users = User.objects.filter(
        username=username_or_email
    ).union(
        User.objects.filter(
            email=username_or_email
        )
    )
    username = users[0].username
    user = auth.authenticate(request, username=username, password=password)
    if not user:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_403_FORBIDDEN)
    auth.login(request, user)
    return Response({'message': 'Logged In'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    username = request.data['username']
    firstname = request.data['firstname']
    lastname = request.data['lastname']
    email = request.data['email']
    password = request.data['password']
    cnf_password = request.data['cnf_password']

    try:
        User.username_validator(username)
    except ValidationError:
        return Response({'error': 'Invalid username'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        validate_password(password)
    except ValidationError:
        return Response({'error': 'Weak password'}, status=status.HTTP_400_BAD_REQUEST)

    is_existing_username = len(User.objects.filter(username=username)) > 0
    if is_existing_username:
        return Response({'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST)

    is_existing_email = len(User.objects.filter(email=email)) > 0
    if is_existing_username:
        return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

    if password != cnf_password:
        return Response({'error': 'Password and Confirm Password mismatched'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(
        username=username,
        first_name=firstname,
        last_name=lastname,
        email=email,
        password=password
    )
    user.save()
    auth.login(request, user)
    return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def user_logout(request):
    auth.logout(request)
    return Response({'message': 'Logged Out'}, status=status.HTTP_200_OK)
