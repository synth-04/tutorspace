# Generated by Django 5.2 on 2025-04-21 21:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('overview', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='courses.course')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('content_type', models.CharField(choices=[('text', 'Testo'), ('image', 'Immagine'), ('audio', 'Audio'), ('document', 'Documento'), ('link', 'Link'), ('assignment', 'Compito'), ('discussion', 'Discussione'), ('poll', 'Sondaggio'), ('video', 'Video'), ('quiz', 'Quiz')], max_length=50)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='courses.module')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='resources/')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='courses.content')),
            ],
        ),
    ]
