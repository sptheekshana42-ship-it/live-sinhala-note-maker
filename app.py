import streamlit as st

st.set_page_config(page_title="Live Sinhala Class Notes", page_icon="🎙️")

st.title("🎙️ Live Class Sinhala Voice-to-Notes AI")
st.write("Zoom පන්තිය ලවුඩ්ස්පීකර් එකෙන් අසන්නට සලසා, පහත බටන් එක ඔබා සජීවීව සටහන් ලබා ගන්න.")

# Web Speech API භාවිතා කරමින් බ්‍රවුසර් එකෙන්ම ලයිව් සිංහල ලිවීම සඳහා HTML/JS කෝඩ් එක
st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <button id="start-btn" style="background-color: #ff4b4b; color: white; padding: 12px 24px; font-size: 16px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">🔴 Start Live Listening</button>
        <button id="stop-btn" style="background-color: #6c757d; color: white; padding: 12px 24px; font-size: 16px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; margin-left: 10px;">⏹️ Stop</button>
    </div>
    
    <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; min-height: 250px; color: black; font-size: 18px; line-height: 1.6;" id="notes-box">
        <b>සටහන් මෙහි දිස්වනු ඇත... (කතා කරන්න පටන් ගන්න)</b>
    </div>

    <script>
        const startBtn = document.getElementById('start-btn');
        const stopBtn = document.getElementById('stop-btn');
        const notesBox = document.getElementById('notes-box');

        let recognition;
        let finalTranscript = '';

        if ('webkitSpeechRecognition' in window || 'speechRecognition' in window) {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            recognition = new SpeechRecognition();
            recognition.continuous = true;
            recognition.interimResults = true;
            recognition.lang = 'si-LK'; // සිංහල භාෂාව සඳහා

            recognition.onstart = function() {
                notesBox.innerHTML = "<b>හඬ ශ්‍රවණය කරමින් පවතී... (සර් කතා කරන දේවල් මෙහි වැටේ)</b><br>";
            };

            recognition.onresult = function(event) {
                let interimTranscript = '';
                for (let i = event.resultIndex; i < event.results.length; ++i) {
                    if (event.results[i].isFinal) {
                        finalTranscript += event.results[i][0].transcript + "<br>";
                    } else {
                        interimTranscript += event.results[i][0].transcript;
                    }
                }
                notesBox.innerHTML = finalTranscript + '<span style="color: gray;">' + interimTranscript + '</span>';
            };

            recognition.onerror = function(event) {
                console.error("Speech recognition error", event.error);
            };

            recognition.onend = function() {
                // නැවත ස්වයංක්‍රීයව අසන්නට සැලැස්වීම
                try {
                    recognition.start();
                } catch (e) {}
            };

            startBtn.onclick = function() {
                finalTranscript = '';
                try {
                    recognition.start();
                } catch (e) {}
            };

            stopBtn.onclick = function() {
                recognition.stop();
            };
        } else {
            notesBox.innerHTML = "ඔබගේ බ්‍රවුසර් එක මෙම පහසුකම සඳහා සහය නොදක්වයි. කරුණාකර Google Chrome භාවිතා කරන්න.";
        }
    </script>
""", unsafe_allow_html=True)
