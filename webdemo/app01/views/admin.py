from django.shortcuts import render, redirect

from app01 import models
from app01.utils.form import AdminModelForm, AdminEditModelForm, AdminResetModelForm
from app01.utils.pagination import pagination


def admin_list(request):
    # 搜索
    search_data = request.GET.get("q", "")
    dict_data = {}
    dict_data["username__contains"] = search_data

    queryset = models.admin.objects.filter(**dict_data).all()

    # 分页
    a = pagination(request,queryset,size_one_page=3, pages_show=3)
    page_string, queryset = a.html()

    return render(request, 'admin_list.html', {'queryset': queryset,
                                               'search_data':search_data,
                                                "page_string":page_string})


def admin_add(request):
    title = "新建管理员"
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, "change.html", {"form":form,"title":title})

    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")
    return render(request, "change.html", {"form":form, "title":title})

def admin_reset(request, nid):
    title = "重置密码"
    row_object = models.admin.objects.filter(id=nid).first()
    if request.method == "GET":
        form = AdminResetModelForm(instance=row_object)
        return render(request, "change.html", {"form": form, "title": title})

    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")
    return render(request, "change.html", {"form": form, "title": title})

def admin_edit(request,nid):
    title = "编辑管理员"
    row_object = models.admin.objects.filter(id=nid).first()
    if request.method == "GET":
        form = AdminEditModelForm(instance=row_object)
        return render(request, "change.html", {"form": form, "title":title})

    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")
    return render(request, "change.html", {"form": form, "title":title})


def admin_delete(request,nid):
    models.admin.objects.filter(id=nid).delete()
    return redirect("/admin/list")
