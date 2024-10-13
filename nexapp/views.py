from django.shortcuts import render, redirect
from .forms import CreateUserForm, CollegeSearchform
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import College


# Create your views here.
def home(request):
    return render(request, 'nexapp/home.html')

def user_login(request):  # Renamed from login to user_login
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # This is the Django auth login function
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request, 'nexapp/login.html')


def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'nexapp/signup.html',context=context)

def search_colleges(request):
    query_result = None
    if request.method == 'POST':
        form = CollegeSearchform(request.POST)
        if form.is_valid():
            institute_name = form.cleaned_data['institute_name']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            course = form.cleaned_data['course']
            govt = form.cleaned_data['govt']

            query = College.objects.all()

            if institute_name:
                query = query.filter(institute_name__icontains=institute_name)
            if city:
                query = query.filter(city__icontains=city)
            if state:
                query = query.filter(state__icontains=state)
            if course:
                query = query.filter(course__icontains=course)
            if govt is not None:
                query = query.filter(govt=govt)

            query_result = query
    else:
        form = CollegeSearchform()
        
    return render(request, 'nexapp/college.html', {'form':form, 'query_result':query_result})