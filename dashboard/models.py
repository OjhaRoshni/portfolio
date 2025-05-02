from django.db import models

# Create your models here.
class  LanguageImg(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',default="")
    
 #in admin panel it will show the name of the image
    def __str__(self):
        return self.name

class  CurrentLangImg(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',default="")

    def __str__(self):
        return self.name

class EducationsQuali(models.Model):
    Year = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Projects(models.Model):
    image = models.ImageField(upload_to='images/',default="")
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    language_used = models.CharField(max_length=100)
    project_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.project_name

