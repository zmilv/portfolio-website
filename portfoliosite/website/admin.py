from django.contrib import admin
from .models import Project, Print, WorkExperience, UniProject, Education

# Register your models here.

admin.site.register(Project)
admin.site.register(Print)
admin.site.register(WorkExperience)
admin.site.register(UniProject)
admin.site.register(Education)