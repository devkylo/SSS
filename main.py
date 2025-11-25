import streamlit as st


# 페이지 설정
st.set_page_config(
    page_title="Status List - 주요 서비스 상태 페이지",
    page_icon="🔍",
    layout="wide"
)


# 제목
st.title("🔍 Status List")
st.markdown("주요 서비스의 상태 페이지를 확인하세요")
st.markdown("---")


# 서비스 목록 (아이콘 포함)
services = {
    "해외 주요 서비스": {
        "🤖 OpenAI (오픈에이아이)": "https://status.openai.com/",
        "🔍 Google (구글)": "https://www.google.com/appsstatus/dashboard/",
        "🍎 Apple KR (애플)": "https://www.apple.com/kr/support/systemstatus/",
        "🍎 Apple US (애플)": "https://www.apple.com/support/systemstatus/",
        "☁️ AWS (아마존 클라우드)": "https://health.aws.amazon.com/health/status",
        "💠 Microsoft Azure (애저)": "https://azure.status.microsoft/ko-kr/status",
        "📘 Meta (페이스북/인스타그램)": "https://metastatus.com/",
        "🌐 Cloudflare (클라우드플레어)": "https://www.cloudflarestatus.com/",
        "📺 Netflix (넷플릭스)": "https://help.netflix.com/ko/is-netflix-down",
    },
    "국내 주요 서비스": {
        "💬 Kakao (카카오 - 개발자용)": "https://developers.kakao.com/status",
        "💳 Toss Payments (토스 페이먼츠)": "https://status.tosspayments.com/",
        "☁️ Naver Cloud (네이버 클라우드)": "https://www.ncloud.com/support/notice",
    },
    "주요 로밍 서비스": {
        "📱 Verizon (미국)": "https://www.verizon.com/support/check-network-status/",
    },
}


# 검색 기능 추가
search_query = st.text_input("🔍 서비스 검색 (모든 카테고리 검색)", placeholder="서비스 이름을 입력하세요 (예: OpenAI, 구글, 카카오)")


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
    st.info(f"🔎 검색 결과: {total_count}개의 서비스 (전체 카테고리 검색)")
    
    # 검색 결과가 있으면 카테고리 구분 없이 모두 표시
    if filtered_services:
        for group_name, group_services in filtered_services.items():
            st.subheader(f"📡 {group_name}")
            
            # 3개의 열 생성
            col1, col2, col3 = st.columns(3)
            
            # 서비스를 3개 열에 순환 배치
            for idx, (name, url) in enumerate(group_services.items()):
                if idx % 3 == 0:
                    with col1:
                        st.link_button(name, url, use_container_width=True)
                elif idx % 3 == 1:
                    with col2:
                        st.link_button(name, url, use_container_width=True)
                else:
                    with col3:
                        st.link_button(name, url, use_container_width=True)
            
            st.markdown("---")
    else:
        # 검색 결과가 없을 때
        st.warning("⚠️ 검색 결과가 없습니다. 다른 키워드로 검색해보세요.")

else:
    # 검색 안 할 때만 탭으로 표시
    tabs = st.tabs(["🌏 해외 주요 서비스", "🇰🇷 국내 주요 서비스", "📱 주요 로밍 서비스"])
    
    # 해외 주요 서비스 탭
    with tabs[0]:
        group_services = services["해외 주요 서비스"]
        
        # 3개의 열 생성
        col1, col2, col3 = st.columns(3)
        
        # 서비스를 3개 열에 순환 배치
        for idx, (name, url) in enumerate(group_services.items()):
            if idx % 3 == 0:
                with col1:
                    st.link_button(name, url, use_container_width=True)
            elif idx % 3 == 1:
                with col2:
                    st.link_button(name, url, use_container_width=True)
            else:
                with col3:
                    st.link_button(name, url, use_container_width=True)
    
    # 국내 주요 서비스 탭
    with tabs[1]:
        group_services = services["국내 주요 서비스"]
        
        # 3개의 열 생성
        col1, col2, col3 = st.columns(3)
        
        # 서비스를 3개 열에 순환 배치
        for idx, (name, url) in enumerate(group_services.items()):
            if idx % 3 == 0:
                with col1:
                    st.link_button(name, url, use_container_width=True)
            elif idx % 3 == 1:
                with col2:
                    st.link_button(name, url, use_container_width=True)
            else:
                with col3:
                    st.link_button(name, url, use_container_width=True)
    
    # 주요 로밍 서비스 탭
    with tabs[2]:
        group_services = services["주요 로밍 서비스"]
        
        # 3개의 열 생성
        col1, col2, col3 = st.columns(3)
        
        # 서비스를 3개 열에 순환 배치
        for idx, (name, url) in enumerate(group_services.items()):
            if idx % 3 == 0:
                with col1:
                    st.link_button(name, url, use_container_width=True)
            elif idx % 3 == 1:
                with col2:
                    st.link_button(name, url, use_container_width=True)
            else:
                with col3:
                    st.link_button(name, url, use_container_width=True)


# 푸터
st.markdown("---")
st.markdown("💡 각 버튼을 클릭하면 새 탭에서 상태 페이지가 열립니다.")
