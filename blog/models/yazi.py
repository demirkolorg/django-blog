from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from blog.models.abstract_model import DateAbstractModel

class YazilarModel(DateAbstractModel):
    baslik=models.CharField(max_length=50,blank=False,null=False)
    icerik=RichTextField()
    slug=AutoSlugField(populate_from='baslik',unique=True)
    kategoriler=models.ManyToManyField(KategoriModel,related_name='yazi')
    resim=models.ImageField(upload_to='yazi_resimleri')
    yazar=models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yazilar')

    class Meta:
        db_table='yazi'
        verbose_name_plural="Yazılar"
        verbose_name="Yazı"
    
    def __str__(self):
        return self.baslik