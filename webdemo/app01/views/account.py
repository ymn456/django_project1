from django.forms import forms
from django.shortcuts import render, redirect

from app01.utils.Bootstrap import BootstrapForm
from django import forms
from app01 import models

from app01.utils.form import encrypt


class LoginForm(BootstrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput,
        required=True
    )
    def clean_password(self):
        pwd = encrypt(self.cleaned_data.get("password"))
        return pwd


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form":form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        admin_object = models.admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, "login.html", {"form":form})

        request.session["info"] = {"id":admin_object.id, "username":admin_object.username}
        request.session.set_expiry(60 * 60)
        return redirect("/user/list/")


def logout(request):
    request.session.clear()
    return redirect("/login/")
