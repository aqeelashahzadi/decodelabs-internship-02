from django.contrib import admin
from .models import Student # Apne model ko import karo
from .models import teachers
admin.site.register(Student) # Isay register karo
admin.site.register(teachers)