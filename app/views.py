from django.shortcuts import render
from django.views import View
from . import forms

# Create your views here.
class Note(View):
    def get(self, request):
        return render(request, 'app/note.html', {'form': forms.NoteForm()})

    def post(self, request):
        form = forms.NoteForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            return render(request, 'app/note.html', {'name': name, 'message': message, 'form': form})
        else:
            return render(request, 'app/note.html', {'form': form})
