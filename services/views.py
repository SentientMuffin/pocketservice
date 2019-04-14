from django.shortcuts import render
from rest_framework.response import Response

from . import models
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from django.shortcuts import redirect

# Create your views here.
@api_view(['GET'])
def fetch_client_requests(request, client_id):
    crqs = ClientRequest.objects.filter(client__user_id=client_id)
    serializer = ClientRequestSerializer(crqs, many=True)
    return Response(serializer.data)