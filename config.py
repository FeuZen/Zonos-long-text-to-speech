# Basic parameters
model = 'hybrid' # choose between 'hybrid' and 'transformer' 
# You will lose some parameters if you choose 'transformer' (see ./CONDITIONING_README.md for more info)

prefix_audio = './neutral.wav' # Path to prefix audio file (Neutral and without noise)
prefix_text = "Your prefix text" # The EXACT transcription of the prefix audio
text_path = './test.txt' # Path to your text file

language = "en-gb" # Language code
audio_output_dir = "./audio_out" # Directory to save the generated audio file, will be created if it doesn't exist
audio_output_name = "final_output" # Name of the final audio output file, without extension (will be saved as .mp3)

speaker_audio = './reference.mp3' # Path to reference audio file (can be .wav too)
speaker_noised = True # Whether to use the denoiser on the reference audio 
# (set this to true if your audio has background noise/echo, only works with the hybrid model)


# Emotion parameters, values between 0 and 1, don't forget to remove "emotion" from the unconditional keys if you want to use emotions
Happiness = 1
Sadness = 0.05
Disgust = 0.05
Fear = 0.05
Surprise = 0.05
Anger = 0.05
Other = 0.1
Neutral = 0.2

# Conditioning and generation parameters, see ./CONDITIONING_README.md for reference
vq_single = 0.78 # VQ single value, between 0 and 1
fmax = 22050 # Maximum frequency, typically 24000 or 22050 (48KHz and 44.1KHz respectively)
pitch_std = 60 # Pitch standard deviation
speaking_rate = 14 # Speaking rate, typically 15
dnsmos_ovrl = 4
cfg_scale = 2
seed = 420
randomize_seed = True # Whether to randomize the seed after each run
unconditional_keys = ["emotion"] # Disabled keys speaker, can be anything from
# ["emotion" "fmax" "pitch_std" "speaking_rate" "vqscore_8" "ctc_loss" "dnsmos_ovrl" "speaker_noised"]

# Sampling parameters
# legacy sampling
top_p = 0
top_k = 0
min_p = 0
# NovelAi's unified sampler
linear = 0.5
confidence = 0.4
quadratic = 0

client_url = "http://127.0.0.1:7860/" # URL of the Gradio client
api_name = "/generate_audio" # API endpoint for audio generation