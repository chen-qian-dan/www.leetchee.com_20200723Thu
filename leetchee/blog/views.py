from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog

# Create your views here.

# blogs = [
#     {
#         'author': 'Qian', 
#         'title': 'ML', 
#         'content': 'Machine Learning', 
#         'date_posted': 'July 24, 2020', 
#     }, 
#     {
#         'author': 'dan', 
#         'title': 'CV', 
#         'content': 'Computer Vision', 
#         'date_posted': 'July 24, 2020', 
#     },
# ]
def blog_home(request):
    context = {
        'title': '博客',
        'blogs': Blog.objects.all()
    }
    return render(request, 'blog/blog_home.html', context)


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_home.html'
    context_object_name = 'blogs'
    ordering = ['-date_posted'] 


class BlogDetailView(DetailView):
    model = Blog