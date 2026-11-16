from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def valuate(request):
    return render(request, "valuate.html")


def api_docs(request):
    return render(request, "api.html")