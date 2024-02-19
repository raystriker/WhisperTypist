import threading
import wave

import pyaudio
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

from audio_transcriber import transcribe
from keyboard_typer import type_text, type_text_init


class RecordApp(App):
    def build(self):
        """
        Builds and returns a BoxLayout widget containing two buttons for starting and stopping recording,
        with the specified properties and bindings.
        """
        # Set background color or add a background image
        Window.clearcolor = get_color_from_hex('#101216')

        self.is_recording = False
        self.record_thread = None

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.start_button = Button(text='Start Recording',
                                   background_normal='',
                                   background_color=get_color_from_hex('#007ACC'),
                                   color=get_color_from_hex('#FFFFFF'),
                                   size_hint=(1, 0.2),
                                   font_size='50sp')
        self.stop_button = Button(text='Stop Recording',
                                  background_normal='',
                                  background_color=get_color_from_hex('#D32F2F'),
                                  color=get_color_from_hex('#FFFFFF'),
                                  disabled=True,
                                  size_hint=(1, 0.2),
                                  font_size='50sp')

        self.start_button.bind(on_press=self.start_recording)
        self.stop_button.bind(on_press=self.stop_recording)

        layout.add_widget(self.start_button)
        layout.add_widget(self.stop_button)

        return layout

    def start_recording(self, instance):

        self.is_recording = True
        self.start_button.disabled = True
        self.stop_button.disabled = False
        self.record_thread = threading.Thread(target=self.record)
        self.record_thread.start()

    def stop_recording(self, instance):
        self.is_recording = False
        self.start_button.disabled = False
        self.stop_button.disabled = True

    def record(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100

        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        wf = wave.open('output.wav', 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        once = False

        while self.is_recording:
            if not once:
                once = True
                print('Recording...')
            data = stream.read(CHUNK, exception_on_overflow=False)
            wf.writeframes(data)

        stream.stop_stream()
        stream.close()
        p.terminate()
        wf.close()

        text_to_type = transcribe('output.wav')
        type_text(text_to_type)


if __name__ == '__main__':
    type_text_init()
    RecordApp().run()
