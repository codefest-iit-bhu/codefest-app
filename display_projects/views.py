from django.shortcuts import get_object_or_404, redirect, render
from .models import ProjectModel
from .forms import ProjectForm
# Create your views here.


def Project_list(request):
    projects = ProjectModel.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


def Submit_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            if(request.user):
                post.creator = request.user
            else:
                print("No user")
            post.screenshot = form.cleaned_data.get("screenshot")
            post.save()
            return redirect('/projects/')
    else:
        form = ProjectForm
    return render(request, 'projects/project_edit.html', {'form': form, 'type': 'submit'})


def Project_detail(request, pk):
    project = ProjectModel.objects.get(pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})


def Project_edit(request, pk):
    project = get_object_or_404(ProjectModel, pk=pk)
    if request.user != project.creator:
        return render(request, 'projects/unauthorised.html')
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            post = form.save(commit=False)
            post.screenshot = form.cleaned_data.get("screenshot")
            post.save()
            return redirect('/projectdetails/' + str(project.pk) + '/')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_edit.html', {'form': form, 'type': 'edit',  'project': project})


def Project_delete(request, pk):
    project = get_object_or_404(ProjectModel, pk=pk)
    if request.user != project.creator:
        return render(request, 'projects/unauthorised.html')
    if request.method == 'POST':
        project.delete()
        return redirect('/projects/')
    else:
        return render(request, 'projects/project_delete.html', {"project": project})
