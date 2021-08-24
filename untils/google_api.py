# export GOOGLE_APPLICATION_CREDENTIALS="akaOCR-56d7564dc6ae.json"
from google.cloud import speech
import io
import soundfile as sf
import os
import pandas as pd
from tqdm import tqdm


def writeFile(fileName, content):
    with open(fileName, 'a') as f1:
        f1.write(content + os.linesep)

def transcribe_file(speech_file):
    client = speech.SpeechClient()
    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ms-MY",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        return result.alternatives[0].transcript

# df = pd.read_csv('data.csv')
#
# for idx, row in tqdm(df.iterrows(), total=df.shape[0]):
#     path_file = os.path.join('data',row['path_file'])
#     transcript = transcribe_file(path_file)
#     writeFile('result_transcript.csv', f'{path_file};{transcript}')