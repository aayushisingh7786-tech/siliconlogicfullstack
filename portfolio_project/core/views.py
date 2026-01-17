from django.shortcuts import render
from django.http import HttpResponse

# View for the Home Page
def home(request):
    # This renders an HTML template named 'home.html'
    return render(request, 'home.html')
# View for the About Page
def about(request):
    return render(request, 'about.html')

# View for the Contact Page
def contact(request):
    return render(request, 'contact.html')