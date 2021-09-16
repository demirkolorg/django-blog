from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField

class IletisimModel(models.Model):
    email=models.EmailField(max_length=250,blank=False,null=False)
    isim_soyisim=models.CharField(max_length=150)
    mesaj=models.TextField()    
    olusturmaTarihi=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='iletisim'
        verbose_name_plural="İletisimler"
        verbose_name="İletisim"
    
    def __str__(self):
        return self.email