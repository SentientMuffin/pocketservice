from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from django.shortcuts import redirect


# Create your views here.
# allowed request methods for this "view"
@api_view(['GET'])
def fetch_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    if request.method == 'GET':
        return redirect('/fetch_users/')
    breakpoint()
    # adding username to request.data
    request.data['username'] = request.data['email']
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid() and (request.data['user_type'] in ['client', 'worker']):
        user = serializer.save()

        # Create corresponding sub model records
        if request.data['user_type'] == 'client':
            cli = Client.create(user)
            cli.save()
        else:
            sw = ServiceWorker.create(user)
            sw.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_user(request, user_id):
    if request.method != 'PUT':
        return redirect('/fetch_users/')

    user = User.objects.get(pk=user_id)
    srl = UserSerializer(user, data=request.data)
    if srl.is_valid():
        srl.save()
        return Response(srl.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(srl.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_user(request, user_id):
    if request.method != 'DELETE':
        return redirect('/fetch_users/')

    try:
        user = User.objects.get(pk=user_id)
        user.destroy() # this should only update the deleted_at field instead of actually hard delete
    except User.DoesNotExist:
        return Response("User does not exist!", status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def fetch_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        serializer = UserSerializer([user], many=True)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response("User does not exist!", status=status.HTTP_204_NO_CONTENT)


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
