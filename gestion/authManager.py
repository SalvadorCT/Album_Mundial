from django.contrib.auth.models import BaseUserManager
# BaseUserManager > es una clase que nos permite crear usuarios y administrarlos
# BaseUserManager > modificar el comportamiento entero de la creacion de un usuario
# UserManager > me permite modificar el comportamiento de las clases nuevas

class AuthManager(BaseUserManager):
    def create_superuser(self, email, password, nombre, apellido, rol):
        """Creacion de un superusuario por consola (python manage.py createsuperuser)"""
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        # Valido el correo y ademas lo nomrmalizo
        correo_normalizado = self.normalize_email(email)
        nuevoUsuario = self.model(email=correo_normalizado, nombre=nombre, apellido=apellido, rol=rol)
        
        nuevoUsuario.is_staff = True
        nuevoUsuario.is_superuser = True

        # generara un hash de la contraseña para evitar guardar de manera pura
        nuevoUsuario.set_password(password)
        nuevoUsuario.save()

        return nuevoUsuario
