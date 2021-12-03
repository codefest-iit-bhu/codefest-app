from django.shortcuts import redirect, render
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
    else:
        form = ProjectForm
    return render(request, 'projects/submit_project.html', {'form': form})
