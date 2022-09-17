from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from .serializers import RegistroUsuarioSerializer
from rest_framework.response import Response
from rest_framework import status
from .enviar_correos import enviar_correo_validacion


class RegistroUsuarioView(CreateAPIView):
    serializer_class = RegistroUsuarioSerializer

    def post(self, request: Request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()

        print(enviar_correo_validacion(data.data.get('email')))

        return Response(data={
            'message': 'Usuario registrado correctamente',
            'content': ''
        }, status=status.HTTP_201_CREATED)