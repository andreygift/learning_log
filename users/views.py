from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm

# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
    
def singup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)
        
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'learning_logs/topics.html', {'new_user': new_user})
    else:
        # Create a empty form
        user_form = UserRegistrationForm()
    
    context = {'user_form': user_form}
    return render (request , 'users/singup.html', context)
