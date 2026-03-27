from django.shortcuts import render
from django.contrib import messages
# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# ye decorator ensure karta hai ke sirf logged-in user hi is page ko access kare
# ye function current user ke saare notes database se fetch karke show karta hai
@login_required
def note_list(request):
    # sirf woh notes la rahe hain jo current user ke hain
    notes = Note.objects.filter(owner=request.user)
    return render(request, 'note_list.html', {'notes': notes})


# ye function naya note create karne ke liye use hota hai
@login_required
def note_create(request):
    # agar user ne form submit kiya hai (POST request)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        
        # agar form valid hai to data save karein
        if form.is_valid():
            note = form.save(commit=False)  # abhi database me save nahi kar rahe
            note.owner = request.user       # note ko current user assign kar rahe hain
            note.save()                     # ab database me save kar diya
            
            return redirect('note_list')    # save hone ke baad list page par redirect

    else:
        # agar GET request hai to empty form show karo
        form = NoteForm()

    return render(request, 'note_form.html', {'form': form})


# ye function existing note ko edit/update karta hai
@login_required
def note_edit(request, id):
    # check kar rahe hain ke note exist karta hai aur current user ka hi hai
    note = get_object_or_404(Note, id=id, owner=request.user)
    
    # form ko existing data ke sath load kar rahe hain
    form = NoteForm(request.POST or None, instance=note)
    
    # agar form valid hai to changes save karo
    if form.is_valid():
        form.save()
        return redirect('note_list')

    return render(request, 'note_form.html', {'form': form})


# ye function note delete karta hai lekin pehle confirmation page dikhata hai
@login_required
def note_delete(request, id):
    # note ko fetch kar rahe hain jo delete karna hai
    note = get_object_or_404(Note, id=id, owner=request.user)
    
    # agar user ne confirm kar diya (POST request)
    if request.method == 'POST':
        note.delete()                 # note delete ho gaya
        return redirect('note_list')  # wapas list page par jao

    # agar GET request hai to confirmation page show karo
    return render(request, 'note_confirm_delete.html', {'note': note})


# ye function new user ko register karta hai
def register_view(request):
    # form ko POST data ke sath initialize kar rahe hain
    form = UserCreationForm(request.POST or None)

    # agar form valid hai to new user create karo
    if form.is_valid():
        user = form.save()
        
        # success message show kar rahe hain
        messages.success(request, "Account created successfully! You can now login.")
        
        return redirect('login')   # login page par redirect

    # agar POST request hai aur form me error hai
    elif request.method == 'POST':
        messages.error(request, "Please fix the errors below.")

    return render(request, 'register.html', {'form': form})