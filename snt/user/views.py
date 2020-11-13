from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from user.forms import SignUpForm, ProfileForm, UserForm
from user.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

class SignUp(View):
    def get(self,request):
        if not request.user.is_authenticated:
            form = SignUpForm()
            return render(request, 'user/signup.html', {'form': form})
        else:
            return redirect('home:all')

    def post(self,request):
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                form1 = UserProfile(phone_number='', address='', alternate_email='',owner=user)
                form1.save()
                return redirect('home:all')
            else:
                ctx = {'form': form}
                return render(request, 'user/signup.html', ctx)


class ProfileUpdate(LoginRequiredMixin, View):
    def get(self, request):
        pf = get_object_or_404(UserProfile, owner=self.request.user)
        form1 = ProfileForm(instance=pf,prefix='profile')
        uf = get_object_or_404(User, username=self.request.user)
        form2 = UserForm(instance=uf,prefix='user')
        ctx = {'form1':form1, 'form2':form2}
        return render(request, 'user/user_profile.html', ctx)

    def post(self, request):
        pf = get_object_or_404(UserProfile, owner=self.request.user)
        form1 = ProfileForm(request.POST, instance=pf, prefix='profile')
        uf = get_object_or_404(User, username=self.request.user)
        form2 = UserForm(request.POST, instance=uf, prefix='user')
        if form1.is_valid() and form2.is_valid():
            profile = form1.save(commit=False)
            # profile.owner=self.request.user
            profile.save()
            form2.save()
            return redirect('home:all')
        else:
            ctx = {'form1': form1, 'form2': form2}
            return render(request, 'user/user_profile.html', ctx)

class PasswordChangeView(LoginRequiredMixin, View):
    def get(self, request):
        form = PasswordChangeForm(self.request.user)
        ctx = {'form':form}
        return render(request,'user/password_change.html', ctx)

    def post(self, request):
        form = PasswordChangeForm(self.request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home:all')
        else:
            ctx = {'form' : form}
            return render(request, 'user/password_change.html', ctx)