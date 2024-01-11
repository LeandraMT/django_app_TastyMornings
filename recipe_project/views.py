from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    error_message = None  # Initialize error message

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            # Django authenticate to validate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("recipes:recipes-list")
            else:
                error_message = "Invalid username or password. Please try again."
        else:
            error_message = "Oops... something went wrong."

    else:
        form = AuthenticationForm()

    context = {
        "form": form,
        "error_message": error_message,
    }

    # load the login page using the "context" information
    return render(request, "auth/login.html", context)


def logout_view(request):
    # use the pre-defined django function to logout
    logout(request)
    return redirect("login")
