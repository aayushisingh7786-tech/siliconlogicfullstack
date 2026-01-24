from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# ... other imports ...
from core import views # Import the new views
from django.conf import settings
from django.conf.urls.static import static
#from . import views

##router = DefaultRouter()
#router.register(r'students', views.StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #path('api/', include(router.urls)),
    #path('spa/', views.student_spa, name='spa'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
