from gradio_client import Client, handle_file
import config as cfg

client = Client(cfg.client_url)

def inference(text=f"{cfg.prefix_text} {cfg.text}",
				  model=cfg.model,
				  language=cfg.language,
				  speaker_audio=cfg.speaker_audio,
				  prefix_audio=cfg.prefix_audio,

				  Happiness=cfg.Happiness,
				  Sadness=cfg.Sadness,
				  Disgust=cfg.Disgust,
				  Fear=cfg.Fear,
				  Surprise=cfg.Surprise,
				  Anger=cfg.Anger,
				  Other=cfg.Other,
				  Neutral=cfg.Neutral,

				  vq_single=cfg.vq_single,
				  fmax=cfg.fmax,
				  pitch_std=cfg.pitch_std,
				  speaking_rate=cfg.speaking_rate,
				  dnsmos_ovrl=cfg.dnsmos_ovrl,
				  speaker_noised=cfg.speaker_noised,
				  cfg_scale=cfg.cfg_scale,
				  top_p=cfg.top_p,
				  top_k=cfg.top_k,
				  min_p=cfg.min_p,
				  linear=cfg.linear,
				  confidence=cfg.confidence,
				  quadratic=cfg.quadratic,
				  seed=cfg.seed,
				  randomize_seed=cfg.randomize_seed,

				  unconditional_keys=cfg.unconditional_keys,
				  api_name=cfg.api_name
				  ):
	"""Run inference using the Gradio client."""
	result = client.predict(
			model_choice=f"Zyphra/Zonos-v0.1-{model}",
			text=text, # don't forget the prefix text if you're using prefix audio
			language=language,
			speaker_audio=handle_file(speaker_audio) if speaker_audio!=None else None, # Reference audio
			prefix_audio=handle_file(prefix_audio) if prefix_audio!=None else None, # Prefix audio 
			e1=Happiness,
			e2=Sadness,
			e3=Disgust,
			e4=Fear,
			e5=Surprise,
			e6=Anger,
			e7=Other,
			e8=Neutral,
			vq_single=vq_single,
			fmax=fmax,
			pitch_std=pitch_std,
			speaking_rate=speaking_rate,
			dnsmos_ovrl=dnsmos_ovrl,
			speaker_noised=speaker_noised,
			cfg_scale=cfg_scale,
			top_p=top_p,
			top_k=top_k,
			min_p=min_p,
			linear=linear,
			confidence=confidence,
			quadratic=quadratic,
			seed=seed,
			randomize_seed=randomize_seed,
			unconditional_keys=unconditional_keys, # Disabled keys
			api_name=api_name
	)
	return result