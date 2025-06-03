from fastapi import FastAPI
from pydantic import BaseModel
from TTS.api import TTS
import uuid
import os

app = FastAPI()

# Carrega modelo em português (pode trocar por outro)
tts = TTS(model_name="tts_models/pt/cv-corpus-9-multilingual-v2/ljspeech_tts", progress_bar=False, gpu=False)

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

class TextoEntrada(BaseModel):
    text: str

@app.post("/tts")
def gerar_audio(data: TextoEntrada):
    audio_id = str(uuid.uuid4())
    path = os.path.join(DOWNLOAD_DIR, f"{audio_id}.wav")

    try:
        tts.tts_to_file(text=data.text, file_path=path)
        return {"status": "ok", "id": audio_id, "file": f"/{path}"}
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}
