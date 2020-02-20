from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    profile=Post.objects.filter(parent_title__contains="Skill")
    activity=Post.objects.filter(parent_title__contains="Activity")
    project=Post.objects.filter(parent_title__contains="Project")
    return render(request, 'blog/post_list.html', {'posts': posts,'profile':profile,"activity":activity,"project":project})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    profile=Post.objects.filter(parent_title__contains="Skill")
    activity=Post.objects.filter(parent_title__contains="Activity")
    project=Post.objects.filter(parent_title__contains="Project")
    return render(request, 'blog/post_detail.html', {'post': post,'profile':profile,"activity":activity,"project":project})
