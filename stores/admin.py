from django.contrib import admin
from .models import NearbyStore

# 👇 이 부분이 있어야 화면에 나옵니다!
@admin.register(NearbyStore)
class NearbyStoreAdmin(admin.ModelAdmin):
    # 목록에 보여줄 항목들 (상호, 거리, 주소, 기준지점)
    list_display = ('name', 'distance', 'address', 'base_daiso')
    
    # 검색창 추가 (상호명으로 검색 가능)
    search_fields = ('name',)