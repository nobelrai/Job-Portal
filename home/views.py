from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        "title": "Kaam Milau",
    }
    return render(request, "home.html", context)
