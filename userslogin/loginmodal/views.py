from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# Create your views here.
#index page
def index(request):
    return render(request, 'index.html')


#enforces login to access the portal page
@login_required(login_url="/login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def portal(request):
    return render(request, 'portal.html')

#To ensure user login to access portal
def Login(request):
    if request.user.is_authenticated:
        return render(render, 'portal.html')
    else:
        messages.info(request, 'Please login to access the portal')
        return HttpResponseRedirect('/')
    
#To validate login credential for access
def userLogin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user != None:
            login(request, user)
            messages.info(request, 'Login is succesful')
            return HttpResponseRedirect('/portal')
        else:
            messages.error(request, 'Invalid login credentions, please try again')
            return HttpResponseRedirect('/')

#Logout from the portal
def userLogout(request):
    logout(request)
    request.user= None
    return HttpResponseRedirect('/')


