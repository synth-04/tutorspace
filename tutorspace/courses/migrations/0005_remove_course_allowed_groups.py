# Generated by Django 5.2 on 2025-05-12 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_allowed_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='allowed_groups',
        ),
    ]
