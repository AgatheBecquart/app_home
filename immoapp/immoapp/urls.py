from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.urls import path

import website.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', website.views.welcome, name='welcome'),
    path('login/', LoginView.as_view(
        template_name='website/login.html',
        redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='website/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='website/password_change_done.html'),
         name='password_change_done'
         ),
    path('signup/', website.views.signup_page, name='signup'),
    path('home/', website.views.home, name='home'),
    path('contact-us/',website.views.contact, name='contact'),
    path('about-us/', website.views.about, name='about'),
    path('estimate/', website.views.estimate, name='estimate'),
    path('consult/', website.views.consult, name='consult'),
    path('<int:id>/details/', website.views.prediction_detail, name='prediction-detail'),
    path('<int:id>/change/', website.views.prediction_change, name='prediction-change'),
    path('<int:id>/delete/', website.views.prediction_delete, name='prediction-delete'),
]
