from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .forms import UserRegisterForm

"""
there are:

messages.debug
messages.info
messages.success
messages.warning
messages.error

available in messages. 
"""


# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'您已成功注册新账号：{username} ! 现在可用此账号登陆。')
            return redirect('user_login')
    else:
        form = UserRegisterForm()
    
    context = {
        'form': form
    }
    return render(request, 'user/user_register.html', context)


@login_required
def user_profile(request):
    return render(request, 'user/user_profile.html')
