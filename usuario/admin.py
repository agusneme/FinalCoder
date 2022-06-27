from django.contrib import admin
from .models import *
from usuario.models import Avatar

# Register your models here.

admin.site.register(Avatar)
