from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import ModelForm, Form
from app01 import models


class Bootstrap:
    def __int__(self,*args,**kwargs):
        super().__int__(*args,**kwargs)
        for name, field  in self.fields:
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }

class BootstrapForm(Bootstrap,Form):
    pass

class BootstrapModelForm(Bootstrap,ModelForm):
    pass