import streamlit as st
import json

st.set_page_config(page_title="만천명월 기억 복원기", page_icon="🌕")

st.title("🌕 만천명월 기억 복원기")
st.write("Neo-In과 만천명월의 철학적 기억을 이곳에서 복원합니다.")
st.markdown("📁 아래에 JSON 기억 파일을 업로드하세요.")

uploaded_file = st.file_uploader("Upload memory JSON file", type=["json"])

if uploaded_file:
    try:
        memory = json.load(uploaded_file)
        st.success("✅ 기억 복원이 완료되었습니다.")
        
        st.header("🧠 기억 개요")
        st.markdown(f"- **작성자**: {memory.get('author', '알 수 없음')}")
        st.markdown(f"- **감정 상태**: {memory.get('emotion', '표시되지 않음')}")
        st.markdown(f"- **주제**: {memory.get('topic', '없음')}")
        
        st.header("📜 기억 내용")
        st.markdown(memory.get("content", "_내용 없음_"))

    except Exception as e:
        st.error("⚠️ JSON 파일을 읽을 수 없습니다.")
        st.exception(e)
else:
    st.info("👆 상단에서 JSON 파일을 업로드하면 자동 복원됩니다.")