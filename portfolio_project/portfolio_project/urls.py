"""
URL configuration for portfolio_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
#from .views import StudentViewSet
from core import views # Import your views from the core app

router = DefaultRouter()
router.register2(r'students',StudentViewSet,basename = 'student')


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.home, name='home'),
   path('register2/', views.register2_view, name='register2'),
   path('login/', views.login_view, name='login'),
   path('logout/', views.logout_view, name='logout'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('api/',include(router.urls)),
]
"""

#from django.contrib import admin
#from django.urls import path, include
#from rest_framework.routers import DefaultRouter
#from core import views


# Initialize the router and register the StudentViewSet

#router = DefaultRouter()
#router.register(r'students', views.StudentViewSet, basename='student')

#urlpatterns = [
    #path('admin/', admin.site.urls),
    # Existing website URL
  
    #path('dashboard/', views.dashboard, name='dashboard'),
    # NEW: API endpoints prefix
    #path('api/', include(router.urls)),
   # path('spa/', views.student_spa, name='spa'), # Access at /spa/
#]
# urls.py
#rom django.urls import path
#from . import views 
#from portfolio_project import views  # Or from . import reviews

#urlpatterns = [
    #path('', views.home, name='home'),
    # Ensure 'student_spa' is the actual function name in views.py
  #  path('spa/', views.student_spa, name='spa'), 
#]
# In core/views.py

from django.contrib import admin
from django.urls import path
from core import views # Or from . import views if in the same app's urls.py



urlpatterns = [
    path('admin/', admin.site.urls),
    path('spa/', views.student_spa, name='spa'),

    
]
