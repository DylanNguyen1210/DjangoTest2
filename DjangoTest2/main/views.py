from django.shortcuts import render

# Create your views here.
def home(request):
    return render(
        request, 
        "home.html", 
        {
            'title': "Hi GUYS",
            'content': "Here is something"
        }
    )