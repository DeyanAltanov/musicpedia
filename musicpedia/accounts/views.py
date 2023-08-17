from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from musicpedia.accounts.forms import LoginForm, ProfileForm, RegisterForm
from musicpedia.accounts.models import Profile


def get_profile():
    return Profile.objects.first()


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }

    return render(request, 'login.html', context)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


@login_required
def logout_user(request):
    logout(request)
    return redirect('home')