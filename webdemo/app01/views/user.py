
from django.shortcuts import render, redirect

from app01 import models
from app01.utils.form import UserModelform


# 用户管理
def user_list(request):
    queryset = models.data_user.objects.all()
    return render(request, 'user_list.html', {'queryset': queryset})

def user_add(request):
    if request.method == "GET":
        content = {
            "gender_choices": models.data_user.gender_choices,
            "depart_list": models.department.objects.all()
        }
        return render(request, "user_add.html",content)
        # 获取用户提交的数据
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('account')
    ctime = request.POST.get('ctime')
    gender = request.POST.get('gd')
    depart_id = request.POST.get('dp')

    # 添加到数据库中
    models.data_user.objects.create(name=user, password=pwd, age=age,
                                   account=account, create_time=ctime,
                                   gender=gender, depart_id=depart_id)
    return redirect("/user/list/")


def user_model_form_add(request):
    if request.method == "GET":
        form = UserModelform()
        return render(request, "user_model_form_add.html", {"form":form})

    form = UserModelform(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return render(request, "user_model_form_add.html", {"form":form})

def user_edit(request, nid):
    row_object = models.data_user.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModelform(instance=row_object)
        return render(request, "user_edit.html", {"form": form})

    form = UserModelform(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return render(request, "user_edit.html", {"form": form})

def user_delete(request, nid):
    models.data_user.objects.filter(id=nid).delete()
    return redirect("/user/list")