# 🏪 다이소 상권 분석 프로젝트 (Daiso Research)

이 프로젝트는 **중소기업벤처부 리서치**를 위해 개발된 Django 기반 데이터 수집 서비스입니다.
카카오맵 API를 활용하여 다이소 지점 주변(반경 1km~5km)의 경쟁 매장(카페, 편의점 등) 데이터를 수집하고 분석합니다.

---

## 1. 개발 환경 (Tech Stack)

* **Language:** Python 3.10+
* **Framework:** Django
* **API:** Kakao Maps REST API
* **Data Processing:** Pandas, OpenPyXL

---

### 환경 설정
```bash
# 1. 저장소 클론
git clone [Repository URL]

# 2. 가상환경 생성 및 패키지 설치
python -m venv venv
source venv/Scripts/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. 환경 변수 설정 (.env 파일 생성)
# KAKAO_API_KEY=your_kakao_rest_api_key
```

### 데이터 수집 실행
```bash
# 마이그레이션 (DB 초기화)
python manage.py migrate
# 수집 커맨드 실행
python manage.py collect_cafes
```