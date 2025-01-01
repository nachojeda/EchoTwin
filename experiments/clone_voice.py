import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
# wav = tts.tts(text="Hello world!", speaker_wav="data/my_voice.wav", language="en")
# Text to speech to a file
tts.tts_to_file(
    text="Salut, je m’appelle Nacho et j’aime beaucoup ma chérie, à tel point que je vais l’emmener à Paris pour essayer des crêpes, visiter des musées et lui donner un bon baiser français.",
    speaker_wav="data/my_voice.wav",
    language="fr",
    file_path="outputs/my_voice_fr.wav"
    )