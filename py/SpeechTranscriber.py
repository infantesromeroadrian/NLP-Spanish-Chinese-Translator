import speech_recognition as sr

class SpeechTranscriber:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe(self, audio_file):
        try:
            with sr.AudioFile(audio_file) as source:
                audio_data = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio_data)
                return text
        except sr.UnknownValueError:
            # Error cuando el reconocimiento no entiende lo que se dijo
            return "Error: No se pudo entender el audio."
        except sr.RequestError as e:
            # Error de red o al conectarse al servicio de reconocimiento
            return f"Error de solicitud: {e}"