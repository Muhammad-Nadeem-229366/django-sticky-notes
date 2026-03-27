from django.urls import path
from . import views

# yahan hum notes app ke saare URLs define kar rahe hain
# har URL ek specific view function ke sath map hota hai jo request handle karta hai

urlpatterns = [
    
    # ye main/home route hai jahan user ke saare notes display hote hain
    # sirf logged-in user ke notes show hote hain
    path('', views.note_list, name='note_list'),
    
    # ye route naya note create karne ke liye use hota hai
    # yahan form show hota hai aur submit hone par note save hota hai
    path('new/', views.note_create, name='note_create'),
    
    # ye route kisi existing note ko edit/update karne ke liye hai
    # <int:id> ka matlab hai ke hum specific note ko id ke zariye access kar rahe hain
    path('<int:id>/edit/', views.note_edit, name='note_edit'),
    
    # ye route note delete karne ke liye hai
    # pehle confirmation page show hota hai phir POST request par delete hota hai
    path('<int:id>/delete/', views.note_delete, name='note_delete'),
]