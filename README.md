# Zonos long text to speech
Takes an input text and transcribes it using Zyphra's excellent zonos-v0.1-hybrid ([HuggingFace](https://huggingface.co/Zyphra/Zonos-v0.1-hybrid), [Github](https://github.com/Zyphra/Zonos)) voice cloning tts model running on the gradio API.

## Principle 
The user can provide a text, as long as they want, with emotion tags (e.g., *happy*, *sad*), and the system will chunk it and output the corresponding speech in English.

## Prerequisites
- Python installed
- Zonos-v0.1-hybrid running on gradio (or Zonos-v0.1-transformer but you won't have input denoising)
- os, shutil, gradio_client and pydub libraries installed
- A text to transcribe
- A reference audio for voice cloning

## How to use it
Edit config.py as you wish and run : ```uv run .\main.py```<br>
For more details, check [HOW_TO_RUN.md](./src/HOW_TO_RUN.md)

## Technical details
The chunking system is made to adress context limitations. It uses the same prefix audio before each line of your .txt file so the voice stays clean and consistent throughout the text. (this means you need to have a prefix audio that's exactly to your liking in order to get the same vibe across the whole text) <br>
A different prefix audio can be used for each emotion tag if you want to guide the model better.<br>
Realtime factor : ~0.56 on my RTX 4060 with the model running in WSL