from django.shortcuts import render
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