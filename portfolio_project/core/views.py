from django.shortcuts import render
from .models import Student # Import the model
def home(request):
# Fetch ALL students from the database
    all_students = Student.objects.all()
    # Send the data to the template inside a 'context' dictionary
    return render(request, 'home.html', {'students': all_students})