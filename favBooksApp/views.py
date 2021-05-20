# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import *


def index(request):
    return render(request, "mark5.html")

def Ribs(request):
    errorFromTheValidator = Users.objects.i_am_the_validator(request.POST)

    print("Errors from the Validator is HERE!!!", errorFromTheValidator)

    if len(errorFromTheValidator)>0:
        for key, value in errorFromTheValidator.items():
            messages.error(request, value)
        return redirect("/")
            

    newuser = Users.objects.create(first_name = request.POST["fname"], last_name = request.POST["lname"], email = request.POST["eml"], password = request.POST["PW"])

    request.session["UserID"] = newuser.id
    
    return redirect("/books")

def newsFeed(request):
    print("********************")
    print(request.POST)
    print("********************")
    if "UserID" not in request.session:
        return redirect("/")


    

    context = {
        'Pickachu': Users.objects.get(id=request.session["UserID"]),
        'booklist': Book.objects.all()
    }



    return render(request, "newsfeed.html", context)

def login(request):
    

    errorFromTheValidator = Users.objects.loginVal(request.POST)
    if len(errorFromTheValidator)>0:
        for key, value in errorFromTheValidator.items():
            messages.error(request, value)
        return redirect("/")

    else: 
        user = Users.objects.get(email = request.POST['eml']) 

        request.session["UserID"] = user.id

        return redirect("/books")

def logout(request):
    request.session.clear()
    return redirect("/")

def newBook(request):

    Book.objects.create(title = request.POST["tt"], desc = request.POST["desc"], uploaded_by = Users.objects.get(id=request.session["UserID"]))

    return redirect("/books")

def bookinfo(request, bookId):
    context = {
        'Pickachu': Users.objects.get(id=request.session["UserID"]),
        "oneBooks": Book.objects.get(id=bookId),
    }
    return render(request, "bookinfo.html", context)

def liked(request, bookId):
    book = Book.objects.get(id = bookId)
    book.wholiked.add(Users.objects.get(id=request.session["UserID"]))
    context = {
        'Pickachu': Users.objects.get(id=request.session["UserID"]),
        "oneBooks": Book.objects.get(id=bookId),
    }

    return render(request, "Favbook.html", context)