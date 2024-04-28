from django.urls import path

from account.views import signup_view, activate, LoginUser, logout_view, UserChangePasswordView, \
    UserChangePasswordDoneView, UserPasswordResetView, UserPasswordResetDoneView, UserPasswordResetConfirmView, \
    UserPasswordCompleteView

app_name = "account"
urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_view, name="logout"),

    # Password
    # Change
    path('change-password/', UserChangePasswordView.as_view(), name="change-password"),
    path('change-done/', UserChangePasswordDoneView.as_view(), name="change-done"),

    # Reset
    path('reset-password/', UserPasswordResetView.as_view(), name="reset"),
    path('reset-password-done/', UserPasswordResetDoneView.as_view(), name="reset-done"),
    path('reset-password-confirm/<str:uidb64>/<str:token>/', UserPasswordResetConfirmView.as_view(),
         name="reset-confirm"),
    path('reset-password-complete/', UserPasswordCompleteView.as_view(), name="reset-complete"),
]
