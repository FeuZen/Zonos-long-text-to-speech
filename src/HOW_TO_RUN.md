I assume you already got the zonos-v0.1-hybrid running on gradio. If not, check [Zonos' repo](https://github.com/Zyphra/Zonos).
### Install dependencies
```
git clone https://github.com/FeuZen/Zonos-long-text-to-speech.git
cd Zonos-long-text-to-speech
uv venv
.venv/Scripts/Activate
uv pip install os shutil gradio_client pydub
```
### How to use
First you'll need a txt file containing the text you want to synthesize. 
By default, it should be located in the main directory of this repository as text.txt - you can change that (and almost everything else) in [config.py](../config.py). 
Your text has to follow these rules :
1. Short lines (1-2 sentences max.) so the model's context is not overflowed.
2. No weird characters (like emojis, etc.) execpt in tags.
3. Tags (e.g., *happy*) can only be put at the start of a line and has to have a dictionary of the same name in [emotion_config.py](../emotion_config.py). 
4. You don't need a tag on each line : if there's no tag on a line (or if there's an invalid tag), it will default to neutral.<br>

Then, you'll need a reference audio file (20-40s) named reference.mp3 and placed in the main directory of the repo (you can also change that in [config.py](../config.py) -> speaker_audio).<br>

After that, you'll want a prefix audio (neutral.wav by default in [config.py](../config.py)). It has to be clean, neutral, denoised and to your liking. To make it, craft a short neutral sentence or two and use the gradio interface (with default generation settings and your reference audio) to make multiple audios until you really like one, as your text will have the same vibe. Don't forget to take the 1-2 sentences you crafted earlier and put them in the prefix_text variable in [config.py](../config.py).<br>

Finally, you can run ```uv run ./main.py```<br>

See [config.py](../config.py) if you want to change more settings.<br>
See [emotion_config.py](../emotion_config.py) if you want to add or change emotions.<br>

Have fun !