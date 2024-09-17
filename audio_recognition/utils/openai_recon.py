# Нужные импорты
import openai
from django.conf import settings
from numba.cuda.mathimpl import fp16_cos_impl

from settings import BASE_DIR
import os
import whisper

# Ключ с openai API
openai.api_key = settings.OPEN_AI_API_KEY


# Сама функция, где берем файл и прогоняем его через openai
def open_ai_get_text(filename='file_for_test.mp3'):
    audio_file = open(str(os.path.join(BASE_DIR, 'audio_recognition', 'samples', filename)), "rb")
    response = openai.Audio.transcribe(model="whisper-1", engine="whisper",response_format="text", file=audio_file)
    return response.text


def whisper_get_text(audio_file):
    model = whisper.load_model("small")
    transcript = model.transcribe(audio_file)
    return transcript["text"]

def generate_corrected_transcript(system_prompt = "Please transcribe following audiofile", filename='file_for_test.mp3'):
    audio_file = open(str(os.path.join(BASE_DIR, 'audio_recognition', 'samples', filename)), "rb")
    transcript = openai.Audio.transcribe('whisper-1', audio_file)
    print(transcript)

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": transcribe(audio_file, "")
            }
        ]
    )
    return response.choices[0].message.content
