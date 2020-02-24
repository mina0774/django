from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    profile=Post.objects.filter(parent_title__contains="Profile",published_date__lte=timezone.now())
    activity=Post.objects.filter(parent_title__contains="Activity",published_date__lte=timezone.now())
    project=Post.objects.filter(parent_title__contains="Project",published_date__lte=timezone.now())
    return render(request, 'blog/post_list.html', {'posts': posts,'profile':profile,"activity":activity,"project":project})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    profile=Post.objects.filter(parent_title__contains="Profile",published_date__lte=timezone.now())
    activity=Post.objects.filter(parent_title__contains="Activity",published_date__lte=timezone.now())
    project=Post.objects.filter(parent_title__contains="Project",published_date__lte=timezone.now())
    return render(request, 'blog/post_detail.html', {'post': post,'profile':profile,"activity":activity,"project":project})

@login_required
def post_new(request):
    profile=Post.objects.filter(parent_title__contains="Profile",published_date__lte=timezone.now())
    activity=Post.objects.filter(parent_title__contains="Activity",published_date__lte=timezone.now())
    project=Post.objects.filter(parent_title__contains="Project",published_date__lte=timezone.now())
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
    profile=Post.objects.filter(parent_title__contains="Profile",published_date__lte=timezone.now())
    activity=Post.objects.filter(parent_title__contains="Activity",published_date__lte=timezone.now())
    project=Post.objects.filter(parent_title__contains="Project",published_date__lte=timezone.now())
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
