from django.shortcuts import render
from ogatech_app.forms import UserForm, UserProfileInfoForm

#
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required




# Create your views here.
def index(request):
    return render(request,'ogatech_app/index.html')
# def other(request):
#     return render(request,'ogatech_app/other.html')
# def relative(request):
#     return render(request,'ogatech_app/relative_url_templates.html')
def pricing(request):
    return render(request,'ogatech_app/pricing.html')
@login_required
def special(request):
    return HttpResponse("You are logged in!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        # address_form = AddressModelOtechForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            # address = address_form.save(commit=False)
            # address.user = user

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        # address_form = AddressModelOtechForm()

    return render(request, 'ogatech_app/registration.html',
                  {
                      'user_form': user_form,
                      'profile_form': profile_form,
                      'registered': registered
                  }

                  )


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("someone tried to login and failed!")
            print(f"Username:{username} and password {password}")
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request, 'ogatech_app/login.html', {})
