from email import contentmanager
import imp
from importlib.metadata import requires
from django.shortcuts import redirect, render
from django.template import context
from .models import Podcaster,Podcast,Message;
from .forms import MessageForm,PodcastForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
 


# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.object.get(username=username)
        except:
            messages.error(request, 'اطلاعات معتبر نیست')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'اطلاعات کاربر موجود نیست')

    context = {}
    return render(request, 'podcast/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')


def index(request):
    last_ep = Podcast.objects.latest('id')

    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    messages = Message.objects.all()
    context = {'form':form, 'messages':messages, 'last_ep':last_ep}
    return render(request, 'podcast/index.html',context)


def me(request, pk):
    message = Message.objects.get(id=pk)
    form = MessageForm(instance=message)
    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            #return redirect('index')

    messages = Message.objects.all()
    context = {'form':form, 'messages':messages}
    return render(request, 'podcast/index.html',context)


def main(request):
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    messages = Message.objects.all()
    context = {'form':form, 'messages':messages}
    return render(request, 'podcast/main.html', context)

def podcasters(request):
    podcaster = Podcaster.objects.all()
    context = {'podcaster': podcaster}
    return render(request, 'podcast/podcasters.html', context)


def archive(request):
    podcasts = Podcast.objects.all()
    context={'podcasts':podcasts}
    return render (request, 'podcast/archive.html', context)

def podcastForm(request):
    form = PodcastForm()
    podcasts = Podcast.objects.all()
    if request.method == 'POST':
        form = PodcastForm(request.POST,request.FILES)
        if form.is_valid():
            podcast = form.save()
            podcast.save()
            return redirect ('archive')

    context={'form':form, 'podcasts': podcasts}
    return render(request, 'podcast/podcast_form.html', context)

@login_required(login_url='login')
def podcastEdit(request, pk):    
    podcast = Podcast.objects.get(id=pk)
    form = PodcastForm(instance=podcast)
    podcasts = Podcast.objects.all()
    if request.method == 'POST':
        form = PodcastForm(request.POST,request.FILES, instance=podcast)
        if form.is_valid():
            form.save()
            return redirect ('archive')

    context={'form':form, }
    return render(request, 'podcast/podcast_form.html', context)


def sp(request):
    return render(request, 'podcast/sp.html')

def team(request):
    return render(request, 'podcast/team.html')

@login_required(login_url='login')
def podcastDelete(request,pk):
    podcast = Podcast.objects.get(id=pk)
    if request.method == 'POST':
        podcast.delete()
        return redirect('archive')
    return render(request, 'podcast/podcast_delete.html', {'obj':podcast})
