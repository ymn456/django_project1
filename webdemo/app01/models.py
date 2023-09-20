from django.db import models

# Create your models here.

class Order(models.Model):
    """ 订单 """
    oid = models.CharField(verbose_name="订单号", max_length=64)
    title = models.CharField(verbose_name="名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")

    status_choices = (
        (1, "待支付"),
        (2, "已支付"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
    # admin_id
    admin = models.ForeignKey(verbose_name="管理员", to="admin", on_delete=models.CASCADE, null=True)

class task(models.Model):
    level_choice = (
        (1,"紧急"),
        (2,"重要"),
        (3,"临时")
    )
    level = models.SmallIntegerField(verbose_name="等级",choices=level_choice,default=1)
    detail = models.TextField(verbose_name="详情")
    title = models.CharField(verbose_name="标题", max_length=32)
    user = models.ForeignKey(verbose_name="负责人", to="admin", to_field="username", on_delete=models.CASCADE)

class admin(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32, unique=True)
    password = models.CharField(verbose_name="密码", max_length=32)

    def __str__(self):
        return self.username

class data_user(models.Model):
    name = models.CharField(verbose_name="名字",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄",default=2)
    account = models.DecimalField(verbose_name="余额",max_digits=10, decimal_places=2,default=0)
    create_time = models.DateTimeField(verbose_name="创建时间")
    depart = models.ForeignKey(verbose_name="部门",to="department", to_field="id", on_delete=models.CASCADE)
    gender_choices = (
        (1,"男"),
        (2,"女")
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)


class department(models.Model):
    title = models.CharField(max_length=16)

    def __str__(self):
        return self.title


class PrettyNum(models.Model):
    mobile = models.CharField(max_length=11, verbose_name="号码")
    price = models.IntegerField(verbose_name="价格", default=0)

    level_choice = (
        (1, "一级"),
        (2, "二级"),
        (3, "三级"),
        (4, "四级"),
    )

    level = models.SmallIntegerField(verbose_name="级别", choices=level_choice, default=1)

    status_choices = (
        (1, "已占用"),
        (2, "未使用")
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=2)