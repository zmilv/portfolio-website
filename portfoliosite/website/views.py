from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from.models import Project, UniProject, WorkExperience, Education

def projects(request):
    all_projects = Project.objects.all().order_by('-id')

    template = loader.get_template('projects.html')
    context = {
        'all_projects': all_projects,
        'nbar': 'projects'
    }
    return HttpResponse(template.render(context, request))

def detail(request, project_id):

    return HttpResponse("<h2>Project #" + str(project_id) + "</h2>" +
                        "<p>" + "test" + "</p>")

def experience(request):
    all_workexperiences = WorkExperience.objects.all().order_by('-id')
    template = loader.get_template('experience.html')
    context = {
        'all_workexperiences': all_workexperiences,
        'nbar': 'experience'
    }
    return HttpResponse(template.render(context, request))

def education(request):
    all_educations = Education.objects.all().order_by('-id')
    all_uniprojects = UniProject.objects.all().order_by('-id')
    template = loader.get_template('education.html')
    context = {
        'all_educations': all_educations,
        'all_uniprojects': all_uniprojects,
        'nbar': 'education'
    }
    return HttpResponse(template.render(context, request))

def contacts(request):
    #template = loader.get_template('contacts.html')
    return render(request, 'contacts.html', {'nbar': 'contacts'})

def other(request):
    return render(request, 'other.html', {'nbar': 'other'})