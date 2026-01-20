# In core/views.py

from django.shortcuts import render
from django.http import HttpResponse # Import if using HttpResponse





def student_spa(request):
    # Your view logic here
    return render(request, 'students_spa.html')
    # or return HttpResponse("This is the student SPA page")







