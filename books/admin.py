from django.contrib import admin
from .models import Book
from django.contrib.auth.models import User, Group


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "nivel",
        "status",
        "alumno_responsable",
        "telefono_responsable",
        "email_responsable",
    )
    search_fields = ("title", "alumno_responsable")

    site_header = "Hausand"
    site_title = "Hausand"
    index_title = "Hausand"


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
