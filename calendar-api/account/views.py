from django.contrib import auth
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from django.db.models import Q


# Create your views here.

@api_view(['POST'])
def user_login(request):
    username_or_email = request.data['username']
    password = request.data['password']
    username = User.objects.filter(Q(username__eq=username_or_email) | Q(email__eq=username_or_email)).username
    user = auth.authenticate(username, password)

    if user:
        auth.login(request, user)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_403_FORBIDDEN)


def register():
    pass


def user_logout():
    pass