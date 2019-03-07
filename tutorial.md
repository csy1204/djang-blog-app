# Django Blog Portfolio Project


``` shell
django-admin startproject week4proejct
cd week4project
python manage.py startapp blog
```

## Add blog app in INSTALLED_APPS

>./week4project/settings.py

``` python
# Application definition

INSTALLED_APPS = [
    '...',
    'blog',
]
```

## Define Blog Model

> ./blog/models.py

``` python
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]

```

## Migrate Model

``` shell
python manage.py makemigrations
python manage.py migrate
```

## Admin Configuration

> ./blog/admin.py

``` python
from django.contrib import admin
from blog.models import Blog

admin.site.register(Blog)
```

## Create Functions in Views file

> ./blog/views.py

``` python
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from blog.models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'pages']

def blog_list(request, template_name='blog/blog_list.html'):
    blog = Blog.objects.all()
    data = {}
    data['object_list'] = blog
    return render(request, template_name, data)

def blog_view(request, pk, template_name='blog/blog_detail.html'):
    blog= get_object_or_404(Blog, pk=pk)
    return render(request, template_name, {'object':blog})

def blog_create(request, template_name='blog/blog_form.html'):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog_list')
    return render(request, template_name, {'form':form})

def blog_update(request, pk, template_name='blog/blog_form.html'):
    blog= get_object_or_404(Blog, pk=pk)
    form = BlogForm(request.POST or None, instance=blog)
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
```

## Add URL Patterns

make urls.py in blog folder

> ./blog/urls.py

``` python
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('view/<int:pk>', views.blog_view, name='blog_view'),
    path('new', views.blog_create, name='blog_new'),
    path('edit/<int:pk>', views.blog_update, name='blog_edit'),
    path('delete/<int:pk>', views.blog_delete, name='blog_delete'),
]
```

> ./week4project/urls.py

``` python
# Make sure you import "include" function
from django.urls import include

urlpatterns = [
    :
    path('blog/', include('blog.urls')),
    :
]
```

