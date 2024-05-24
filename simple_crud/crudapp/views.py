from django.shortcuts import render
from .models import Student
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def index(request):
    students = Student.objects.all()
    search_query = ""
    if request.method == "POST":
        if "create" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            place = request.POST.get("place")
            cls = request.POST.get("class")
            Student.objects.create(
                name=name,
                email=email,
                place=place,
                cls=cls
            )
            messages.success(request, "student added successfully")

        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")
            place = request.POST.get("place")
            cls = request.POST.get("class")
            student = Student.objects.get(id=id)
            student.name = name
            student.email = email
            student.place = place
            student.cls = cls
            student.save()
            messages.success(request, "student updated successfully")
        
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Student.objects.get(id=id).delete()
            messages.success(request, "student deleted successfully")

        elif "search" in request.POST:
            search_query = request.POST.get("query")
            students = Student.objects.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query) | Q(place__icontains=search_query) | Q(cls__icontains=search_query))

    context = {"students": students, "search_query": search_query}
    return render(request, "index.html", context=context)

