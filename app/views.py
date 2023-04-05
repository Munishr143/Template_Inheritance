from django.shortcuts import render

# Create your views here.
def Parent(request):
    return render(request, 'parent.html')


def Child(request):
    return render(request, 'child.html')