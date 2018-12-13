from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django import forms
from account_app.models import Account
import sys

class LoginForm(forms.Form):
    user_id = forms.CharField(label='아이디', min_length=3, max_length=20)
    user_pwd = forms.CharField(label='비밀번호', min_length=8, max_length=20,
                                widget=forms.PasswordInput(render_value=True))
    error_message = None

class RegisterForm(forms.Form):
    user_id = forms.CharField(label='아이디', min_length=3, max_length=20)
    user_pwd = forms.CharField(label='비밀번호', min_length=8, max_length=20,
                                widget=forms.PasswordInput(render_value=True))
    pwd_checker = forms.CharField(label='비밀번호 재입력', min_length=8, max_length=20,
                                widget=forms.PasswordInput(render_value=True))
    nickname = forms.CharField(label='닉네임', min_length=3, max_length=20)
    address = forms.CharField(label='주소', min_length=3, max_length=20)
    phone = forms.CharField(label='전화번호', min_length=3, max_length=20)
    error_message = None

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            request_id = clean_data['user_id']
            request_pwd = clean_data['user_pwd']
            user = authenticate(username=request_id, password=request_pwd)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                form = LoginForm()
                form.error_message = "올바르지 않은 회원 정보입니다."
                return render(request, 'account_app/login.html', {'form': form})
        else:
            form = LoginForm()
            form.error_message = "유효하지 않은 입력입니다."
            return render(request, 'account_app/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'account_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data

            # Password Check
            if clean_data['user_pwd'] != clean_data['pwd_checker']:
                # Not matched
                form = RegisterForm()
                form.error_message = "비밀번호가 맞지않습니다."
                return render(request, 'account_app/register.html', {'form': form})

            try:
                user = User.objects.create_user(username=clean_data['user_id'], password=clean_data['user_pwd'])
            except IntegrityError:
                # Already exist the ID.
                form = RegisterForm()
                form.error_message = "이미 있는 아이디입니다."
                return render(request, 'account_app/register.html', {'form': form})

            user.save()
            account = Account(
                    user=user,
                    nickname=clean_data['nickname'],
                    address=clean_data['address'],
                    phone=clean_data['phone'],
                    )
            account.save()
            return HttpResponseRedirect('login')
        else:
            # Show register page
            form = RegisterForm()
            return render(request, 'account_app/register.html', {'form': form})
    else:
        # Show register page
        form = RegisterForm()
        return render(request, 'account_app/register.html', {'form': form})
