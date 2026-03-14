from django.contrib import admin
from .models import *

admin.site.register(custom_user)
admin.site.register(Department)
admin.site.register(Student)

# Register your models here.
