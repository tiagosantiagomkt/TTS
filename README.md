# 🗣️ API Open Source de TTS com Coqui

Este projeto expõe uma API para conversão de texto em voz usando o modelo open source Coqui TTS em português.

## 🚀 Como usar

- Envie um texto via POST para `/tts`
- O servidor gera um arquivo `.wav` com a fala

### Requisição

```json
POST /tts
{
  "text": "Olá, tudo bem com você?"
}
