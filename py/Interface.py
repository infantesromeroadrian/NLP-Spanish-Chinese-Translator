import streamlit as st
from AudioCapturer import AudioCapturer
from SpeechTranscriber import SpeechTranscriber
from Translator import HuggingFaceTranslator

class AudioTranslationStreamlitApp:
    def __init__(self):
        self.capturer = AudioCapturer()
        self.transcriber = SpeechTranscriber()
        self.translator = HuggingFaceTranslator()

    def capture_and_process_audio(self):
        output_filename = "captured_audio.wav"
        self.capturer.record(duration=5, output_filename=output_filename)
        transcribed_text = self.transcriber.transcribe(output_filename)
        translated_text = self.translator.translate(transcribed_text)
        return transcribed_text, translated_text

    def run(self):
        st.title('Audio Capture, Transcribe and Translate')
        st.write('Press the button to record audio, transcribe it, and translate from Spanish to Chinese.')

        if st.button('Record Audio'):
            with st.spinner('Recording...'):
                transcribed_text, translated_text = self.capture_and_process_audio()

            st.write("Transcribed Text:")
            st.write(transcribed_text)
            st.write("Translated Text:")
            st.write(translated_text)

if __name__ == '__main__':
    app = AudioTranslationStreamlitApp()
    app.run()