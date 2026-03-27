from django import forms
from .models import Note

# ye ModelForm hai jo Note model ke basis par automatically form generate karta hai
# is form ko hum note create aur edit dono cases me use karte hain
class NoteForm(forms.ModelForm):
    
    class Meta:
        model = Note
        
        # sirf ye fields user ko input ke liye dikhayi ja rahi hain
        # owner aur timestamps automatically handle hote hain is liye hide kiye gaye hain
        fields = ['title', 'content', 'color']
        
        # widgets ka use karke hum form fields ko Bootstrap styling de rahe hain
        # taake UI clean aur professional lage
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),     
            # ye title ke liye input field hai
            
            'content': forms.Textarea(attrs={'class': 'form-control'}),    
            # ye content ke liye textarea hai jahan user note likhta hai
            
            'color': forms.TextInput(attrs={'class': 'form-control'}),     
            # ye color field hai jahan hex code input hota hai (background color ke liye)
        }