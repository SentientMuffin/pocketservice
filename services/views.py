from django.shortcuts import render
from rest_framework.response import Response

from . import models
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from django.shortcuts import redirect

# Create your views here.

# ClientRequest Block
@api_view(['GET'])
def fetch_client_requests(request, client_id):
    crqs = ClientRequest.objects.filter(client__user_id=client_id)
    serializer = ClientRequestSerializer(crqs, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_client_request(request, request_id):
    crqs = ClientRequest.objects.get(pk=request_id)
    srl = ClientRequestSerializer(crqs, data=request.data)
    if srl.is_valid():
        srl.save()
        return Response(srl.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(srl.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_client_request(request):
    serializer = ClientRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['DELETE'])
def delete_client_request(request, request_id):
    try:
        crq = ClientRequest.get(pk=request_id)
        crq.destroy()
        return Response("ClientRequest successfuly deleted", status=status.HTTP_202_ACCEPTED)
    except ClientRequest.DoesNotExist:
        return Response("ClientRequest does not exist!", status=status.HTTP_204_NO_CONTENT)


# Other model blocks. Not sure if needed at this point
