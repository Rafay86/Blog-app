from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import post


def home(request):
    context={
        'posts': post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model= post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model= post
    
def about(request):
    return render(request,'blog/about.html',{'title':'About'})


