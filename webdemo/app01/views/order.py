from datetime import datetime
import random

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.utils.pagination import pagination
from app01.utils.Bootstrap import BootstrapModelForm

class OrderModelForm(BootstrapModelForm):
    class Meta:
        model = models.Order
        # fields = "__all__"
        # fields = [""]
        exclude = ["oid", 'admin']

def order_list(request):
    queryset = models.Order.objects.all().order_by('-id')
    page_string, queryset= pagination(request, queryset).html()
    form = OrderModelForm()

    context = {
        'form': form,
        "queryset": queryset,  # 分完页的数据
        "page_string": page_string  # 生成页码
    }

    return render(request, 'order_list.html', context)

@csrf_exempt
def order_add(request):
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))

        # 固定设置管理员ID，去哪里获取？
        form.instance.admin_id = request.session["info"]["id"]
        return JsonResponse({"status": True})
    return JsonResponse({'status':False, 'error':form.errors})


def order_delete(request):
    uid = request.GET.get('uid')
    flag = models.Order.objects.filter(id=uid).exists()
    if flag:
        models.Order.objects.filter(id=uid).delete()
        return JsonResponse({'status':True})
    else:
        return JsonResponse({'status':False, 'error':"数据不存在"})

@csrf_exempt
def order_edit(request):
    form = OrderModelForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': True})
    else:
        return JsonResponse({'status': False, 'error': '数据不存在'})


@csrf_exempt
def order_detail(request):
    uid = request.GET.get('uid')
    obj = models.Order.objects.filter(id=uid).values('title','price','status').first()
    if obj:
        return JsonResponse({'status':True, 'data':obj})
    else:
        return JsonResponse({'status': False, 'error': '数据不存在'})
