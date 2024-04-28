from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy


class UserChangePasswordView(PasswordChangeView):
    template_name = "account/password/change-password.html"
    success_url = reverse_lazy("account:change-done")


class UserChangePasswordDoneView(PasswordChangeDoneView):
    template_name = "account/password/change-password-done.html"
    # extra_context = {"coucou": "Coucou l'extra context !"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["coucou"] = "Coucou l'extra context"
        return context


# Maintenant on reset
class UserPasswordResetView(PasswordResetView):
    template_name = "account/password/reset-password.html"
    email_template_name = "account/password/reset-password-email.html"
    success_url = reverse_lazy("account:reset-done")


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = "account/password/reset-password-done.html"


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "account/password/reset-password-confirm.html"
    success_url = reverse_lazy("account:reset-complete")
    # token_generator =


class UserPasswordCompleteView(PasswordResetCompleteView):
    template_name = "account/password/reset-password-complete.html"
