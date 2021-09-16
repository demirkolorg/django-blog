from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class YazilarModel(models.Model):
    baslik=models.CharField(max_length=50,blank=False,null=False)
    icerik=RichTextField()
    olusturmaTarihi=models.DateTimeField(auto_now_add=True)
    duzenlemeTarihi=models.DateTimeField(auto_now=True)
    slug=AutoSlugField(populate_from='baslik',unique=True)
    kategoriler=models.ManyToManyField(KategoriModel,related_name='yazi')
    resim=models.ImageField(upload_to='yazi_resimleri')
    yazar=models.ForeignKey(User, on_delete=models.CASCADE, related_name='yazilar')

    class Meta:
        db_table='yazi'
        verbose_name_plural="Yazlar"
        verbose_name="Yazılar"
    
    def __str__(self):
        return self.baslik