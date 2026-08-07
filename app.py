import streamlit as st
import speech_recognition as sr

st.set_page_config(page_title="Live Sinhala Class Note Maker", page_icon="🎙️")

st.title("🎙️ Live Class Audio to Sinhala Notes AI")
st.write("Zoom ක්ලාස් එක ස්පීකර් එකෙන් අසන්නට සලසා, පහත බොත්තම ඔබා ලයිව් නොට්ස් ලබා ගන්න.")

LANGUAGE_CODE = "si-LK" 

if "notes" not in st.session_state:
    st.session_state.notes = ""

col1, col2 = st.columns(2)

with col1:
    start_button = st.button("🔴 Start Live Listening")

with col2:
    stop_button = st.button("⏹️ Stop & Clear")

if stop_button:
    st.session_state.notes = ""
    st.rerun()

if start_button:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("හඬ ශ්‍රවණය කරමින් පවතී... (කතා කරන්න)")
        r.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=15)
            text = r.recognize_google(audio, language=LANGUAGE_CODE)

            st.session_state.notes += "\n- " + text
            st.success("සාර්ථකයි!")
            st.rerun()

        except sr.WaitTimeoutError:
            st.warning("හඬක් ඇසුනේ නැත. නැවත උත්සාහ කරන්න.")
        except sr.UnknownValueError:
            st.warning("ශබ්දය පැහැදිලි නැත, නැවත උත්සාහ කරන්න.")
        except Exception as e:
            st.error(f"දෝෂයක් සිදු විය: {e}")

st.subheader("📝 Live Generated Notes (සිංහල සටහන්):")
st.markdown(
    f"""
    <div style="background-color: #f0f2f6; padding: 15px; border-radius: 10px; min-height: 200px; color: black;">
    {st.session_state.notes if st.session_state.notes else "සටහන් මෙහි දිස්වනු ඇත..."}
    </div>
    """,
    unsafe_allow_html=True
)

