from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def process(request):
    if request.method == "POST":
        context ={
            'fname': request.POST['first_name'],
            'lname': request.POST['last_name'],
            'email': request.POST['email'],
            'bday': request.POST['birthday'],
            'lang': request.POST['language'],
            'com': request.POST['comment']
        }
        return render(request,'results.html', context)
    return render(request,'results.html')
