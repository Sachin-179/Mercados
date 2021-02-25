from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.conf import settings
from application.views import DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="application/index.html"), name='index'),
    path(
        'account/',
        auth_views.LoginView.as_view(template_name='account/login.html', redirect_authenticated_user=True),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard')
]
