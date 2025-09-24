# ARBUSDT Trading Bot Slide Preview

이 저장소는 ARBUSDT 자동화 트레이딩 봇의 동작 원리와 플로우를 모바일 레이아웃 기반 슬라이드로 정리한 Streamlit 프리뷰 앱을 제공합니다.

## 로컬 실행

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

앱은 1080×1920 모바일 슬라이드 비율을 가정한 UI와 함께 각 슬라이드의 제목, 요지, 스피커 노트를 제공합니다. 사이드바에서 장표를 선택해 내용을 탐색할 수 있습니다.

## GitHub Actions

저장소에는 `python -m compileall streamlit_app.py` 검증을 자동으로 수행하는 GitHub Actions 워크플로(`.github/workflows/ci.yml`)가 포함되어 있습니다. 기본 Python 3.11 환경에서 `requirements.txt`에 정의된 의존성을 설치한 뒤 컴파일 검증을 수행하므로, 추가 종속성이 생기면 `requirements.txt`를 함께 업데이트해 주세요.
