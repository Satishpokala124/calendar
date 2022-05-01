from django.contrib import auth
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


def register(request):
    pass


@api_view(['GET'])
def user_logout(request):
    auth.logout(request)
    return Response({'message': 'Logged Out'}, status=status.HTTP_200_OK)
