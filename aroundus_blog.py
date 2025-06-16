import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Font hỗ trợ tiếng Hàn
matplotlib.rc('font', family='NanumGothic')

# Cấu hình page
st.set_page_config(page_title="Around Us & Highlight 블로그", layout="wide")

# Thêm font đẹp cho toàn bộ app
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Nanum Gothic', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Giới thiệu công ty
st.title("🏢 회사 소개 - Around Us 엔터테인먼트")
st.write("""
Around Us Entertainment는 2016년에 설립된 대한민국의 연예 기획사로,
그룹 **하이라이트(Highlight)**가 전속 계약을 종료한 후 
직접 설립하여 독립 활동을 시작한 회사입니다.

회사명은 \"우리 주변의 모든 이들과 함께 하고 싶다\"는 의미를 담고 있습니다.
현재는 하이라이트를 중심으로 다양한 아티스트 활동과 콘텐츠 제작을 진행하고 있습니다.
""")
# 📸 Logo công ty
st.image("https://i.pinimg.com/736x/3c/97/b1/3c97b12d4966bbe60977bd46f4187a3e.jpg",
         caption="Around Us Entertainment 로고", use_container_width=True)

# 2. Giới thiệu nhóm Highlight
st.header("🎤 대표 아티스트 - Highlight 소개")
st.write("""
하이라이트는 2009년 **비스트(BEAST)**로 데뷔한 보이그룹으로,
2017년부터는 독립하여 **하이라이트(Highlight)**라는 이름으로 활동 중입니다.

감성적인 음악, 뛰어난 무대 퍼포먼스,
그리고 팬들과의 진심 어린 소통으로 꾸준한 사랑을 받고 있습니다.
""")

# Chèn ảnh nhóm
st.image("https://i.pinimg.com/736x/0e/80/81/0e80819a596730175cfdd380db481574.jpg",
         caption="하이라이트 (Highlight) - Marie Claire Korea",
         use_container_width=True)

# 3. Thành viên
st.subheader("👥 멤버를 선택하세요 👇")
members = {
    "윤두준": {
        "position": "리더, 래퍼, 보컬",
        "birth": "1989년 7월 4일",
        "mbti": "ISTJ",
        "image": "https://i.pinimg.com/736x/49/8f/40/498f40cc3ed7b2d7f0b626b69e767401.jpg"
    },
    "양요섭": {
        "position": "메인보컬",
        "birth": "1990년 1월 5일",
        "mbti": "ISFJ",
        "image": "https://i.pinimg.com/736x/fe/aa/c2/feaac283af78039a3b1ca62555b3c345.jpg"
    },
    "이기광": {
        "position": "보컬, 퍼포먼스",
        "birth": "1990년 3월 30일",
        "mbti": "ENFP",
        "image": "https://i.pinimg.com/736x/d5/eb/6a/d5eb6a5030fdcd0fd505d10b373ee283.jpg"
    },
    "손동운": {
        "position": "막내, 보컬",
        "birth": "1991년 6월 6일",
        "mbti": "INFP",
        "image": "https://i.pinimg.com/736x/11/fc/14/11fc1486401c33bac9e73a35738ba6fa.jpg"
    },
}

selected_member = st.selectbox("멤버를 선택하세요", list(members.keys()))
m = members[selected_member]

# Căn giữa thông tin thành viên
st.markdown(f"""
<div style="text-align: center;">
  <h1 style="font-size: 40px; margin-bottom: 20px;">{selected_member}</h1>
  <img src="{m['image']}" width="400" style="margin-bottom: 20px;"><br>
  <p style="font-size: 24px;"><strong>💫 포지션:</strong> {m['position']}</p>
  <p style="font-size: 24px;"><strong>🎂 생년월일:</strong> {m['birth']}</p>
  <p style="font-size: 24px;"><strong>🧠 MBTI:</strong> {m['mbti']}</p>
</div>
""", unsafe_allow_html=True)
# 4. Bài hát & MV
st.header("🎵 대표곡 & 뮤직비디오")
songs = {
    "On Rainy Days (2011)": {
        "desc": "감성을 자극하는 이별 발라드.",
        "video": "https://www.youtube.com/watch?v=NY47mqz4yCg&ab_channel=BEAST-Topic"
    },
    "Fiction (2011)": {
        "desc": "비스트 시절의 대표곡.",
        "video": "https://www.youtube.com/watch?v=ZAzWT8mRoR0&ab_channel=BEAST%EB%B9%84%EC%8A%A4%ED%8A%B8%28OfficialYouTubeChannel%29"
    },
    "Plz Don't Be Sad (2017)": {
        "desc": "하이라이트로서 첫 컴백곡.",
        "video": "https://www.youtube.com/watch?v=1kcwvcbO8MI&ab_channel=1theK%28%EC%9B%90%EB%8D%94%EC%BC%80%EC%9D%B4%29"
    },
    "Not The End (2021)": {
        "desc": "전역 후 첫 완전체 활동곡.",
        "video": "https://www.youtube.com/watch?v=QlvCkxsmwoc&ab_channel=OFFICIALHIGHLIGHT"
    },
    "Endless Ending (2024)": {
        "desc": "감성을 담은 부드럽고 따뜻한 발라드 곡입니다.",
        "video": "https://www.youtube.com/watch?v=RTTVWPXcd8A&ab_channel=CHKCHK%28%EC%B4%89%EC%B4%89%29"
    },
    "Chains (2024)": {
        "desc": "가장 최근 발표된 곡으로 성숙한 매력을 담은 곡.",
        "video": "https://www.youtube.com/watch?v=3kfhoikVzUc&ab_channel=OFFICIALHIGHLIGHT"
    }
}

selected_song = st.selectbox("🎶 가장 좋아하는 곡을 골라보세요", list(songs.keys()))
st.success(f"🎧 당신이 선택한 곡: {selected_song}")
st.write(f"📝 설명: {songs[selected_song]['desc']}")
st.video(songs[selected_song]['video'])

# 5. Biểu đồ album
import matplotlib.pyplot as plt

sales_data = pd.DataFrame({
    "Year": [2011, 2017, 2021, 2024],
    "Album Sales (K)": [165, 115, 95, 110]
})

fig, ax = plt.subplots()
ax.bar(sales_data["Year"], sales_data["Album Sales (K)"])

for i in range(len(sales_data)):
    ax.text(sales_data["Year"][i], sales_data["Album Sales (K)"][i] + 2,
            f"{sales_data['Album Sales (K)'][i]}K", ha='center')

ax.set_xlabel("Year")
ax.set_ylabel("Album Sales (K)")
ax.set_title("Highlight Album Sales by Year")

st.pyplot(fig)

# 6. Kết luận
st.header("💬 마무리 한마디")
st.write("""
저는 콘텐츠와 음악 산업에 큰 관심이 있으며,
**Around Us**처럼 아티스트 중심의 회사를 통해
팬과 아티스트가 함께 성장하는 구조가 인상 깊습니다.

앞으로도 이러한 회사에서 일하며,
좋은 콘텐츠를 만드는 사람이 되고 싶습니다 💙
""")
