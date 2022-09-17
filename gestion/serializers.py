from rest_framework import serializers
from .models import Usuario

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    def save(self):
        # Modificamos el metodo save para que ahora si se pueda generar el hash de la password
        nuevoUsuario = Usuario(**self.validated_data)
        nuevoUsuario.set_password(self.validated_data.get('password'))
        nuevoUsuario.save()
        return nuevoUsuario
    
    class Meta:
        model = Usuario
        exclude = ['groups', 'user_permissions']
        