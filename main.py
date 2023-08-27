#!/usr/bin/env python3

import speech_recognition as sr
from pydub import AudioSegment


def transcribe_audio(input_audio_path, output_text_path, target_language):
    recognizer = sr.Recognizer()

    # convert audio files from .m4a to .wav format
    audio = AudioSegment.from_file(input_audio_path, format='m4a')
    audio.export('temp.wav', format='wav')

    with sr.AudioFile('temp.wav') as source:
        audio_data = recognizer.record(source)
    try:
        if target_language == 'en':
            text = recognizer.recognize_google(audio_data, language='en-US')
        elif target_language == 'zh':
            text = recognizer.recognize_google(audio_data, language='zh-CN')
        else:
            print(f'Error: Unsupported language type \'{target_language}\'')
            return
        with open(output_text_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text)
        print('Transcription Done!')
    except sr.UnknownValueError:
        print('Error: Cannot recognize language in audio')
    except sr.RequestError as e:
        print(f'Error: {e}, check your net connection or proxy server setting')


if __name__ == '__main__':
    transcribe_audio('input_audio.m4a', 'output_text.txt', 'zh')
