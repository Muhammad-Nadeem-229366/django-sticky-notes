from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from notes.views import register_view
from django.shortcuts import redirect

urlpatterns = [
    
    # ye admin panel ka route hai jahan se database manage kiya jata hai
    path('admin/', admin.site.urls),
    
    # yahan hum notes app ke URLs include kar rahe hain
    path('notes/', include('notes.urls')),  
    
    # ye built-in Django login view hai
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    
    # ye logout view hai
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # ye custom register view hai
    path('register/', register_view, name='register'),

    # ye root URL hai jo register page pe redirect karta hai
    path('', lambda request: redirect('register')),
]