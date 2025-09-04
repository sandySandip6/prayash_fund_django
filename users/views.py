from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout 
from .forms import UserRegisterForm, UserLoginForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_campaigner = True  # Set the user as a campaigner 
            user.save()
            login(request,user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    next_url = request.GET.get('next')  # get ?next=/create-campaign/ if present
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if not form.cleaned_data.get('remember_me'):
                request.session.set_expiry(0)
            return redirect(next_url or 'dashboard')  # go back if redirected by login_required
    else:
        form = UserLoginForm()
        
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')

    
        
    