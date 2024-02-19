
# WhisperTypist: Audio Transcription and Keyboard Typing Automation

## Description

This project provides a simple solution for audio transcription and automated typing. It includes a Python-based audio transcriber that converts spoken words into text and an automated keyboard typer for simulating typing actions based on transcribed text. Ideal for when you're in an ecosystem where speech to text is not available.

## Features

- **Audio Transcription:** Converts audio input into text using OpenAI's Whisper TTS model.
- **Keyboard Typer:** Simulates keyboard typing actions based on the transcribed text using `ydotool`.

## Installation

To install and run this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. **Build ydotool:** This project requires `ydotool` for simulating keyboard inputs at a low level. You need to build `ydotool` from source on your system and ensure the `ydotool` binary is available in the working directory. Follow the instructions on the ydotool GitHub page for building from source.

## Usage

- **Main Script:** The `main.py` script serves as the entry point of the application, orchestrating the audio transcription and typing simulation.
- **Audio Transcriber:** `audio_transcriber.py` handles the conversion of audio input into text.
- **Keyboard Typer:** `keyboard_typer.py` is responsible for simulating keyboard typing actions.

To execute the main script, run:

```bash
python main.py
```

## Requirements

- Python 3.11 (others might work, but untested)
- Required Python packages (see `requirements.txt` for versions)
- ydotool (build from source)

## License

This project is open-source and available under the MIT License.
