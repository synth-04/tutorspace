from django.db import models
from django.contrib.auth.models import User, Group
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import Group
from .fields import RichTextField

class Course(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='courses',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    allowed_groups = models.ManyToManyField(
        Group, blank=True, related_name='courses'
    )

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(
        Course,
        related_name='modules',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0)

    unlocked_groups  = models.ManyToManyField(
        Group, blank=True, related_name='unlocked_modules'
    )

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title

class Content(models.Model):
    module = models.ForeignKey(
        Module,
        related_name='contents',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = RichTextField()
    order = models.IntegerField(default=0)
    content_type = models.CharField(max_length=50, choices=[
        ('text', 'Testo'),
        ('image', 'Immagine'),
        ('audio', 'Audio'),
        ('document', 'Documento'),
        ('link', 'Link'),
        ('assignment', 'Compito'),
        ('discussion', 'Discussione'),
        ('poll', 'Sondaggio'),
        ('video', 'Video'),
        ('quiz', 'Quiz')
    ])
    
    unlocked_groups  = models.ManyToManyField(
        Group, blank=True, related_name='unlocked_contents'
    )

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title

class Resource(models.Model):
    content = models.ForeignKey(
        Content,
        related_name='resources',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200, default="file")
    file = models.FileField(upload_to='resources/')
    description = models.TextField(default="Nessuna descrizione")

    def __str__(self):
        return self.description[:50]
    
    
class GroupProfile(models.Model):
    group = models.OneToOneField(Group,
                                 related_name='profile',
                                 on_delete=models.CASCADE)
    selectable = models.BooleanField(default=False,
                                     help_text="Se True, il gruppo appare nel dropdown di registrazione")

    def __str__(self):
        return f"Profile di {self.group.name}"