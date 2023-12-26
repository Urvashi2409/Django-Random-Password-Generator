from django.shortcuts import render
import string 
import random 

# Create your views here.
def generate_password(request):
    length = 12 
    characters = string.ascii_letters + string.digits + string. punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    
    data = {
        "password" : password
    }
    return render(request, "password.html", data)