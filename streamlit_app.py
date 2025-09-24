"""Streamlit preview app for the ARBUSDT automated trading bot deck."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

import streamlit as st


st.set_page_config(
    page_title="ARBUSDT Bot Flow Preview",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)


CUSTOM_CSS = """
<style>
:root {
    color-scheme: light;
    --mint: #b5f5ec;
    --aqua: #0ea5e9;
    --deep-navy: #0f172a;
    --teal: #0f766e;
    --lavender: #a855f7;
}

body {
    background: radial-gradient(120% 120% at 50% 10%, rgba(186, 230, 253, 0.72) 0%, #fdf2ff 44%, #ffffff 100%);
    color: var(--deep-navy);
    font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
}

.main .block-container {
    padding-top: 2.4rem;
    padding-bottom: 2.8rem;
    max-width: 520px;
}

.mobile-frame {
    background: rgba(255, 255, 255, 0.94);
    border-radius: 36px;
    border: 2px solid rgba(14, 165, 233, 0.14);
    box-shadow: 0 32px 64px rgba(15, 118, 110, 0.18);
    padding: 2.8rem 2.4rem 2rem 2.4rem;
    min-height: 800px;
    display: flex;
    flex-direction: column;
    gap: 1.8rem;
    position: relative;
    overflow: hidden;
}

.mobile-frame::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(160deg, rgba(186, 230, 253, 0.25), rgba(224, 231, 255, 0.18));
    pointer-events: none;
}

.slide-content {
    position: relative;
    z-index: 1;
    animation: fadeIn 420ms ease-out;
}

.slide-title {
    font-size: 3.6rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: var(--deep-navy);
}

.slide-subtitle {
    font-size: 1.45rem;
    font-weight: 600;
    color: var(--teal);
}

.slide-body {
    font-size: 1.34rem;
    line-height: 1.58;
}

.slide-body ul {
    padding-left: 1.2rem;
    margin: 0;
}

.slide-body li {
    margin-bottom: 0.45rem;
}

.slide-body li::marker {
    color: var(--aqua);
}

.note-box {
    margin-top: auto;
    padding: 1.05rem 1.15rem;
    border-radius: 20px;
    background: linear-gradient(120deg, rgba(236, 254, 255, 0.9), rgba(224, 242, 254, 0.9));
    color: var(--teal);
    font-size: 1.05rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
    box-shadow: inset 0 0 0 1px rgba(14, 165, 233, 0.1);
}

.note-box span {
    font-weight: 700;
}

.footer-note {
    font-size: 0.95rem;
    text-align: center;
    color: rgba(15, 23, 42, 0.62);
    margin-top: 1.6rem;
}

.flow-grid {
    display: flex;
    flex-direction: column;
    gap: 0.95rem;
}

.flow-row {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.75rem;
}

.flow-item {
    font-weight: 700;
    padding: 0.6rem 0.95rem;
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    color: var(--deep-navy);
    position: relative;
    backdrop-filter: blur(6px);
}

.flow-item.hex {
    background: rgba(14, 165, 233, 0.18);
    clip-path: polygon(10% 0%, 90% 0%, 100% 50%, 90% 100%, 10% 100%, 0% 50%);
    min-width: 126px;
    justify-content: center;
}

.flow-item.guard {
    background: rgba(248, 113, 113, 0.22);
    border-radius: 999px;
    padding-inline: 1.1rem;
}

.flow-item.sync {
    background: rgba(14, 116, 144, 0.2);
    border-radius: 22px;
    padding-inline: 1.2rem;
}

.badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.36rem 0.78rem;
    border-radius: 999px;
    font-size: 0.98rem;
    font-weight: 700;
    margin-right: 0.42rem;
}

.badge.full {background: #0d9488; color: #fff; box-shadow: 0 6px 12px rgba(13, 148, 136, 0.25);}
.badge.selective {background: #fbbf24; color: #78350f; box-shadow: 0 6px 12px rgba(251, 191, 36, 0.3);}
.badge.fail {background: #d1d5db; color: #0f172a; box-shadow: inset 0 0 0 1px rgba(148, 163, 184, 0.4);}
.badge.block {background: #f87171; color: #fff; box-shadow: 0 6px 12px rgba(248, 113, 113, 0.35);}

.summary-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 1.05rem;
    overflow: hidden;
    border-radius: 20px;
    box-shadow: 0 16px 24px rgba(14, 165, 233, 0.12);
}

.summary-table thead {
    background: rgba(14, 165, 233, 0.16);
}

.summary-table th {
    color: var(--deep-navy);
}

.summary-table th, .summary-table td {
    border: 1px solid rgba(14, 116, 144, 0.12);
    padding: 0.7rem 0.65rem;
    text-align: center;
}

.state-machine {
    background: rgba(129, 140, 248, 0.16);
    padding: 1.2rem 1.1rem;
    border-radius: 20px;
    font-size: 1.12rem;
    line-height: 1.64;
}

.state-machine strong {
    color: var(--lavender);
}

.checklist {
    background: rgba(74, 222, 128, 0.18);
    padding: 1.15rem 1.2rem;
    border-radius: 20px;
    font-size: 1.12rem;
    line-height: 1.64;
    box-shadow: inset 0 0 0 1px rgba(22, 163, 74, 0.16);
}

.keyword-box {
    display: grid;
    gap: 0.65rem;
}

.keyword-box div {
    background: rgba(14, 165, 233, 0.18);
    border-radius: 16px;
    padding: 0.7rem 0.85rem;
    font-weight: 700;
    color: #0369a1;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

.keyword-box div::before {
    content: "✨";
}

.hero-title {
    font-size: 0.96rem;
    letter-spacing: 0.28em;
    color: rgba(15, 23, 42, 0.5);
    text-transform: uppercase;
    margin-bottom: 0.24rem;
}

.progress-label {
    display: flex;
    justify-content: center;
    gap: 0.7rem;
    font-size: 0.98rem;
    color: rgba(15, 23, 42, 0.7);
    margin-bottom: 0.75rem;
    font-weight: 600;
}

.progress-label span {
    font-weight: 800;
    color: var(--teal);
}

.progress-dot-wrapper {
    display: flex;
    justify-content: center;
    gap: 0.4rem;
    margin-bottom: 0.4rem;
}

.progress-dot {
    width: 10px;
    height: 10px;
    border-radius: 999px;
    background: rgba(14, 165, 233, 0.2);
    transition: all 0.2s ease;
}

.progress-dot.active {
    background: var(--aqua);
    width: 26px;
}

@keyframes fadeIn {
    0% {
        opacity: 0;
        transform: translateY(18px) scale(0.99);
    }
    100% {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}
</style>
"""


st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


@dataclass
class Slide:
    """Representation for a single deck slide."""

    title: str
    subtitle: str
    body_html: str
    note: str


slides: List[Slide] = [
    Slide(
        title="ARBUSDT 자동화 트레이딩 봇",
        subtitle="동작 원리 & 플로우",
        body_html="""
        <div class='keyword-box'>
            <div>게이트 기반 의사결정 + 브래킷 주문 영속 관리</div>
            <div>실시간 동기화·검증 가드로 체결 일관성 확보</div>
            <div>변동성 구간에서도 오버트레이드 억제</div>
        </div>
        """,
        note="연구 목적 전용 · 투자 조언 아님",
    ),
    Slide(
        title="Executive Summary",
        subtitle="한눈 요약",
        body_html="""
        <ul>
            <li>MEG→Regime→EV→Risk→Signal→Order 게이트 파이프라인</li>
            <li>브래킷 주문 상태 영속 관리로 부분·전량 체결 대응</li>
            <li>동기화·검증 레이어로 Funding 창·모드 불일치 가드</li>
        </ul>
        """,
        note="결과: 변동성 장에서도 오버트레이드 억제 & 체결 일관성 확보",
    ),
    Slide(
        title="Gate 파이프라인 요약",
        subtitle="Gate 0.5 ~ Gate 5",
        body_html="""
        <table class='summary-table'>
            <thead>
                <tr>
                    <th>Gate</th>
                    <th>목적</th>
                    <th>핵심 기준</th>
                    <th>통과 시</th>
                    <th>불통 시</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>0.5 MEG</td><td>이벤트 리스크 억제</td><td>block / soft / normal</td><td>다음 게이트</td><td>대기 / 축소</td></tr>
                <tr><td>1 Regime</td><td>시장 적합성</td><td>Full / Selective / Fail</td><td>2로 진행</td><td>중단</td></tr>
                <tr><td>2 EV</td><td>기대값</td><td>EV ≥ 하한</td><td>3로 진행</td><td>중단</td></tr>
                <tr><td>3 Risk</td><td>사이징·제약</td><td>위험액·라운딩·minNotional</td><td>4로</td><td>중단</td></tr>
                <tr><td>4 Signal</td><td>시그널 정합</td><td>진입·스톱·목표 생성</td><td>5로</td><td>중단</td></tr>
                <tr><td>5 Order</td><td>체결·발주</td><td>GTC / reduceOnly 등</td><td>포지션 오픈</td><td>오류 처리</td></tr>
            </tbody>
        </table>
        """,
        note="Gate 기준을 한 장에서 비교하고 팀 합의를 빠르게 진행",
    ),
    Slide(
        title="전체 동작 플로우",
        subtitle="입력 → 게이트 → 보조",
        body_html="""
        <div class='flow-grid'>
            <div class='flow-row'>
                <span class='flow-item sync'>⚙️ 입력: Market WS · Account WS · exchangeInfo · TimeSync</span>
            </div>
            <div class='flow-row'>
                <span class='flow-item hex'>Gate0.5 (MEG)</span>
                <span class='flow-item hex'>G1 Regime</span>
                <span class='flow-item guard'>🛡️ Funding Block Guard</span>
                <span class='flow-item hex'>G2 EV</span>
                <span class='flow-item hex'>G3 Risk</span>
                <span class='flow-item hex'>G4 Signal</span>
                <span class='flow-item hex'>G5 Order</span>
            </div>
            <div class='flow-row'>
                <span class='flow-item sync'>🔄 보조: BracketManager · Validator · Logger</span>
            </div>
        </div>
        """,
        note="도식: 게이트=육각형, 가드=원형, 동기화=기어 표현",
    ),
    Slide(
        title="Gate 0.5 · MacroEventGuard",
        subtitle="거시 이벤트 가드",
        body_html="""
        <ul>
            <li>모드: <span class='badge block'>block</span> / <span class='badge selective'>soft</span> / normal</li>
            <li>block: 신규 진입 차단 → 급격한 슬리피지 대비</li>
            <li>soft: EV 하한 가산 + 사이징 축소 + 유동성 페널티</li>
            <li>normal: 평시 기본 모드 유지</li>
        </ul>
        """,
        note="FOMC·CPI 등 고변동 이벤트 대응",
    ),
    Slide(
        title="Funding Block Guard",
        subtitle="펀딩 정산 창 회피",
        body_html="""
        <ul>
            <li>UTC 3개 창: 00:00-00:15 / 07:45-08:15 / 15:45-16:15</li>
            <li>창 내부: 신규 진입 보류, 종료 후 자동 해제</li>
            <li>TimeSync ±5초 이내 보정 필수</li>
        </ul>
        """,
        note="서버시간 오차 누적 시 가드 무력화",
    ),
    Slide(
        title="Gate 1 · RegimeEngine",
        subtitle="시장 레짐 판정",
        body_html="""
        <ul>
            <li>레짐: <span class='badge full'>Full</span> / <span class='badge selective'>Selective</span> / <span class='badge fail'>Fail</span></li>
            <li>Full: Altseason ≥ 75 & 상관계수 > 0.6</li>
            <li>Selective: 65~75 & 상관 > 0.6 → 사이징 50% + 헤지</li>
            <li>Fail: 기준 미충족 시 노-트레이드</li>
        </ul>
        """,
        note="지표 값은 운영 중 캘리브레이션",
    ),
    Slide(
        title="Gate 2 · EVEngine",
        subtitle="기대값 판단",
        body_html="""
        <ul>
            <li>EV = 체결확률 × 보상 − 비용(수수료·슬리피지·펀딩)</li>
            <li>기준: EV ≥ +0.02R, soft 모드면 하한 가산</li>
            <li>유동성 페널티로 기대수익 검증</li>
        </ul>
        """,
        note="사용자 확인 필요: EV 하한 값",
    ),
    Slide(
        title="Gate 3 · RiskEngine",
        subtitle="사이징 & 제약",
        body_html="""
        <ul>
            <li>기본 위험액 1.2% → 스톱거리 기반 수량 산정</li>
            <li>tick/step 라운딩 & minNotional 보정</li>
            <li>변동성 등급(저·중·고·크라이시스)별 사이징 조정</li>
        </ul>
        """,
        note="0-스톱거리(Entry = Stop)는 무효 처리",
    ),
    Slide(
        title="Gate 4~5",
        subtitle="SignalHub → OrderRouter",
        body_html="""
        <ul>
            <li>주문 세트: Entry LIMIT, SL STOP_MARKET, TP LIMIT reduceOnly</li>
            <li>포지션 모드에 따라 hedge / one-way 자동 정합</li>
            <li>타임스탬프·recvWindow·심볼 스펙 준수 전송</li>
        </ul>
        """,
        note="브래킷 주문 전송 지연 최소화",
    ),
    Slide(
        title="체결 이벤트 상태머신",
        subtitle="BracketManager",
        body_html="""
        <div class='state-machine'>
            <strong>NEW</strong> → (Entry fill) → <strong>OPEN</strong> → (TP partial) → <strong>PARTIAL</strong> → (TP fill all) → <strong>COMPLETED</strong> [SL 취소]<br><br>
            OPEN / PARTIAL → (SL hit) → <strong>COMPLETED</strong> [TP 전취소]<br>
            (어떤 상태든) 재시작 → <strong>RECONCILE</strong> → 상태 복원
        </div>
        """,
        note="부분 체결 시 SL을 잔여수량 reduceOnly로 교체",
    ),
    Slide(
        title="동기화·검증 레이어",
        subtitle="운영 안정성",
        body_html="""
        <ul>
            <li>TimeSync: 서버시간 수시 보정 (경고 임계 ±5s)</li>
            <li>exchangeInfo: tick/step/minNotional 실시간 갱신</li>
            <li>PositionMode Validator: 기대 모드와 불일치 시 선처리</li>
        </ul>
        """,
        note="동기화 실패 시 주문 중단 후 재평가",
    ),
    Slide(
        title="로깅·모니터링",
        subtitle="장애 대응",
        body_html="""
        <ul>
            <li>필수 로그: EV 경로, 사이징 근거, 주문 요청/응답</li>
            <li>장애 패턴: 네트워크 타임아웃, 모드 불일치, minNotional 미달</li>
            <li>대응: 재시도, 보류→재평가, MEG 모드 강등(soft→normal)</li>
        </ul>
        """,
        note="Funding 창 충돌 감지 시 메트릭 알림",
    ),
    Slide(
        title="운영 체크리스트",
        subtitle="Go-Live 전",
        body_html="""
        <div class='checklist'>
            TimeSync 오프셋 &lt; 5s / Funding 창 회피 ON / exchangeInfo 최신 / 라운딩 통과<br>
            EV 로그 유효 / 사이징 근거 기록 / 포지션 모드 일치
        </div>
        """,
        note="백테스트 → 페이퍼 → 소액 실험 3단계",
    ),
    Slide(
        title="사용자 확인 필요 변수",
        subtitle="배포 전 점검",
        body_html="""
        <ul>
            <li>Regime 기준: Altseason Index 75 / 65~75 경계, 상관계수 0.6</li>
            <li>EV 하한: +0.02R (예시값)</li>
            <li>1회 거래 위험액: 1.2% (예시값)</li>
            <li>Funding Block UTC 창: 00:00~00:15 / 07:45~08:15 / 15:45~16:15</li>
        </ul>
        """,
        note="운영 값 확정 시 노란 박스만 교체 후 재배포",
    ),
    Slide(
        title="면책·가드레일",
        subtitle="리스크 주의",
        body_html="""
        <ul>
            <li>연구 목적 전용 · 투자 조언 아님</li>
            <li>실거래 전 백테스트 → 페이퍼 → 소액 실험</li>
        </ul>
        """,
        note="운영 정책 변경 시 즉시 업데이트",
    ),
    Slide(
        title="한 줄 결론",
        subtitle="ARBUSDT Bot",
        body_html="""
        <div class='keyword-box'>
            <div>게이트 기반 결정 + 브래킷 영속 관리</div>
            <div>안 되는 장은 피하고 되는 장만 사이징</div>
            <div>기대값이 양(+)일 때만 집행</div>
        </div>
        """,
        note="Gate & Bracket으로 품질 제어",
    ),
]


slide_titles = [f"{idx + 1:02d}. {slide.title}" for idx, slide in enumerate(slides)]

if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0


def sync_sidebar(index: int) -> None:
    """Update sidebar radio selection to match the active slide."""

    st.session_state.slide_index = index
    st.session_state.sidebar_radio = slide_titles[index]


with st.sidebar:
    st.markdown("<div class='hero-title'>Slide Navigator</div>", unsafe_allow_html=True)
    selected_title = st.radio(
        "슬라이드를 선택하세요",
        slide_titles,
        index=st.session_state.slide_index,
        key="sidebar_radio",
    )
    sync_sidebar(slide_titles.index(selected_title))
    st.markdown(
        """
        **디자인 가이드**
        - 슬라이드당 3~5줄 키워드
        - 상태 컬러: Full(청록) · Selective(호박) · Fail(회색) · Block(적색)
        - 애니메이션: 나타내기→강조→사라지기 (핵심 2회 이내)
        """
    )


progress_value = (st.session_state.slide_index + 1) / len(slides)
st.markdown(
    f"<div class='progress-label'><span>{st.session_state.slide_index + 1:02d}</span>/"
    f"{len(slides):02d} Slides</div>",
    unsafe_allow_html=True,
)
dot_markup = "".join(
    f"<div class='progress-dot{' active' if idx == st.session_state.slide_index else ''}'></div>"
    for idx in range(len(slides))
)
st.markdown(
    f"<div class='progress-dot-wrapper'>{dot_markup}</div>",
    unsafe_allow_html=True,
)
st.progress(progress_value)

nav_left, nav_spacer, nav_right = st.columns([1.5, 3, 1.5])
with nav_left:
    if st.button("⬅️ 이전", use_container_width=True, disabled=st.session_state.slide_index == 0):
        sync_sidebar(st.session_state.slide_index - 1)
        st.experimental_rerun()
with nav_right:
    if st.button(
        "다음 ➡️",
        use_container_width=True,
        disabled=st.session_state.slide_index == len(slides) - 1,
    ):
        sync_sidebar(st.session_state.slide_index + 1)
        st.experimental_rerun()


current_slide = slides[st.session_state.slide_index]

st.markdown("<div class='mobile-frame'>", unsafe_allow_html=True)
st.markdown(
    f"""
    <div class='slide-content'>
        <div class='slide-title'>{current_slide.title}</div>
        <div class='slide-subtitle'>{current_slide.subtitle}</div>
        <div class='slide-body'>{current_slide.body_html}</div>
        <div class='note-box'>💡 <span>Speaker Note</span> {current_slide.note}</div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='footer-note'>모바일(1080×1920) 기준 미리보기 · Streamlit 프리뷰용</div>",
    unsafe_allow_html=True,
)
