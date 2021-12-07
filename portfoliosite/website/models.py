from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length= 255)
    description = models.CharField(max_length= 10000)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    githublink = models.CharField(max_length= 255, null=True, blank=True)
    websitelink = models.CharField(max_length= 255, null=True, blank=True)

    def __str__(self):
        return self.name + ', ID' + str(self.id)

class Print(models.Model):
    name = models.CharField(max_length= 255)
    description = models.CharField(max_length= 10000, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    detailimage1 = models.ImageField(null=True, blank=True)
    detailimage2 = models.ImageField(null=True, blank=True)
    detailimage3 = models.ImageField(null=True, blank=True)
    detailimage4 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name + ', ID' + str(self.id)

class WorkExperience(models.Model):
    name = models.CharField(max_length= 255)
    duration = models.CharField(max_length= 255)
    description = models.CharField(max_length= 10000)

    def __str__(self):
        return self.name + ', ID' + str(self.id)

class Education(models.Model):
    name = models.CharField(max_length= 255)
    degree = models.CharField(max_length= 255)
    duration = models.CharField(max_length= 255)

    def __str__(self):
        return self.name + ', ID' + str(self.id)

class UniProject(models.Model):
    name = models.CharField(max_length= 255)
    description = models.CharField(max_length= 10000)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name + ', ID' + str(self.id)