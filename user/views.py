from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('blog-home')
        else:
            messages.error(request, f'Account issues')
            form = UserCreationForm()

    else:
        form = UserCreationForm()
    context = {
        'form' : form,
        'title': 'Register'
    }
    return render(request, 'user/register.html', context)