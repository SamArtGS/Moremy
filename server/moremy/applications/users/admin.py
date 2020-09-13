from django.contrib import admin

from .models import StudentProfile, User

# Register your models here.
admin.site.register(User)
admin.site.register(StudentProfile)
