from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'nivel', 'status', 'alumno_responsable', 'telefono_responsable', 'email_responsable')

# Register your models here.
admin.site.register(Book, BookAdmin)