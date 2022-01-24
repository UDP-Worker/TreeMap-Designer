from django.db import models

# Create your models here.

class InfoField(models.Model):
    """信息将分类存储，这个类用以存储每一类信息的类的信息"""
    field_name = models.CharField(max_length= 200)#信息的类名
    date_added = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.field_name
