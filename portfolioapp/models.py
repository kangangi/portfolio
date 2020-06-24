from django.db import models
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    '''
    Class that defines the profile page
    '''
    fullname = models.CharField(max_length = 50)
    picture =CloudinaryField('image')
    bio = models.TextField()
    github = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.fullname

class Language(models.Model):
    '''
    class that defines the language objects
    '''
    name = models.CharField(max_length= 50)
    image = CloudinaryField('image', null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    '''
    class that defines project objects
    '''
    title = models.CharField(max_length = 100)
    description = models.TextField()
    link = models.URLField()
    languages = models.ManyToManyField(Language)
    image = CloudinaryField('image',null=True)

    def __str__(self):
        return self.title





