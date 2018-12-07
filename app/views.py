from django.shortcuts import render, redirect
from django.views import View
from . import forms
from app import models

# Create your views here.
class Note(View):
    def get(self, request):
        return render(request, 'note.html', {'form': forms.NoteForm()})

    def post(self, request):
        form = forms.NoteForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            models.NoteModel.submitted({'name': name, 'message': message})
            return redirect('./')
        else:
            return render(request, 'note.html', {'form': form})

class Home(View):
    def get(self, request):
        return render(request, 'homepage.html')
