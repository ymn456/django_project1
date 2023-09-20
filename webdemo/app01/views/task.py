import json

from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app01.utils.Bootstrap import BootstrapModelForm
from app01 import models
from app01.utils.pagination import pagination


class TaskModelForm(BootstrapModelForm):
    class Meta:
        model = models.task
        fields = "__all__"
        widgets = {
            "detail":forms.TextInput
        }

def task_list(request):
    queryset = models.task.objects.all()
    a = pagination(request, queryset, size_one_page=3, pages_show=3)
    page_string, queryset = a.html()
    form = TaskModelForm()
    return render(request,"task_list.html", {"form":form,
                                             "page_string":page_string,
                                             'queryset': queryset,})

@csrf_exempt
def task_add(request):
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))

    data_dict = {"status": False, 'error': form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))