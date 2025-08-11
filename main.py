import config as cfg
from src import gradio_client

result = gradio_client.inference()

print(result)