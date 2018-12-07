from django.db import models

# Create your models here.
class NoteModel(models.Model):
    name = models.TextField()
    date = models.DateField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.name

    @staticmethod
    def submitted(dict):
        NoteModel(name=dict['name'], message=dict['message']).save()
