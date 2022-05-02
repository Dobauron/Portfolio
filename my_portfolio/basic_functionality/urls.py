from django.urls import path
from . views import MainView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
urlpatterns = (
    path('', MainView.as_view(), name='main_view'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('basic_functionality:password_change_done')), name= 'password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('basic_functionality:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('basic_functionality:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name='register')
)