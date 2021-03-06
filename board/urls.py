"""board URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import static
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy

from accounts import views as accounts_views

from boards import views

urlpatterns = (
    url(r'^$', views.home, name='home'),

    url(r'^password/reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset_form.html',
            html_email_template_name='password_reset_email.html',
            title ='Password Reset',
            email_template_name='password_reset_email.html',
            subject_template_name ='password_reset_subject.txt',
            success_url= reverse_lazy('password_reset_done'),



        ),
        name='password_reset'),


    url(r'^password/reset/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html',
        ),
        name='password_reset_done'),



    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html',
            success_url= reverse_lazy('login'),
        ),
        name='password_reset_change'),


    url(r'^password/reset/change/$',
        auth_views.PasswordChangeView.as_view(
            template_name='password_reset_change.html',
            success_url= reverse_lazy('login'),

        ),
        name='password_reset_change'),


    url(r'^password/reset/change_done/$',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='password_reset_change_done.html',

        ),
        name='password_reset_change_done'),

    url(r'^password/reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_change_done.html',

        ),
        name='password_reset_complete'),



    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^login/$', auth_views.LoginView.as_view(
        template_name='login.html',
        redirect_field_name = 'LOGIN_REDIRECT_URL',
        redirect_authenticated_user = True,
    ), name='login'),

    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='board_topics_new'),
    path('admin/', admin.site.urls),


)