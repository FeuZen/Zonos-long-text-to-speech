import os, shutil
import config as cfg
from pydub import AudioSegment # type: ignore

# Function to save the audio output
def copy_audio_file(temp_path, destination_dir="./audio_out"):
    os.makedirs(destination_dir, exist_ok=True)
    filename = os.path.basename(temp_path)
    destination_path = os.path.join(destination_dir, filename)
    shutil.copy2(temp_path, destination_path)
    return destination_path


# Function to read text from a file
def read_text_file(file_path=cfg.text_path):
    with open(file_path, 'r', encoding="utf-8") as file:
       content = file.readlines()
    file.close()
    content = [line.strip() for line in content if line.strip()]
    return content


# Time converter
def format_time(seconds):
    """Convert seconds to HH:MM:SS format"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


# Audio manipulation functions
def load_audio(file_path):
    """Load audio file"""
    return AudioSegment.from_file(file_path)

def cut_audio(audio, start_ms, end_ms=None):
    """Cut audio from start_ms to end_ms"""
    if end_ms is None:
        end_ms = len(audio)
    return audio[start_ms:end_ms]

def append_audio(audio1, audio2):
    """Append two audio segments"""
    return audio1 + audio2

def save_audio(audio, output_path, format="mp3"):
    """Save audio to file"""
    audio.export(output_path, format=format, bitrate="320k")

def get_audio_duration(audio):
    """Get audio duration in milliseconds"""
    return len(audio)