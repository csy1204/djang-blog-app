from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Blog
from django.core.paginator import Paginator
from django.utils import timezone
import datetime
from .forms import BlogPost


def blog_list(request, template_name='blog/blog_list.html'):
    blog = Blog.objects.all()
    pages = Paginator(blog,  3)
    page_num = request.GET.get('page',1)
    posts = pages.get_page(page_num)
    data = {}
    data['blogs'] = blog
    data['posts'] = posts
    return render(request, template_name, data)

def blog_view(request, pk, template_name='blog/blog_detail.html'):
    blog= get_object_or_404(Blog, pk=pk)
    return render(request, template_name, {'object':blog})

def blog_new(request, template_name='blog/blog_new.html'):
    return render(request, template_name)

def blog_create(request):
    if request.method == "POST":
        blog = Blog()
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        if request.POST['image']:
            blog.image = request.POST['image']
        blog.created_at = timezone.datetime.now()
        blog.updated_at =timezone.datetime.now() + datetime.timedelta(days=15)
        blog.save()
        return redirect('blog')
    return redirect('blog')

def blogpost(request):
    # 1. 입력된 내용 처리 기능
    # 2. 빈 페이지 띄워주는 기능
    if request.method == "POST":
        form = BlogPost(request.POST, request.FILES)
        print("POST로 통신이 왔습니다.")
        if form.is_valid():
            print("모두 정상적입니다.")
            post = form.save(commit=False)
            # post.image = request.POST.get('image')
            # post.created_at = timezone.datetime.now()
            post.save()
            return redirect('blog')
    else:
        form = BlogPost()
        return render(request, 'blog/blog_new.html', {'form':form})

def blog_update(request, pk, template_name='blog/blog_form.html'):
    blog= get_object_or_404(Blog, pk=pk)
    if form.is_valid():
        form.save()
        return redirect('blog_list')
    return render(request, template_name, {'form':form})

def blog_delete(request, pk, template_name='blog/blog_confirm_delete.html'):
    blog= get_object_or_404(Blog, pk=pk)
    if request.method=='POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, template_name, {'object':blog})