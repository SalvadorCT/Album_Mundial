from django.db import models
from .authManager import AuthManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# AbstractBaseUser > usar la plantilla del usuario que django nos provee
# PermissionsMixin > nos permite usar los permisos de django
class Usuario(AbstractBaseUser, PermissionsMixin):
    
    id = models.AutoField(primary_key=True, unique=True)
    email = models.EmailField(max_length=50,null=False, unique=True)
    password = models.TextField(null=False)
    nombre = models.CharField(max_length=50,null=False)
    apellido = models.CharField(max_length=50,null=False)
    # EN EL PRIMER VALOR sera el que se almacena en la bd | en el que se usa para formularios
    rol = models.CharField(max_length=50,choices = (['ADMINISTRADOR','ADMINISTRADOR'],['USUARIO','USUARIO']))
    validado = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)


    # fECHA DE CREACION del usuario
    creteAt = models.DateTimeField(auto_now_add=True,db_column='creado')
    # fECHA DE ACTUALIZACION del usuario
    updateAt = models.DateTimeField(auto_now=True,db_column='actualizado')

    # ======================================
    #Todo lo siguiente ES NETAMENTE SI AUN QUEREMOS USAR EL ADMIN DE DJANGO
    
    # agregar las siguientes columnas para que el panel administrativo siga funcionando a pesar de haber modificado
    # el auth_user
    # is_staff > sirve para saber si el usuario es administrador o no
    is_staff = models.BooleanField(default=False)
    # is_active > sirve para saber si el usuario esta activo o no
    # is_active > puede realizar operaciones dentro del panel administrativo, pero si el usuario no esta activo podra logearse pero no realizar ninguna accion dentro del panel administrativo
    is_active = models.BooleanField(default=True)

    objects = AuthManager()

    #Se usara para el panel administrativo al momento de hacer el login
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['nombre','apellido','rol']

    class Meta:
        db_table = 'usuarios'


class Categoria(models.Model):
    nombre = models.CharField(max_length=45, null=False)


    class Meta:
        db_table = 'categorias'

class Figura(models.Model):
    codigo = models.CharField(max_length=10, null=False, 
    unique=True)
    nombre = models.CharField(max_length=45, null=False)

    # RELACIONES
    categoria = models.ForeignKey(to=Categoria, 
    on_delete=models.PROTECT, related_name='figuras')

    class  Meta:
        db_table = 'figuras'

class Registro(models.Model):
    numeroVeces = models.IntegerField(db_column='num_veces', null=False)
    tipo = models.CharField(max_length=40, choices=(['NORMAL','NORMAL'],['ESPECIAL','ESPECIAL'],
    ['ESCUDO','ESCUDO']))
    #RELACIONES
    figura = models.ForeignKey(to=Figura, on_delete=models.PROTECT, related_name='figura_registros')
    usuario = models.ForeignKey(to=Usuario, on_delete=models.PROTECT, related_name='usuario_registros')

    class Meta:
        db_table = 'registros'