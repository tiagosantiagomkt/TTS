# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
import uuid
import os
from TTS.api import TTS

app = FastAPI()
tts_model = TTS(model_name="tts_models/pt/cv-corpus-9-multilingual-v2/ljspeech_tts", progress_bar=False, gpu=False)

OUTPUT_DIR = "downloads"
os.makedirs(OUTPUT_DIR, exist_ok=True)

class TextInput(BaseModel):
    text: str

@app.post("/tts")
def gerar_audio(data: TextInput):
    audio_id = str(uuid.uuid4())
    path = os.path.join(OUTPUT_DIR, f"{audio_id}.wav")
    try:
        tts_model.tts_to_file(text=data.text, file_path=path)
        return {"status": "ok", "id": audio_id, "path": path}
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}
