from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Note
from .forms import ProjectForm, NoteForm
from django.contrib.auth.models import User

# ---------- Basic Pages ----------

def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def aboutus(request):
    return render(request, 'aboutus.html')

@login_required
def articles(request):
    return render(request, 'articles.html')

@login_required
def projects(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'projects.html', {'projects': projects})

def researches(request):
    return render(request, 'researches.html')

@login_required
def notes(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes.html', {'notes': notes})

# ---------- Dashboard ----------

@login_required
def dashboard(request):
    projects = Project.objects.filter(user=request.user)
    notes = Note.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {
        'projects': projects,
        'notes': notes
    })

# ---------- Projects ----------

@login_required
def upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            messages.success(request, "Project uploaded successfully.")
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'upload_project.html', {'form': form})

@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project updated successfully.")
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form})

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    project.delete()
    messages.success(request, "Project deleted successfully.")
    return redirect('dashboard')

# ---------- Notes ----------

@login_required
def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, "Note added successfully.")
            return redirect('dashboard')
    else:
        form = NoteForm()
    return render(request, 'upload_note.html', {'form': form})

@login_required
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Note updated successfully.")
            return redirect('dashboard')
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form})

@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.delete()
    messages.success(request, "Note deleted successfully.")
    return redirect('dashboard')
