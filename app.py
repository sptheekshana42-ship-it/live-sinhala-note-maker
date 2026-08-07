import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Sinhala Class Note Maker AI", page_icon="🎙️")

st.title("🎙️ Sinhala Zoom Class Note Maker AI")
st.write("පන්තියේ ඕඩියෝ ෆයිල් එක (Audio/Mp3) මෙතැනට Upload කර AI සටහන් ලබා ගන්න.")

# OpenAI / Groq API Key එක (අවශ්‍ය නම් පසුව එකතු කරගත හැක)
# මෙහිදී සරලව ශ්‍රව්‍ය ගොනුවක් අප්ලෝඩ් කර නෝට්ස් ලබාගත හැක.

uploaded_file = st.file_uploader("ඔබේ පන්තියේ රෙකෝඩින් එක (mp3, wav, m4a) මෙතැනට දමන්න", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/mp3')
    
    if st.button("✨ Generate AI Notes (නෝට්ස් සාදන්න)"):
        with st.spinner("AI එක මඟින් සටහන් සකස් කරමින් පවතී... ටිකක් රැඳී සිටින්න."):
            # තාවකාලිකව පෙන්වීම සඳහා
            st.success("සටහන් සාර්ථකව සකස් කරන ලදී!")
            
            st.markdown("""
            ### 📝 පන්ති සටහන් (Notes):
            - **විෂය:** ක්‍රිප්ටෝ / Zoom පන්තිය
            - **සටහන:** ඉහත උඩුගත කළ ශ්‍රව්‍ය ගොනුව මත පදනම් වූ AI සටහන් මෙහි දිස්වේ.
            """)
