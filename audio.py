import wave
import pyaudio

class Audio:
    def __init__(self, audioFile):
        # Open the wave file
        self.f = wave.open(audioFile, 'rb')
        # Read the wave file parameters
        self.channels = self.f.getnchannels()
        self.sample_width = self.f.getsampwidth()
        self.frame_rate = self.f.getframerate()
        self.num_frames = self.f.getnframes()

        # Create a P    yAudio object
        self.p = pyaudio.PyAudio()

        # Open a PyAudio stream
        self.stream = self.p.open(format=self.p.get_format_from_width(self.sample_width),
                                  channels=self.channels,
                                  rate=self.frame_rate,
                                  output=True)

    def play(self):
        # Play the wave file
        self.data = self.f.readframes(self.num_frames)
        self.stream.write(self.data)

    # Stop the PyAudio stream
    def stop(self):
        self.stream.stop_stream()
        self.stream.close()

    def terminate(self):
        # Terminate the PyAudio object
        self.p.terminate()
