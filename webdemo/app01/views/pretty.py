from django.shortcuts import render, redirect

from app01 import models
from app01.utils.form import PrettyModelForm
from app01.utils.pagination import pagination


def pretty_list(request):
    # 搜索
    search_data = request.GET.get("q", "")
    dict_data = {}
    dict_data["mobile__contains"] = search_data

    queryset = models.PrettyNum.objects.filter(**dict_data).all()


    # 分页
    a = pagination(request,queryset,size_one_page=3, pages_show=3)
    page_string, queryset = a.html()

    return render(request, 'pretty_list.html', {'queryset': queryset,
                                                "search_data":search_data,
                                                "page_string":page_string})


def pretty_add(request):
    if request.method == "GET":
        form = PrettyModelForm()
        return render(request, "pretty_add.html", {"form":form})

    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")
    return render(request, "pretty_add.html", {"form":form})

def pretty_edit(request,nid):
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == "GET":
        form = PrettyModelForm(instance=row_object)
        return render(request, "pretty_edit.html", {"form": form})

    form = PrettyModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")
    return render(request, "pretty_edit.html", {"form": form})


def pretty_delete(request,nid):
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect("/pretty/list")
