from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from base.forms import PersonForms
from .models import Person
from django.db.models import Q

# Create your views here.

def home(request):
    query = request.GET.get('q', '')  # Get the search query or empty string if none
    if query:
        per = Person.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) | 
            Q(email__icontains=query) | 
            Q(details__icontains=query)
        )
    else:
        per = Person.objects.all()
    
    context = {
        'per': per,
        'query': query,  # Pass query back to template to keep in search box
    }
    return render(request, 'home.html', context)


def add_person(request):
    if request.method == "POST":
        form = PersonForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_person')
    else:
        form = PersonForms

    context = {
        'form': form,
    }
    return render(request, 'add_person.html', context)

def edit_person(request, pk):
    perosn = get_object_or_404(Person, pk= pk)
    if request.method ==  "POST":
        form = PersonForms(request.POST, instance= perosn)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PersonForms(instance= perosn)
    return render(request, "edit_person.html", {"form": form})


def delete_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        person.delete()
        return redirect('home')
    return render(request, 'confirm_delete.html', {'person': person})

def about(request):
    return render(request, 'about.html')