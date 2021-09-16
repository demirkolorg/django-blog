from django.contrib import admin
from blog.models import KategoriModel, YazilarModel

admin.site.register(KategoriModel)


class YazilarAdmin(admin.ModelAdmin):
    list_display=('baslik','olusturmaTarihi','duzenlemeTarihi','yazar')
    search_fields=('baslik','icerik')
admin.site.register(YazilarModel,YazilarAdmin)
