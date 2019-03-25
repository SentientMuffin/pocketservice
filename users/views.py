from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer
from django.shortcuts import redirect

# Create your views here.
# allowed request methods for this "view"
@api_view(['GET', 'POST', 'PUT'])
def fetch_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


def create_user(request):
    if request.method == 'GET':
        return redirect('/fetch_users/')

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def validate_user_data(data):
    # check that data contains the correct information, nothing more, could be less
    # White list the data listed below
    proper_user_data = {
        "first_name": data.get("first_name"),
        "last_name": data.get("last_name"),
        "email": data.get("email"),
        "password": data.get("password"),
        "phone_number": data.get("phone_number"),
    }
    return proper_user_data
