from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User 
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView, 
)
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
    paginate_by = 2


class BlogUserBlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_user_blogs.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Blog.objects.filter(author=user).order_by('-date_posted')


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog/blog_create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'blog/blog_create.html'
    fields = ['title', 'content']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True 
        return False 


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/blog/'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False 
