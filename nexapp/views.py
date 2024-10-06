from django.shortcuts import render
from .forms import CreateUserForm

# Create your views here.
def home(request):
    return render(request, 'nexapp/home.html')

def login(request):
    return render(request, 'nexapp/login.html')

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'nexapp/signup.html',context=context)

