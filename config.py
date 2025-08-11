# Basic parameters
model = 'hybrid' # choose between 'hybrid' and 'transformer'

prefix_audio = './neutral.wav' # Path to prefix audio file
prefix_text = "Prefix text" # The transcription of the prefix audio
text = "" # Text to synthesize, don't forget the prefix text if you're using prefix audio
text_path = './test.txt' # Path to text file, if you want to use a long text file instead of a limited string
# Use the text variable only for testing purposes, otherwise put your text in a .txt file as it will use chunking (line by line so put only one or two sentences per line)

language = "en-gb" # Language code, choose between 'en-gb', 'en-us', 'fr-fr'
audio_output_dir = "./audio_out" # Directory to save the generated audio file, will be created if it doesn't exist

speaker_audio = './reference.mp3' # Path to reference audio file
speaker_noised = True # Whether to use the denoiser on the reference audio (set this to true if your audio has background noise/echo, only works with the hybrid model)


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
fmax = 24000 # Maximum frequency, typically 24000 or 22050 (48KHz and 44.1KHz respectively)
pitch_std = 60 # Pitch standard deviation
speaking_rate = 15 # Speaking rate, typically 15
dnsmos_ovrl = 4
cfg_scale = 2
seed = 420
randomize_seed = True # Whether to randomize the seed after each run
unconditional_keys = ["emotion"] # Disabled keys 

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