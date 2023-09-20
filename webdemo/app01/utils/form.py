
from hashlib import md5

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django import forms

from app01 import models
from app01.utils.Bootstrap import BootstrapModelForm

def encrypt(s):
    return md5(s.encode('utf-8')).hexdigest()

class AdminEditModelForm(BootstrapModelForm):
    class Meta:
        model = models.admin
        fields = ["username"]

class AdminResetModelForm(BootstrapModelForm):
    confirm_password = forms.CharField(
        label = "确认密码",
        widget = forms.PasswordInput()
    )
    class Meta:
        model = models.admin
        fields = ["password","confirm_password"]

    def clean_password(self):
        pwd = encrypt(self.cleaned_data.get("password"))
        return pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        conform_pwd = encrypt(self.cleaned_data.get("confirm_password"))
        if pwd != conform_pwd:
            raise ValidationError("密码不一致")
        else:
            return conform_pwd

class AdminModelForm(BootstrapModelForm):
    confirm_password = forms.CharField(
        label = "确认密码",
        widget= forms.PasswordInput()
    )
    class Meta:
        model = models.admin
        fields = ["username","password","confirm_password"]


    def clean_password(self):
        pwd = encrypt(self.cleaned_data.get("password"))
        return pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        conform_pwd = encrypt(self.cleaned_data.get("confirm_password"))
        if pwd != conform_pwd:
            raise ValidationError("密码不一致")
        else:
            return conform_pwd

class UserModelform(BootstrapModelForm):
    class Meta:
        model = models.data_user
        fields = ["name", "password", "age", 'account', 'create_time', "gender", "depart"]


class PrettyModelForm(BootstrapModelForm):
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', "手机号格式错误"), ],
    )

    class Meta:
        model = models.PrettyNum
        fields = ["mobile", 'price', 'level', 'status']

    def clean_mobile(self):
        text_mobile = self.cleaned_data["mobile"]
        flag = models.PrettyNum.objects.filter(mobile=text_mobile).exists()
        if flag:
            raise ValidationError("手机号已存在")
        else:
            return text_mobile