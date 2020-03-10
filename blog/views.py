from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Comment, Menu
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    profile=Menu.objects.filter(parent_title__contains="Profile")
    activity=Menu.objects.filter(parent_title__contains="Activity")
    project=Menu.objects.filter(parent_title__contains="Project")
    return render(request, 'blog/post_list.html', {'posts': posts,'profile':profile,"activity":activity,"project":project})

def menu_detail(request,pk):
    menu=get_object_or_404(Menu,pk=pk)
    posts = Post.objects.all()
    profile=Menu.objects.filter(parent_title__contains="Profile")
    activity=Menu.objects.filter(parent_title__contains="Activity")
    project=Menu.objects.filter(parent_title__contains="Project")
    return render(request,'blog/menu_detail.html',{'menu':menu,'profile':profile,"activity":activity,"project":project,'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    profile=Menu.objects.filter(parent_title__contains="Profile")
    activity=Menu.objects.filter(parent_title__contains="Activity")
    project=Menu.objects.filter(parent_title__contains="Project")
    return render(request, 'blog/post_detail.html', {'post': post,'profile':profile,"activity":activity,"project":project})

@login_required
def post_new(request):
    profile=Menu.objects.filter(parent_title__contains="Profile")
    activity=Menu.objects.filter(parent_title__contains="Activity")
    project=Menu.objects.filter(parent_title__contains="Project")
    if request.method == "POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm()
    return render(request,'blog/post_edit.html',{'form':form,'profile':profile,"activity":activity,"project":project})

@login_required
def post_edit(request, pk):
    profile=Menu.objects.filter(parent_title__contains="Profile")
    activity=Menu.objects.filter(parent_title__contains="Activity")
    project=Menu.objects.filter(parent_title__contains="Project")
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form,'profile':profile,"activity":activity,"project":project})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
            form=CommentForm()
    return render(request,'blog/add_comment_to_post.html',{'form':form})

@login_required
def comment_approve(request, pk):
    comment=get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment=get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail',pk=comment.post.pk)

def result(request):
    query=request.GET['query']
    if query:
        posts=posts.objects.filter(title__contains=query)
        return render(request,'result.html',{'posts',posts})
