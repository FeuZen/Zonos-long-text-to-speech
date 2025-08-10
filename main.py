from gradio_client import Client, handle_file

client = Client("http://127.0.0.1:7860/")
result = client.predict(
		model_choice="Zyphra/Zonos-v0.1-hybrid",
		text="prefix text, input text", # don't forget the prefix text if you're using prefix audio
		language="en-gb",
		speaker_audio=handle_file('./reference.mp3'), # Reference audio
		prefix_audio=handle_file('./audio.wav'), # Prefix audio 
		e1=1, # Happiness
		e2=0.05, # Sadness
		e3=0.05, # Disgust
		e4=0.05, # Fear
		e5=0.05, # Surprise
		e6=0.05, # Anger
		e7=0.1, # Other
		e8=0.2, # Neutral
		vq_single=0.78,
		fmax=24000,
		pitch_std=60,
		speaking_rate=15,
		dnsmos_ovrl=4,
		speaker_noised=True,
		cfg_scale=2,
		top_p=0,
		top_k=0,
		min_p=0,
		linear=0.5,
		confidence=0.4,
		quadratic=0,
		seed=420,
		randomize_seed=True,
		unconditional_keys=["emotion"], # Disabled keys
		api_name="/generate_audio"
)
print(result)