from smtplib import SMTPException
from django.contrib import messages
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.http import require_POST

from account.forms import SignupForm
from account.verification import send_email_verification, email_verification_token


def index_view(request):
    return render(request, "account/index.html")


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            try:
                send_email_verification(request, user)
            except SMTPException:
                # Log
                pass
            return redirect("index")
    else:
        form = SignupForm()
    return render(request, "account/signup.html", context={"form": form})


def activate(request, uidb64, token):
    user = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = user.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and email_verification_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.add_message(request, messages.INFO, "Votre compte est désormait actif, vous pouvez vous connecter")
        return redirect("index")
    else:
        messages.add_message(request, messages.INFO,
                             "Vous pouvez nous contacter par email, nous résoudrons le problème")
        return redirect("index")


class LoginUser(LoginView):
    template_name = "account/login.html"
    next_page = reverse_lazy("index")


@require_POST
def logout_view(request):
    logout(request)
    return redirect("index")
