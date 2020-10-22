from django.shortcuts import render
from . import models

def index(request):
    return render(request, 'app/index.html')
#add user and pass in database
def submit(request):
    if request.method=='GET':
        if request.GET.get('username') and request.GET.get('password'):
            saverecord = models.User()
            saverecord.username = request.GET.get('username')
            saverecord.password = request.GET.get('password')
            saverecord.save()
            return render(request, 'app/index.html')
    else:
            return render(request, 'app/index.html')
def sites(request):
    return render(request, 'app/notes.html')
#add a note to database
def notes(request):
    if request.method=='GET':
        if request.GET.get('username') and request.GET.get('note'):
            saverecord = models.Note()
            saverecord.username = request.GET.get('username')
            saverecord.note = request.GET.get('note')
            saverecord.save()
            return render(request, 'app/notes.html')
    else:
            return render(request, 'app/notes.html')
#return all the notes
def details(request):
    allnotes = models.Note.objects.all()
    return render(request, 'app/list.html', {'allnotes': allnotes})
