from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import login, logout, authenticate

# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
    
def singup(request):
    if request.method != 'POST':
        # Create a empty form
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    
    context = {'form': form}
    return render (request , 'users/singup.html', context)
