import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="Service Status Search - 서비스 상태 검색 페이지",
    page_icon="🔍",
    layout="wide"
)

# 제목
st.title("Service Status Search ")
st.markdown("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
st.markdown("---")
# ✨ 상단 깃허브 아이콘 및 하단 푸터 숨기기 ✨
hide_streamlit_style = """
<style>
/* 1. 우측 상단 깃허브 아이콘, Fork, Stop 버튼 등이 있는 헤더 전체 숨김 */
header {visibility: hidden !important;}
[data-testid="stHeader"] {display: none !important;}
[data-testid="stToolbar"] {display: none !important;}

/* 2. 하단 푸터 숨김 */
footer {visibility: hidden !important;}

/* 3. 하단 뱃지 숨김 시도 (클라우드 환경에 따라 안 먹힐 수 있음) */
.viewerBadge_container__1QSob,
.viewerBadge_link__1S137,
.viewerBadge_text__1JaDK,
[class^="viewerBadge_"] {
    display: none !important;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# 서비스 목록
services = {
    "해외 주요 서비스": {
        "OpenAI & ChatGPT (오픈에이아이 & 챗지피티)": "https://status.openai.com/",
        "Cloudflare (클라우드플레어)": "https://www.cloudflarestatus.com/",
        "AWS (아마존 클라우드)": "https://health.aws.amazon.com/health/status",
        "Microsoft 365 (마이크로소프트 365)": "https://status.cloud.microsoft/m365/",
        "Microsoft Azure (마이크로소프트 애저)": "https://azure.status.microsoft/ko-kr/status",
        "Google Cloud Platform (구글 클라우드)": "https://status.cloud.google.com/",
        "Google Workspace (구글 워크스페이스)": "https://www.google.com/appsstatus/dashboard/",
        "Google Play (구글 플레이)": "https://status.play.google.com",
        "Apple US (애플 미국)": "https://www.apple.com/support/systemstatus/",
        "Apple KR (애플 한국)": "https://www.apple.com/kr/support/systemstatus/",
        "Meta (메타 / 페이스북 / 인스타그램)": "https://metastatus.com/",
        "Netflix (넷플릭스 미국)": "https://help.netflix.com/en/is-netflix-down",
        "Netflix (넷플릭스 한국)": "https://help.netflix.com/ko/is-netflix-down",
        "Spotify (스포티파이)": "https://spotify.statuspage.io",
        "Zoom (줌)": "https://status.zoom.us",
        "X & Twitter (엑스 & 트위터)": "https://x.com/X",
        "Starlink (스타링크 비공식)": "https://starlinkstatus.space/",
    },
    "국내 주요 서비스": {
        "Toss Payments (토스 페이먼츠)": "https://status.tosspayments.com/",
        "Naver Pay (네이버페이 공지사항)": "https://pay.naver.com/member/notice/",
        "KakaoPay (카카오페이 공지사항)": "https://www.kakaopay.com/news/notice",
        "Daum (다음 고객센터)": "https://cs.daum.net/",
        "Kakao API(카카오 API)": "https://developers.kakao.com/status",
        "Naver Cloud (네이버 클라우드)": "https://www.ncloud.com/support/notice",
        "Naver API (네이버 API)": "https://developers.naver.com/notice/apistatus/",
    },
    "주요 로밍 서비스": {
        "T-Mobile (미국)": "https://www.t-mobile.com/support/coverage/network-outages",
        "AT&T Mobility (미국)": "https://www.att.com/outages/",
        "Verizon Wireless (미국)": "https://www.verizon.com/support/check-network-status/",
        "SingTel Optus Pty Limited (호주)": "https://www.optus.com.au/living-network/service-status",
        "Orange (프랑스)": "https://suivi-des-incidents.orange.fr/infos-incident-local-internet-TV-telephone-fixe",
        "Maxis Broadband (말레이시아)": "https://www.maxis.com.my/en/about-maxis/maxis-network/mobile-network-checker/",
    },
}

# 검색 기능 추가
search_query = st.text_input("서비스 검색🔍 (모든 카테고리 검색)", placeholder="서비스 이름을 입력하세요.")

# 검색 필터링 함수
def filter_services(query):
    if not query:
        return services
    
    filtered = {}
    query_lower = query.lower()
    
    for group_name, group_services in services.items():
        filtered_group = {}
        for name, url in group_services.items():
            # 아이콘 제거한 이름으로 검색
            name_without_emoji = ''.join(c for c in name if not c.encode('utf-8').startswith(b'\xf0\x9f'))
            if query_lower in name_without_emoji.lower():
                filtered_group[name] = url
        
        if filtered_group:
            filtered[group_name] = filtered_group
    
    return filtered

# 필터링된 서비스 가져오기
filtered_services = filter_services(search_query)

# 검색 중일 때는 탭 없이 검색 결과만 표시
if search_query:
    total_count = sum(len(group) for group in filtered_services.values())
    st.info(f"검색 결과: {total_count}개의 서비스 (전체 카테고리 검색)")
    
    # 검색 결과가 있으면 카테고리 구분 없이 모두 표시
    if filtered_services:
        for group_name, group_services in filtered_services.items():
            st.subheader(f"{group_name}")
            
            # 4개의 열 생성
            col1, col2, col3, col4 = st.columns(4)
            
            # 서비스를 4개 열에 순환 배치
            for idx, (name, url) in enumerate(group_services.items()):
                if idx % 4 == 0:
                    with col1:
                        st.link_button(name, url, use_container_width=True)
                elif idx % 4 == 1:
                    with col2:
                        st.link_button(name, url, use_container_width=True)
                elif idx % 4 == 2:
                    with col3:
                        st.link_button(name, url, use_container_width=True)
                else:
                    with col4:
                        st.link_button(name, url, use_container_width=True)
            
            st.markdown("---")
    else:
        # 검색 결과가 없을 때
        st.warning("⚠️ 검색 결과가 없습니다. 다른 키워드로 검색해보세요.")

else:
    # 검색 안 할 때만 탭으로 표시
    tabs = st.tabs(["해외 주요 서비스", "국내 주요 서비스", "주요 로밍 서비스"])
    
    # 해외 주요 서비스 탭
    with tabs[0]:
        group_services = services["해외 주요 서비스"]
        
        # 4개의 열 생성
        col1, col2, col3, col4 = st.columns(4)
        
        # 서비스를 4개 열에 순환 배치
        for idx, (name, url) in enumerate(group_services.items()):
            if idx % 4 == 0:
                with col1:
                    st.link_button(name, url, use_container_width=True)
            elif idx % 4 == 1:
                with col2:
                    st.link_button(name, url, use_container_width=True)
            elif idx % 4 == 2:
                with col3:
                    st.link_button(name, url, use_container_width=True)
            else:
                with col4:
                    st.link_button(name, url, use_container_width=True)
    
    # 국내 주요 서비스 탭
    with tabs[1]:
        group_services = services["국내 주요 서비스"]
        
        # 4개의 열 생성
        col1, col2, col3, col4 = st.columns(4)
        
        # 서비스를 4개 열에 순환 배치
        for idx, (name, url) in enumerate(group_services.items()):
            if idx % 4 == 0:
                with col1:
                    st.link_button(name, url, use_container_width=True)
            elif idx % 4 == 1:
                with col2:
                    st.link_button(name, url, use_container_width=True)
            elif idx % 4 == 2:
                with col3:
                    st.link_button(name, url, use_container_width=True)
            else:
                with col4:
                    st.link_button(name, url, use_container_width=True)
    
    # 주요 로밍 서비스 탭
    with tabs[2]:
        group_services = services["주요 로밍 서비스"]
        
        # 4개의 열 생성
        col1, col2, col3, col4 = st.columns(4)
        
        # 서비스를 4개 열에 순환 배치
        for idx, (name, url) in enumerate(group_services.items()):
            if idx % 4 == 0:
                with col1:
                    st.link_button(name, url, use_container_width=True)
            elif idx % 4 == 1:
                with col2:
                    st.link_button(name, url, use_container_width=True)
            elif idx % 4 == 2:
                with col3:
                    st.link_button(name, url, use_container_width=True)
            else:
                with col4:
                    st.link_button(name, url, use_container_width=True)

st.markdown("---")
st.markdown("💡 각 버튼을 클릭하면 새 탭에서 상태 페이지가 열립니다.")
st.markdown("💡 업데이트 요청 : 윤성주")


