# Generated by Django 5.1.1 on 2024-10-09 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nexapp', '0005_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='college',
            old_name='courses',
            new_name='course_name',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='course_name',
        ),
    ]
