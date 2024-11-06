from django.shortcuts import render
from .forms import ProjectForm
from .models import Project

# Create your views here.
def addProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            
    context = {'form': form}
    return render(request, 'projectmanager/add_project.html', context)

def listProjects(request):
    projectList = Project.objects.all()
    context = {'projectList': projectList}
    return render(request, 'projectmanager/browse_project.html', context)


def projectDetails(request, id):
    project = Project.objects.get(id=id)
    context = {'projectDetails': project}
    return render(request, 'projectmanager/project_details.html', context)