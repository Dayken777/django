from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def registration_get_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        valid_pass = request.POST.get('valid_pass')
        emails = User.objects.all()
        user = authenticate(request, username=email, password=password)
        for item in emails:
            if str(email) == str(item):
                error = 2
                return render(request, 'registration.html', context={"error": error})
        if (valid_pass != password):
            error = 1
            return render(request, 'registration.html', context={"error": error})
        user = User.objects.create_user(username=email, password=password)
        user.first_name = name
        user.save()
        if user is not None:
            if user.is_active:
                login(request, user)
            return redirect('main')
        else:
            error = 1
            return redirect('registration')
    return render(request, 'registration.html')


def auth_get_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            return redirect('main')
        else:
            error = 1
            return redirect('auth')
    return render(request, 'auth.html')


def profile_get_page(request):
    user = User.objects.all().get(pk=request.user.pk)
    email = user.username;
    first_name = user.first_name;
    return render(request, 'personal_cabinet.html', context={'email': email, 'first_name': first_name})
