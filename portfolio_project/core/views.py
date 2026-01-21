from rest_framework import viewsets
from .serializers import StudentSerializer


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required # Protects pages
#from .forms import RegisterForm # Import the form we just made
from django.shortcuts import render, redirect 
# Ensure redirect is imported
from django.shortcuts import render
from .models import Student

def home(request):
    all_students = Student.objects.all()
    return render(request, 'home.html', {'students': all_students})

def student_spa(request):
    return render(request, 'students_spa.html')

# ... (any other existing views like 'home' go here) ...
# 1. REGISTER VIEW
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() # Saves the user to DB
            login(request, user) # Auto-login after registration
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# 2. LOGIN VIEW
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Get the user object from the form
            user = form.get_user()
            login(request, user) # Starts the session
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# 3. LOGOUT VIEW
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

# 4. DASHBOARD (Protected Page)
@login_required(login_url='login') # Redirects to login if not signed in
def dashboard(request):
    return render(request, 'dashboard.html')

# API ViewSet
class StudentViewSet(viewsets.ModelViewSet):
    # 1. What data do we want? (All students)
    queryset = Student.objects.all()
    # 2. How do we turn it into JSON? (Use the serializer)
    serializer_class = StudentSerializer
