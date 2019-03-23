from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from rest_framework.decorators import api_view
from .serializers import UserSerializer


# Create your views here.
# allowed request methods for this "view"
@api_view(['GET', 'POST', 'PUT'])
def fetch_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)