from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
import os


# Create your views here.

class MainView(TemplateView):
    template_name = 'index.html'


class RegisterUser(CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('register_done')
    form_class = UserRegisterForm

    def form_valid(self, form):
        form.save()
        return redirect('register_done')


class RegisterUserDone(TemplateView):
    template_name = 'registration/register_done.html'


@login_required
def dashboard(request):
    return render(request,
                  'registration/dashboard.html',
                  {'section': 'dashboard'})


def cv_show():
    filepath = os.path.join('static',
                            '/home/dob/PycharmProjects/my_portfolio/my_portfolio/'
                            'basic_functionality/static/Dobromir Matuszak - IT CV.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
