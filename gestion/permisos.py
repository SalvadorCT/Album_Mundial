from email import message
from rest_framework.permissions import BasePermission
from rest_framework.request import Request

class PermisoPersonalizado(BasePermission):
    # message > mensaje que se mostrara cuando no se cumpla la condicion
    message = 'No tienes permisos'
    def has_permission(self, request: Request, view):
        # middleware > es un intermediario entre la peticion del usuario
        # (endpoint) y el controlador final (view)
        # Aqui va la logicad de permisos

        # request > es la peticion del usuario
        # request.user > nos devuelve la instancia del usuario encontrado en la base de datos
        # En el caso no se proporcione las credenciales de autenticacion
        # request.user > AnonymousUser (es un usuario anonimo)
        print(request.user)

        # request.auth > sino se le dan las credenciales de auth nos devuelve vacio,
        # si se le dan las credenciales nos devuelve el token que nos envia el user
        print(request.auth)
        # view > es la vista que se desea acceder
        # print(view)
        # print(request.user.rol)

        if request.auth is None:
            return False
        print(request.user.rol)

        if request.user.rol == 'ADMINISTRADOR':
            return False
        else:
            return True

class EsAdministrador(BasePermission):
    message = 'El usuario no tiene permisos necesarios'

    def has_permission(self, request: Request, view):
        print(request.data.get('rol'))
        # si el rol es 'USUARIO' no pida la token y si el rol es 'ADMINISTRADOR' pida la token
        if request.data.get('rol') == 'USUARIO':
            return True
        
        #validamos que en el auth tengamos una token
        if request.auth is None:
            self.message = 'Se necesita una token para esta peticion'
            return False

        #validamos que el usuario sea administrador para poder crear
        if request.user.rol == 'ADMINISTRADOR':
            return True
        else:
            return False