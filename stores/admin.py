from django.contrib import admin
from .models import DaisoStore, NearbyStore

# 다이소 지점 관리자 화면 설정
@admin.register(DaisoStore)
class DaisoStoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'daiso_id') # 목록에 보여줄 항목
    search_fields = ('name', 'address') # 검색 기능 추가

#  이 부분이 있어야 화면에 나옵니다!
@admin.register(NearbyStore)
class NearbyStoreAdmin(admin.ModelAdmin):
    # 목록에 보여줄 항목들 (상호, 전화번호, 거리(km), 주소, 기준지점)
    list_display = ('name', 'phone', 'distance_km', 'address', 'base_daiso')
    
    # 검색창 추가 (상호명으로 검색 가능)
    search_fields = ('name',)

    # 거리(m)를 km 단위로 변환해서 보여주는 함수
    def distance_km(self, obj):
        if obj.distance:
            return f"{obj.distance / 1000:.2f} km"
        return "0 km"
    distance_km.short_description = '거리 (km)'