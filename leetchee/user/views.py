from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'新生成账号：{username}!')
            return redirect('page_home')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    return render(request, 'user/user_register.html', context)
