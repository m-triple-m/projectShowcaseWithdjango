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
    q = request.GET.get('q', None)
    technology = request.GET.get('technology', None)
    projectList = Project.objects.all()
    print(technology)
    if q:
        projectList = projectList.filter(title__icontains=q)
    if technology:
        projectList = projectList.filter(technology=technology)
    context = {'projectList': projectList, 'q' : q}
    return render(request, 'projectmanager/browse_project.html', context)


def projectDetails(request, id):
    project = Project.objects.get(id=id)
    context = {'projectDetails': project}
    return render(request, 'projectmanager/project_details.html', context)