from django.db import models

class DateAbstractModel(models.Model):
    olusturmaTarihi=models.DateTimeField(auto_now_add=True)
    duzenlemeTarihi=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True