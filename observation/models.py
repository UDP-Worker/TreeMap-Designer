from django.db import models

# Create your models here.

class InfoField(models.Model):
    """信息将分类存储，这个类用以存储每一类信息的类的信息"""
    field_name = models.CharField(max_length= 200)#信息的类名
    date_added = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.field_name

class InfoLine(models.Model):
    """储存每一条具体的信息"""
    field = models.ForeignKey(InfoField,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    #关于信息的重要性
    EMERGENCY = 'EM'
    CONCERN = 'CO'
    CRUCIAL = 'CR'
    PLAIN = 'PL'
    MEANINGLESS = 'ME'
    importance_choice = (
        (EMERGENCY, '紧急'),
        (CONCERN, '值得关注'),
        (CRUCIAL, '相对重要'),
        (PLAIN, '普通'),
        (MEANINGLESS,'毫无意义'),
    )
    importance = models.CharField(
        max_length=2,
        choices=importance_choice,
        default=PLAIN,
    )

    class Meta:
        """重写类以使Django使用Infolines而非Infoline来表示多个条目"""
        verbose_name_plural = 'Infolines'

    def __str__(self):
        return self.get_importance_display() + ' : ' + self.text[:50] + '…'
