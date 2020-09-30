from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.info(request,f"Account Successfully created {username}!!")
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'account/signup.html', {'form':form})