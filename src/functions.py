import os
import shutil
import config as cfg
from pydub import AudioSegment

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
   line_number = 0
   for line in content:
       content[line_number] = line.strip("\n")
       line_number += 1
   return content


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

def save_audio(audio, output_path, format="wav"):
    """Save audio to file"""
    audio.export(output_path, format=format)

def get_audio_duration(audio):
    """Get audio duration in milliseconds"""
    return len(audio)