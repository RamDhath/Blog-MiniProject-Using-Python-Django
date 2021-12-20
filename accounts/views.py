from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def signin_signup(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'sign_in':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('new_post')
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('signin_signup')

        elif request.POST.get('submit') == 'sign_up':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Already Exists')
                    return redirect('signin_signup')

                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'E-mail Already Exists')
                    return redirect('signin_signup')

                else:
                    user = User.objects.create_user(
                        username=username,
                        password=password1,
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )
                    user.save()
                    return redirect('new_post')

            else:
                messages.info(request, 'Password not matching')
                return redirect('signin_signup')

        return render(request, 'signin_signup.html')

    return render(request, 'signin_signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')