import config as cfg
from src import functions as fn, gradio_client

# Loading the .txt file and cleaning it up
content = fn.read_text_file(cfg.text_path) # Read the text file specified in config.py and converts it to a list of strings

loaded_prefix_audio = fn.load_audio(cfg.prefix_audio)
prefix_audio_duration = fn.get_audio_duration(loaded_prefix_audio)

final_audio = loaded_prefix_audio # Start with the prefix audio (will be removed at the end)

for line in content:
   temp_audio_path = gradio_client.inference(text=f"{cfg.prefix_text} {line}")[0]
   temp_audio = fn.load_audio(temp_audio_path)
   temp_audio = fn.cut_audio(temp_audio, prefix_audio_duration)
   final_audio = fn.append_audio(final_audio, temp_audio)

final_audio = fn.cut_audio(final_audio, prefix_audio_duration) # Remove the prefix audio from the final output

fn.save_audio(final_audio, f"{cfg.audio_output_dir}/final_output.mp3", format="mp3")