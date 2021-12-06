from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import ProjectForm 
# Create your views here.


def Project_list(request):
    projects = ProjectModel.objects.all()
    if request.method == 'POST':
        if request.user.is_authenticated:
            # A comment was posted
            key=request.POST.get("key")
            comm=request.POST.get("comment")
            cur_proj= ProjectModel.objects.get(id__exact=key)
            obj=Comment(post=cur_proj,comment=comm,commentor=request.user)
            obj.save() 
        else:
            return render(request, 'projects/unauthorised.html')          
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
    if request.user.is_authenticated:
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
    else:
        return render(request, 'projects/unauthorised.html')


def Project_delete(request, pk):
    if request.user.is_authenticated:
        project = get_object_or_404(ProjectModel, pk=pk)
        if request.user != project.creator:
            return render(request, 'projects/unauthorised.html')
        if request.method == 'POST':
            project.delete()
            return redirect('/projects/')
        else:
            return render(request, 'projects/project_delete.html', {"project": project})
    else:
        return render(request, 'projects/unauthorised.html')


def Project_Like(request,pk):

    if request.user.is_authenticated:
        cur_proj= ProjectModel.objects.get(id__exact=pk)
        user=request.user
        rating_now=ProjectRating.objects.get_or_create(user=user,project=cur_proj)[0]
        # print(f'\n\n\n {cur_proj} \n\n\n {rating_now} \n\n\n {user}')

        rating_now.like = not rating_now.like
        if not rating_now.view:
            rating_now.view= True
            cur_proj.views_count+=1

        if rating_now.like:
            cur_proj.likes_count+=1
        else:
            cur_proj.likes_count-=1

        cur_proj.save()
        rating_now.save()

        return redirect(Project_list)
    else:
        return render(request, 'projects/unauthorised.html')

def Project_View(request,pk):
    if request.user.is_authenticated:    
        cur_proj= ProjectModel.objects.get(id__exact=pk)
        user=request.user
        rating_now=ProjectRating.objects.get_or_create(user=user,project=cur_proj)[0]
        # print(f'\n\n\n {cur_proj} \n\n\n {rating_now} \n\n\n {user}')

        if not rating_now.view:
            rating_now.view = True
            cur_proj.views_count+=1

        cur_proj.save()
        rating_now.save()

        return redirect(cur_proj.link)
    else:
        return render(request, 'projects/unauthorised.html')


def Comment_Like(request,pk):
    if request.user.is_authenticated:
        cur_comment= Comment.objects.get(id__exact=pk)
        user=request.user
        rating_now=CommentRating.objects.get_or_create(user=user,comment=cur_comment)[0]
        # print(f'\n\n\n {cur_proj} \n\n\n {rating_now} \n\n\n {user}')

        rating_now.like = not rating_now.like
        if rating_now.like:
            cur_comment.likes_count+=1
        else:
            cur_comment.likes_count-=1

        cur_comment.save()
        rating_now.save()

        return redirect(Project_list)
    else:
        return render(request, 'projects/unauthorised.html')

def Comment_Del(request,pk):
    cur_comment= Comment.objects.get(id__exact=pk)
    cur_comment.delete()
    return redirect(Project_list)