
import pyaudio
import wave

class AudioCapturer:
    def __init__(self, format=pyaudio.paInt16, channels=1, rate=44100, frames_per_buffer=1024):
        self.format = format
        self.channels = channels
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer
        self.audio = pyaudio.PyAudio()

    def record(self, duration=5, output_filename="output.wav"):
        print("Iniciando la grabación...")
        stream = self.audio.open(format=self.format, channels=self.channels,
                                 rate=self.rate, input=True,
                                 frames_per_buffer=self.frames_per_buffer)
        frames = []

        for _ in range(0, int(self.rate / self.frames_per_buffer * duration)):
            data = stream.read(self.frames_per_buffer)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        self.audio.terminate()

        with wave.open(output_filename, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.audio.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(frames))

        print(f"Grabación finalizada. El audio se ha guardado en '{output_filename}'.")