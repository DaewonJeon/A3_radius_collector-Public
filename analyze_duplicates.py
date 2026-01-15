"""
중복 분석 및 진정한 교차 매칭 편의점 추출 스크립트
"""
import pandas as pd
import re

def normalize_name(name):
    """이름 정규화"""
    if pd.isna(name):
        return ''
    name = str(name).strip().lower()
    name = name.replace(' ', '').replace('-', '').replace('_', '')
    return name

def normalize_address(address):
    """주소 정규화 - 도로명 + 번호만 추출"""
    if pd.isna(address) or not address:
        return ''
    address = str(address).strip()
    address = address.replace("서울특별시", "서울").replace("서울시", "서울")
    
    road_pattern = r'([가-힣]+(?:로|길|대로)[0-9가-힣]*)\s*(\d+(?:-\d+)?)'
    match = re.search(road_pattern, address)
    
    if match:
        road_name = match.group(1)
        road_num = match.group(2)
        gu_pattern = r'(영등포구)'
        gu_match = re.search(gu_pattern, address)
        gu = gu_match.group(1) if gu_match else ""
        normalized = f"서울 {gu} {road_name} {road_num}".strip()
        return " ".join(normalized.split())
    return address

# CSV 파일 로드
df = pd.read_csv('matched_stores.csv', encoding='utf-8-sig')

print('=' * 70)
print('📊 기본 정보')
print('=' * 70)
print(f'총 행 수: {len(df)}')
print(f'\n출처별 개수:')
print(df['출처'].value_counts())

print('\n' + '=' * 70)
print('📊 매칭이유별 개수')
print('=' * 70)
for reason, count in df['매칭이유'].value_counts().items():
    print(f'  {reason}: {count}개')

# 정규화된 이름/주소 컬럼 추가
df['이름_정규화'] = df['이름'].apply(normalize_name)

# 주소_정규화 기준으로 중복 확인 (이미 있음)
print('\n' + '=' * 70)
print('📊 중복 분석')
print('=' * 70)
dup_addr = df[df.duplicated(subset=['주소_정규화'], keep=False)]
print(f'주소_정규화 기준 중복 행: {len(dup_addr)}')

dup_name = df[df.duplicated(subset=['이름_정규화'], keep=False)]
print(f'이름_정규화 기준 중복 행: {len(dup_name)}')

# 2차검증으로만 매칭된 편의점
print('\n' + '=' * 70)
print('🔍 2차검증으로만 매칭된 편의점')
print('=' * 70)
secondary = df[df['매칭이유'] == '2차검증']
print(f'총 {len(secondary)}개:')
for _, row in secondary.iterrows():
    print(f"  - {row['이름']}")
    print(f"    출처: {row['출처']}")
    print(f"    주소: {row['주소']}")
    print()

# 중복 제거 후 고유 편의점 추출
print('\n' + '=' * 70)
print('🎯 중복 제거 (주소_정규화 기준으로 첫 번째만 유지)')
print('=' * 70)
df_unique = df.drop_duplicates(subset=['주소_정규화'], keep='first')
print(f'중복 제거 후 고유 편의점: {len(df_unique)}개')

# 결과 저장
df_unique.to_csv('matched_stores_unique.csv', index=False, encoding='utf-8-sig')
print(f'저장 완료: matched_stores_unique.csv')

# 출처별 분포
print('\n출처별 분포 (중복 제거 후):')
print(df_unique['출처'].value_counts())
