import streamlit as st
from typing import List, Dict

st.set_page_config(
    page_title="ARBUSDT Bot Flow Preview",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

CUSTOM_CSS = """
<style>
body {
    background: linear-gradient(180deg, #f0fbff 0%, #fdf7ff 100%);
    color: #111827;
    font-family: 'Noto Sans KR', 'Pretendard', sans-serif;
}
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 480px;
}
.mobile-frame {
    background: rgba(255, 255, 255, 0.92);
    border-radius: 32px;
    box-shadow: 0 24px 48px rgba(15, 118, 110, 0.12);
    padding: 2.4rem 2rem 1.8rem 2rem;
    border: 2px solid rgba(14, 116, 144, 0.08);
    min-height: 760px;
    display: flex;
    flex-direction: column;
    gap: 1.6rem;
}
.slide-title {
    font-size: 2.4rem;
    font-weight: 800;
    line-height: 1.2;
    letter-spacing: -0.02em;
}
.slide-subtitle {
    font-size: 1.2rem;
    font-weight: 600;
    color: #0f766e;
}
.slide-body {
    font-size: 1.12rem;
    line-height: 1.6;
}
.slide-body ul {
    padding-left: 1.1rem;
    margin: 0;
}
.slide-body li {
    margin-bottom: 0.3rem;
}
.note-box {
    margin-top: auto;
    padding: 0.9rem 1rem;
    border-radius: 18px;
    background: #ecfeff;
    color: #036672;
    font-size: 0.92rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.35rem 0.75rem;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-right: 0.4rem;
}
.badge.full {background: #0d9488; color: white;}
.badge.selective {background: #fbbf24; color: #78350f;}
.badge.fail {background: #d1d5db; color: #111827;}
.badge.block {background: #f87171; color: #fff;}
.icon-hex {
    background: #cffafe;
    color: #0f766e;
    padding: 0.45rem 0.6rem;
    border-radius: 16px;
    font-weight: 700;
}
.table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.95rem;
}
.table th {
    background: rgba(14, 116, 144, 0.12);
    color: #0f172a;
}
.table th, .table td {
    border: 1px solid rgba(14, 116, 144, 0.12);
    padding: 0.55rem 0.6rem;
    text-align: center;
}
.arrow-flow {
    display: grid;
    gap: 0.6rem;
}
.arrow-flow span {
    background: rgba(14, 116, 144, 0.12);
    padding: 0.6rem 0.8rem;
    border-radius: 16px;
    text-align: center;
    font-weight: 600;
    font-size: 1.02rem;
}
.arrow-flow span .tag {
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    margin-left: 0.3rem;
    color: #0f766e;
}
.status-machine {
    background: rgba(129, 140, 248, 0.12);
    padding: 1rem;
    border-radius: 18px;
    font-size: 1rem;
    line-height: 1.6;
}
.highlight {
    color: #0ea5e9;
    font-weight: 600;
}
.footer-note {
    font-size: 0.85rem;
    text-align: center;
    color: rgba(15, 23, 42, 0.6);
    margin-top: 1.4rem;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

slides: List[Dict[str, str]] = [
    {
        "title": "ARBUSDT 자동화 트레이딩 봇",
        "subtitle": "동작 원리 & 플로우",
        "body": """
        • 게이트 기반 의사결정과 브래킷 주문 영속 관리<br>
        • 실시간 동기화·검증 가드로 체결 일관성 확보<br>
        • 변동성 구간에서도 오버트레이드 억제
        """,
        "note": "연구 목적 전용 · 투자 조언 아님",
    },
    {
        "title": "Executive Summary",
        "subtitle": "한눈 요약",
        "body": """
        • MEG→Regime→EV→Risk→Signal→Order 게이트 파이프라인<br>
        • 브래킷 주문 상태 영속 관리로 부분·전량 체결 대응<br>
        • 동기화·검증 레이어로 Funding 창·모드 불일치 가드
        """,
        "note": "결과: 변동성 장에서도 오버트레이드 억제 & 체결 일관성 확보",
    },
    {
        "title": "전체 동작 플로우",
        "subtitle": "입력부터 주문까지",
        "body": """
        <div class='arrow-flow'>
            <span>입력 ▶️ Market WS · Account WS · exchangeInfo · TimeSync</span>
            <span>Gate0.5 (MEG) → G1 Regime → Funding Block Guard → G2 EV</span>
            <span>G3 Risk → G4 Signal → G5 Order</span>
            <span>보조 ▶️ BracketManager · Validator · Logger</span>
        </div>
        """,
        "note": "도식: 게이트=육각형, 가드=원형, 동기화=기어로 시각화",
    },
    {
        "title": "Gate 0.5 · MacroEventGuard",
        "subtitle": "거시 이벤트 가드",
        "body": """
        • 모드: <span class='badge block'>block</span> / <span class='badge selective'>soft</span> / normal<br>
        • block: 신규 진입 차단 → 급격한 슬리피지 대비<br>
        • soft: EV 하한 가산 + 사이징 축소 + 유동성 페널티<br>
        • normal: 기본 모드, 평시 체계 유지
        """,
        "note": "FOMC·CPI 전후 급격 변동 대응",
    },
    {
        "title": "Funding Block Guard",
        "subtitle": "펀딩 정산 창 회피",
        "body": """
        • UTC 3개 창: 00:00-00:15 / 07:45-08:15 / 15:45-16:15<br>
        • 창 내부: 신규 진입 보류, 종료 후 자동 해제<br>
        • TimeSync ±5초 이내로 보정 필수
        """,
        "note": "서버시간 오차가 누적되면 가드 무력화",
    },
    {
        "title": "Gate 1 · RegimeEngine",
        "subtitle": "시장 레짐 판정",
        "body": """
        • 레짐: <span class='badge full'>Full</span> / <span class='badge selective'>Selective</span> / <span class='badge fail'>Fail</span><br>
        • Full ≥ Altseason 75 & 상관계수 0.6 초과<br>
        • Selective: 65~75 & 상관 0.6 → 사이징 50% + 헤지<br>
        • Fail: 기준 미충족 시 노-트레이드
        """,
        "note": "지표 값은 운영 중 캘리브레이션",
    },
    {
        "title": "Gate 2 · EVEngine",
        "subtitle": "기대값 계산",
        "body": """
        • EV = 체결확률×보상 − 비용(수수료·슬리피지·펀딩)<br>
        • 기준: EV ≥ +0.02R (soft 모드 시 하한 상향)<br>
        • 유동성 페널티 반영하여 기대수익 검증
        """,
        "note": "사용자 확인 필요: EV 하한 값",
    },
    {
        "title": "Gate 3 · RiskEngine",
        "subtitle": "사이징 & 제약",
        "body": """
        • 기본 위험액 1.2% → 스톱거리 기반 수량 산정<br>
        • tick/step 라운딩 & minNotional 보정<br>
        • 변동성 등급: 저/중/고/크라이시스 별 사이징 조정
        """,
        "note": "0-스톱거리(Entry=Stop)는 무효 처리",
    },
    {
        "title": "Gate 4-5",
        "subtitle": "SignalHub → OrderRouter",
        "body": """
        • 주문 세트: Entry LIMIT, SL STOP_MARKET, TP LIMIT reduceOnly<br>
        • 포지션 모드에 따라 hedge/one-way 자동 정합<br>
        • 타임스탬프·recvWindow·심볼 스펙 준수 전송
        """,
        "note": "브래킷 주문 전송 시 지연 최소화",
    },
    {
        "title": "체결 후 상태머신",
        "subtitle": "BracketManager",
        "body": """
        <div class='status-machine'>NEW → Entry fill → OPEN → TP partial → PARTIAL → TP fill all → COMPLETED (SL 취소)<br><br>
        OPEN/PARTIAL → SL hit → COMPLETED (TP 전취소)<br>
        모든 상태: 재시작 → RECONCILE → 상태 복원
        </div>
        """,
        "note": "부분 체결은 SL을 잔여수량 reduceOnly로 교체",
    },
    {
        "title": "동기화·검증 레이어",
        "subtitle": "운영 안정성",
        "body": """
        • TimeSync: 서버시간 수시 보정 (경고 ±5s)<br>
        • exchangeInfo: tick/step/minNotional 실시간 갱신<br>
        • PositionMode Validator: 모드 불일치 선처리
        """,
        "note": "동기화 실패 시 주문 중단 후 재평가",
    },
    {
        "title": "로깅·모니터링",
        "subtitle": "장애 대응",
        "body": """
        • 필수 로그: EV 경로, 사이징 근거, 주문 요청/응답<br>
        • 장애 패턴: 네트워크 타임아웃, 모드 불일치, minNotional 미달<br>
        • 대응: 재시도, 보류→재평가, MEG 모드 강등 롤백
        """,
        "note": "Funding 창 충돌 감지 후 메트릭 알림",
    },
    {
        "title": "운영 체크리스트",
        "subtitle": "Go-Live 전 필수",
        "body": """
        <ul>
            <li>TimeSync 오프셋 < 5s, Funding 창 회피 ON</li>
            <li>exchangeInfo 최신, 라운딩 통과</li>
            <li>EV 하한·위험액·변동성 등급 확정값 테스트</li>
        </ul>
        """,
        "note": "백테스트→페이퍼→소액 실험 3단계",
    },
    {
        "title": "면책·가드레일",
        "subtitle": "리스크 주의",
        "body": """
        • 연구 목적 전용 · 투자 조언 아님<br>
        • 실거래 전 백테스트 → 페이퍼 → 소액 실험
        """,
        "note": "운영 값 확정 시 노란 박스만 교체",
    },
    {
        "title": "한 줄 결론",
        "subtitle": "ARBUSDT Bot",
        "body": """
        • 게이트 기반 결정 + 브래킷 영속 관리로<br>
        • 안 되는 장은 피하고 되는 장만 사이징<br>
        • 기대값이 양(+)일 때만 집행
        """,
        "note": "Gate & Bracket으로 품질 제어",
    },
]

slide_titles = [f"{idx+1:02d}. {slide['title']}" for idx, slide in enumerate(slides)]

with st.sidebar:
    st.header("슬라이드 네비게이터")
    selected = st.radio("슬라이드를 선택하세요", slide_titles, index=0)
    st.markdown("""
    **디자인 가이드**
    - 슬라이드당 3~5줄 키워드
    - 상태 컬러: Full(청록) · Selective(호박) · Fail(회색) · Block(적색)
    - 애니메이션: 나타내기→강조→사라지기 (핵심 2회 이내)
    """)

current_index = slide_titles.index(selected)
current_slide = slides[current_index]

st.markdown("<div class='mobile-frame'>", unsafe_allow_html=True)
st.markdown(
    f"""
    <div class='slide-title'>{current_slide['title']}</div>
    <div class='slide-subtitle'>{current_slide['subtitle']}</div>
    <div class='slide-body'>{current_slide['body']}</div>
    <div class='note-box'>💡 {current_slide['note']}</div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='footer-note'>모바일(1080×1920) 기준 미리보기 · Streamlit 프리뷰용</div>",
    unsafe_allow_html=True,
)
