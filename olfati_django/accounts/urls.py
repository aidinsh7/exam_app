from django.urls import path

from accounts.views import EditProfileView, ResetPasswordView, SendCode, VerifyOTPView, UserView,AdminLoginView

urlpatterns = [
    path("login", SendCode.as_view()),
    path("verify-otp", VerifyOTPView.as_view()),
    path("create-user", UserView.as_view()),
    # Admin:
    path("admin-login", AdminLoginView.as_view()),
    path("admin-reset", ResetPasswordView.as_view()),
    path("admin-edite", EditProfileView.as_view()),

]
