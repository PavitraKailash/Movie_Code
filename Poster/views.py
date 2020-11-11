from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *
from django.urls import reverse_lazy, reverse


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_request(request):
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user.is_superuser:
            login(request, user)
            print("SuperUser")
            print(request, f"You are now logged in as {username}")
            return redirect('/')
        else:
            print("User")
            print(request, f"You are now logged in as {username}")
            return redirect('Page_2')
    else:
        print(request, "Invalid username or password.")
        form = AuthenticationForm()
        return render(request = request,
                    template_name = "registration/login.html",
                    context={"form":form})




def firstPage(request):
    postcheck = Poster.objects.all().select_related("movieId")
    print(postcheck)
    # p = Poster.objects.all().select_related("movieId")
    # print(p)
    return render(request, 'firstPage.html', context={'postcheck':postcheck})


def secondPage(request):
    postcheck = Poster.objects.all().select_related("movieId")
    print(postcheck)
    # p = Poster.objects.all().select_related("movieId")
    # print(p)
    return render(request, 'secondPage.html', context={'postcheck': postcheck})


def addMovies(request):
    print("in add Movies")
    print(request.method)
    if request.method == "POST":
        print("in add Movies")
        movieForm = MovieForm(request.POST, request.FILES)
        posterForm = PosterForm(request.POST, request.FILES)
        print(movieForm.errors)
        print(movieForm.is_valid)
        print(posterForm.errors)
        print(posterForm.is_valid)
        files = request.FILES.getlist('poster')
        if movieForm.is_valid() and posterForm.is_valid():
            movieForm.save()
            movieInst = movieForm.instance
            print(movieInst)

            for f in files:
                # print("in for")
                fileInst = Poster(movieId=movieInst, poster=f)
                fileInst.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            movieForm = MovieForm()
            posterForm = PosterForm()
            return render(request, 'addMovies.html', context={'movieForm':movieForm, 'posterForm':posterForm})
    else:
        movieForm = MovieForm()
        posterForm = PosterForm()
        return render(request, 'addMovies.html', context={'movieForm': movieForm, 'posterForm':posterForm})


