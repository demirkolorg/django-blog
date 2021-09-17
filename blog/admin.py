from django.contrib import admin
from blog.models import KategoriModel, YazilarModel, YorumModel, IletisimModel




@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    list_display=('baslik','olusturmaTarihi','duzenlemeTarihi','yazar')
    search_fields=('baslik','icerik')


@admin.register(YorumModel)
class YorumlarAdmin(admin.ModelAdmin):
    list_display=('yazi','yazan','olusturmaTarihi','duzenlemeTarihi')
    search_fields=('yazan__username','yazi__icerik')


@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    list_display=('email','olusturmaTarihi')
    search_fields=('email','mesaj')

admin.site.register(KategoriModel)
