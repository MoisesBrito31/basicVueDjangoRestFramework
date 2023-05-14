from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Usuario
from .serializer import UsuarioSerializer

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getUserData(request):
    try:
        user = request.user
        print(f'tipo: {type(user)}, dados:{user}')
        print(user.username)
        serial = UsuarioSerializer(user)
        data = serial.data
    except Exception as EX:
        data = {
            'valor': '',
            'erro': str(EX)
        }
    return Response(data)
