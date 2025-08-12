import time
start_time = time.time()
import config as cfg, emotion_config as emo_cfg
from src import functions as fn, gradio_client

# Loading the .txt file and cleaning it up
content = fn.read_text_file(cfg.text_path) # Read the text file specified in config.py and converts it to a list of strings

# Load the prefix audio and get its duration
loaded_prefix_audio = fn.load_audio(cfg.prefix_audio)
prefix_audio_duration = fn.get_audio_duration(loaded_prefix_audio)


###### Line by line audio generation ######
final_audio = loaded_prefix_audio # Start with the prefix audio (will be removed at the end)
line_number, line_count = 0, len(content)

# Main loop
for line in content:
   # Check for tags
   if line.startswith("*") and "*" in line[1:]:
      tag = line.split("*")[1] # Extract the tag from the line
      line = line.replace(f"*{tag}*", "").strip() # Remove the tag from the line
      emo = emo_cfg.__dict__.get(tag, None) # Get the emotion from the dictionary
      if emo != None:
         temp_audio_path = gradio_client.inference(text=f"{emo["prefix_text"]} {line}", 
                                                   Happiness=emo["Happiness"],
                                                   Sadness=emo["Sadness"],
                                                   Disgust=emo["Disgust"],
                                                   Fear=emo["Fear"],
                                                   Surprise=emo["Surprise"],
                                                   Anger=emo["Anger"], 
                                                   Other=emo["Other"],
                                                   Neutral=emo["Neutral"],
                                                   pitch_std=emo["pitch_std"],
                                                   unconditional_keys=emo["unconditional_keys"],
                                                   speaking_rate=emo["speaking_rate"],
                                                   prefix_audio=emo["prefix_audio"])[0] 
         
      else:
      # Create and append the audio for each line
         print(f"Emotion '{tag}' not found in emotion_config.py, using default settings.")
         temp_audio_path = gradio_client.inference(text=f"{cfg.prefix_text} {line}")[0]
   else:
      temp_audio_path = gradio_client.inference(text=f"{cfg.prefix_text} {line}")[0]
   temp_audio = fn.load_audio(temp_audio_path)
   temp_audio = fn.cut_audio(temp_audio, prefix_audio_duration) # Remove the prefix audio from the temporary audio
   final_audio = fn.append_audio(final_audio, temp_audio)
   line_number += 1
   proportion_done = line_number / line_count
   proportion_remaining = 1 - proportion_done
   elapsed_time = time.time() - start_time
   remaining_time = elapsed_time / proportion_done * proportion_remaining
   print(f"~{round((proportion_done)*100, 1)}% - {fn.format_time(elapsed_time)} elapsed - ~{fn.format_time(remaining_time)} remaining")

final_audio = fn.cut_audio(final_audio, prefix_audio_duration) # Remove the prefix audio from the final output
###########################################


fn.save_audio(final_audio, f"{cfg.audio_output_dir}/{cfg.audio_output_name}.mp3")
print(f"Done in {fn.format_time(time.time()-start_time)}.")
print(f"Final audio saved to {cfg.audio_output_dir}/{cfg.audio_output_name}.mp3.")
print(f"Realtime ratio : {round((fn.get_audio_duration(final_audio)/1000)/(time.time()-start_time), 3)}.")