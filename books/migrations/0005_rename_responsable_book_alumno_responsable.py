# Generated by Django 4.0.6 on 2022-07-29 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_email_responsable_book_telefono_responsable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='responsable',
            new_name='alumno_responsable',
        ),
    ]
