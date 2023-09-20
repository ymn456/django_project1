from django.shortcuts import render, redirect
from app01 import models


def depart_list(request):
    queryset = models.department.objects.all()
    return render(request, 'depart_list.html', {'queryset': queryset})
def depart_add(request):
    if request.method == 'GET':
        return render(request, 'depart_add.html')

    title = request.POST.get('title')
    models.department.objects.create(title=title)
    return redirect('/depart/list/')

def depart_delete(request):
    nid = request.GET.get('nid')
    models.department.objects.filter(id=nid).delete()
    return redirect('/depart/list/')

def depart_edit(request,nid):
    if request.method == 'GET':
        row_title = models.department.objects.filter(id=nid).first()
        return render(request,"depart_edit.html",{'row_title':row_title})

    title = request.POST.get('title')
    models.department.objects.filter(id=nid).update(title=title)
    return redirect('/depart/list/')