from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.messages import info, success, warning, error
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Room, Topic, Messages
from .forms import RoomForm
from django.contrib.auth.forms import UserCreationForm


def userProfile(request,pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.messages_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms,
               'room_messages': room_messages, 'topics': topics}
    return render(request,'base/user_profile.html',context)
def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    page = 'register'
    form = UserCreationForm()
    #form = MyUserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    #     form = MyUserCreationForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.username = user.username.lower()
           user.save()
           login(request, user)
           return redirect('home')
        else:
            error(request, 'An error occurred during registration')
    context = {'form':form}
    return render(request,'base/login_register.html',context)

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
      return redirect('home')
 
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username,password=password)
        except:
            error(request, 'User does not exist')

        user = authenticate(request, username=username)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error(request, 'Username OR password does not exit')

    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
     Q(topic__name__icontains=q) |
     Q(name__icontains=q)| 
     Q(description__icontains=q))
    topics = Topic.objects.all()
    room_count = rooms.count()
    room_messages = Messages.objects.filter(Q(room__topic__name__icontains=q))
    context = {'rooms':rooms,'topics':topics,'room_count':room_count,'room_messages':room_messages}
    return  render(request,'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    room_messages = room.messages_set.all()
    participants = room.participants.all()
    if request.method == 'POST':
        message = Messages.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    context = {'room':room,'room_messages':room_messages,'participants':participants}
    return render(request,'base/room.html',context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    context = {'form':form}
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room = request.user
            room.save()
            return redirect('home')
    return render(request,'base/room_form.html',context)  

@login_required(login_url='login')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    #Only room host can update the room
    if request.user != room.host:
       return HttpResponse('You are not allowed to edit this room!')
    context = {'form':form}
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'base/room_form.html',context)

@login_required(login_url='login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})

@login_required(login_url='login')
def deleteMessage(request,pk):
    message = Messages.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':message})