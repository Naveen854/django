from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# Create your views here.

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects':projects})

def project(request,pk):
    project = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html',{'project':project})

def create_project(request):
    form = ProjectForm()
    if(request.method == 'POST'):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,'projects/project_form.html', context)

def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if(request.method == 'POST'):
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,'projects/project_form.html', context)

def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    context = {'object':project}
    if(request.method=="POST"):
        project.delete()
        return redirect("projects")
    return render(request,'projects/delete-project.html', context)