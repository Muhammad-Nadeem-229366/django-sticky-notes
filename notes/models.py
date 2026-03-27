from django.db import models
from django.contrib.auth.models import User

# ye Note model hai jo har user ke notes ko database me store karta hai
class Note(models.Model):
    
    # note ka title store karta hai (max 200 characters)
    title = models.CharField(max_length=200)
    
    # note ka main content/text store karta hai
    content = models.TextField()
    
    # note ka background color store karta hai (hex code format)
    color = models.CharField(max_length=7, default='#FFFF99')
    
    # ye field automatically note banne ka time save karti hai
    created_at = models.DateTimeField(auto_now_add=True)
    
    # ye field automatically last update ka time save karti hai
    updated_at = models.DateTimeField(auto_now=True)
    
    # ye batata hai ke ye note kis user ka hai (relationship with User model)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # ye function admin panel ya shell me object ka readable name return karta hai
    def __str__(self):
        return self.title

# Create your models here.