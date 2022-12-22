from django.db import models
from datetime import datetime
# Create your models here.
class SimFiles(models.Model):
    #主键id可以省略不写
    filename=models.CharField(max_length=100, verbose_name="文件名")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name='上传时间')

    class Meta:
        db_table="file"
