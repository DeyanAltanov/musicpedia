from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from musicpedia.accounts.forms import LoginForm, RegisterForm, ProfileForm
from musicpedia.accounts.models import Profile
from musicpedia.music.models import Review


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


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)

    reviews = Review.objects.filter(user=profile)

    context = {
        'form': form,
        'reviews': reviews,
        'profile': profile,
    }

    return render(request, 'profile_details.html', context)


@login_required
def user_details(request, pk):
    user = Profile.objects.get(pk=pk)
    reviews = Review.objects.filter(user=user)

    context = {
        'reviews': reviews,
        'profile': user,
    }

    return render(request, 'user_details.html', context)