from AudioCapturer import AudioCapturer
from SpeechTranscriber import SpeechTranscriber
from Translator import HuggingFaceTranslator


def main():
    # Capturar audio
    capturer = AudioCapturer()
    capturer.record(duration=10, output_filename="test_audio.wav")

    # Transcribir audio
    transcriber = SpeechTranscriber()
    text = transcriber.transcribe("test_audio.wav")
    print("Texto Transcrito:", text)

    # Traducir texto
    translator = HuggingFaceTranslator()
    translated_text = translator.translate(text)
    print("Texto Traducido:", translated_text)


if __name__ == "__main__":
    main()