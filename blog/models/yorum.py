from django.db import models
from django.contrib.auth.models import User
from blog.models import YazilarModel
from blog.models.abstract_model import DateAbstractModel

class YorumModel(DateAbstractModel):
    yazan=models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yorum')
    yazi=models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yorumlar')
    icerik=models.TextField()

    class Meta:
        db_table='yorum'
        verbose_name_plural="Yorumlar"
        verbose_name="Yorum"
    
    def __str__(self):
        return self.yazan.username