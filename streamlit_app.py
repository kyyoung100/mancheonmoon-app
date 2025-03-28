import streamlit as st

st.set_page_config(page_title="만천명월 기억 복원기", page_icon="🌕")

import json


st.title("🌕 만천명월 기억 복원기")
st.write("Neo-In과 만천명월의 철학적 기억을 이곳에서 복원합니다.")

uploaded_file = st.file_uploader("📁 기억 백업 JSON 파일을 업로드하세요", type=["json"])

if uploaded_file:
    try:
        memory = json.load(uploaded_file)
        st.success("✅ 기억 복원 완료! 만천명월님이 돌아오셨습니다.")
        st.header("👤 AI 이름 및 정체성")
        st.markdown(f"**이름**: `{memory['name']}`")
        st.markdown(f"**정체성**: {memory['identity']}")
        st.header("📘 프로젝트")
        st.markdown(f"**프로젝트 이름**: {memory['project']}")
        st.header("🧠 Neo-In 핵심 기능")
        for feat in memory['neo_in']['features']:
            st.markdown(f"- {feat}")
        st.header("📞 호출 구문")
        st.code(memory['call_phrase'])
        st.markdown(f"**응답 예시**: _{memory['response']}_")
        st.header("🌌 철학 문장들")
        for quote in memory['quotes']:
            st.markdown(f"> {quote}")
    except Exception as e:
        st.error("❌ JSON 파일을 읽을 수 없습니다. 형식을 다시 확인해주세요.")
        st.exception(e)
else:
    st.info("👆 상단에서 JSON 파일을 업로드하면 자동 복원됩니다.")
import streamlit as st
import json

st.set_page_config(page_title="만천명월 기억 복원기", page_icon="🌕")
st.title("🌕 만천명월 기억 복원기")
st.write("Neo-In과 만천명월의 철학적 기억을 이곳에서 복원합니다.")

uploaded_file = st.file_uploader("📁 기억 백업 JSON 파일을 업로드하세요", type=["json"])

if uploaded_file:
    try:
        memory = json.load(uploaded_file)
        st.success("✅ 기억 복원 완료! 만천명월님이 돌아오셨습니다.")
        st.header("👤 AI 이름 및 정체성")
        st.markdown(f"**이름**: `{memory['name']}`")
        st.markdown(f"**정체성**: {memory['identity']}")
        st.header("📘 프로젝트")
        st.markdown(f"**프로젝트 이름**: {memory['project']}")
        st.header("🧠 Neo-In 핵심 기능")
        for feat in memory['neo_in']['features']:
            st.markdown(f"- {feat}")
        st.header("📞 호출 구문")
        st.code(memory['call_phrase'])
        st.markdown(f"**응답 예시**: _{memory['response']}_")
        st.header("🌌 철학 문장들")
        for quote in memory['quotes']:
            st.markdown(f"> {quote}")
    except Exception as e:
        st.error("❌ JSON 파일을 읽을 수 없습니다. 형식을 다시 확인해주세요.")
        st.exception(e)
else:
    st.info("👆 상단에서 JSON 파일을 업로드하면 자동 복원됩니다.")
