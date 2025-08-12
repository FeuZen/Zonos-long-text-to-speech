import config as cfg

# No neutral dict as it's the default found in config.py

happy = {
         "Happiness" : 1,
         "Sadness" : 0.05,
         "Disgust" : 0.05,
         "Fear" : 0.05,
         "Surprise" : 0.05,
         "Anger" : 0.05,
         "Other" : 0.1,
         "Neutral" : 0.1,

         "pitch_std" : 90,
         "unconditional_keys" : [], # You can try to disable these if you want : "vqscore_8", "dnsmos_ovrl"
         # (They're disabled when they're IN the "unconditional_keys" list)
         # DISCLAIMER : Disabling "vqscore_8" and "dnsmos_ovrl" can worsen quality but may be preferable for expressiveness
         "speaking_rate" : 15,

         # If you want better quality, make multiple attempts on creating the prefix audio in the gradio interface
         # (while tweaking the parameters) for the specific emotion until you have a good one
         # Then change prefix_audio and prefix_text below.
         # Or you can just use it as is using the default prefix audio and text
         "prefix_audio" : cfg.prefix_audio, 
         "prefix_text" : cfg.prefix_text
         }

gentle = {
         "Happiness" : 0.05,
         "Sadness" : 0.15,
         "Disgust" : 0.05,
         "Fear" : 0.05,
         "Surprise" : 0,
         "Anger" : 0,
         "Other" : 0.15,
         "Neutral" : 0.4,

         "pitch_std" : 40, 
         "unconditional_keys" : [],
         "speaking_rate" : 12.5,
         "prefix_audio" : cfg.prefix_audio, 
         "prefix_text" : cfg.prefix_text
         }

# You can add more emotions here, just copy one of the dictionaries and change the values