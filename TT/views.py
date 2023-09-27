from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import UserProfileModel, RoomMessages, Room
import json
from django.http import JsonResponse
from .models import Room, RoomMessages


# Create your views here.
class Registration(View):
    def get(self, request):
        form = UserRegistrationForm()
        context = {'form':form}
        return render(request, 'signUp.html', context)
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        #import pdb;pdb.set_trace()
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Register Successfully")
            return redirect('signin')
        else:
            context = {'form':form}
            return render(request, 'signUp.html', context)

class SignIn(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'signIn.html', {'form': form})
    
    def post(self, request):
        userN = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = userN   , password = password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            form = UserLoginForm()
            messages.success(request, "User is not in database, try different username or passowrd")
            return render(request, 'signIn.html', {'form': form})

class Profile(View):
    def get(self, request):
        try:
            userProfile = UserProfileModel.objects.get(user=request.user)
            # If the user profile exists, redirect to 'dashboard'
            return redirect('dashboard')
        except UserProfileModel.DoesNotExist:
            # If the user profile does not exist, create a new one and then redirect to dashboard
            form = UserProfileForm()
            return render(request, 'profile.html', {'form': form})
    
    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            dateOfBirth = form.cleaned_data['dateOfBirth']
            picture = form.cleaned_data['picture']
            obj = UserProfileModel(user = user, firstName = firstName, lastName = lastName, dateOfBirth = dateOfBirth, picture = picture)
            obj.save()
            messages.success(request, "Profile update Successfully")
            return redirect('dashboard')
        else:
            return render(request, 'profile.html', {'form': form.errors})

class Dashboard(View):
    def get(self, request):
        allrooms = Room.objects.filter(roomMembers=request.user)
    
        context = {
            'allrooms': allrooms,
            'user_rooms': Room.objects.filter(roomMembers=request.user),  # Get all user's rooms
        }
        return render(request, "dashboard.html", context)

    def post(self, request):
        room_name = request.POST.get('room-name-input')
        if room_name:
            try:
                existRoom = Room.objects.get(name=room_name)
                if existRoom:
                    if request.user not in existRoom.roomMembers.all():
                        existRoom.roomMembers.add(request.user)
                    messages = RoomMessages.objects.filter(room=existRoom)[:25]
                allrooms = Room.objects.filter(roomMembers=request.user)
                
                context = {
                    'room_name': room_name,
                    'allrooms': allrooms,
                    'user_rooms': Room.objects.filter(roomMembers=request.user),  # Get all user's rooms
                    'messages': messages
                }
                return render(request, "dashboard.html", context)

            except Room.DoesNotExist:
                room = Room(name=room_name)
                room.save()
                room.roomMembers.add(request.user)
                allrooms = Room.objects.filter(roomMembers=request.user)
                
                context = {
                    'room_name': room_name,
                    'allrooms': allrooms,
                    'user_rooms': Room.objects.filter(roomMembers=request.user),  # Get all user's rooms
                }
                return render(request, "dashboard.html", context)

        

def displayroom(request, pk):
    roomObject = Room.objects.get(id = pk)
    room_name = roomObject.name
    allrooms = Room.objects.filter(roomMembers=request.user)
    existRoom = Room.objects.get(name=room_name)
    messages = RoomMessages.objects.filter(room=existRoom)[:25]
    context = {
        'room_name': room_name,
        'messages': messages,
        'allrooms': allrooms
    }
    return render(request, "dashboard.html", context)

