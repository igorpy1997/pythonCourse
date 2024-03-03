from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect  # noqa
from .forms import PersonForm, TriangleForm
from .models import Person


def person(request, person_id=None):
    if person_id is not None:
        person = get_object_or_404(Person, id=id)
    else:
        person = None

    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("person")
    else:
        form = PersonForm(instance=person)

    return render(request, "catalog/person_form.html", {"form": form})


def index(request):
    return HttpResponse("This is catalog")


def triangle(request):
    if request.method == "POST":
        form = TriangleForm(request.POST)
        if form.is_valid():
            cathetus1 = form.cleaned_data["cathetus1"]
            cathetus2 = form.cleaned_data["cathetus2"]
            hypotenuse = (cathetus1**2 + cathetus2**2) ** 0.5
            return render(request, "catalog/triangle.html", {"form": form, "hypotenuse": hypotenuse})
    else:
        form = TriangleForm()
    return render(request, "catalog/triangle.html", {"form": form})
