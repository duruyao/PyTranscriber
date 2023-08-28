#!/usr/bin/env python3

import argparse
from typing import Tuple

from pydub import AudioSegment
import speech_recognition as sr


def parse_args() -> Tuple[str, str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, help='input media filename')
    parser.add_argument('-o', '--output', required=False, type=str, help='output text filename')
    parser.add_argument('--language', required=False, type=str, default='en-US', help='target language',
                        choices=['en-GB', 'en-US',
                                 'zh-CN', 'zh-TW'])
    args = parser.parse_args()
    input_filename = args.input
    output_filename = args.output if args.output else f'{input_filename}.out.txt'
    target_language = args.language
    return input_filename, output_filename, target_language


def transcribe_audio(input_filename: str, output_filename: str, target_language: str):
    temp_filename = f'{input_filename}.temp.wav'
    try:
        audio = AudioSegment.from_file(input_filename)
        audio.export(temp_filename, format='wav')
    except Exception as e:
        print(f'Error: {e}')
        return

    recognizer = sr.Recognizer()
    with sr.AudioFile(temp_filename) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data, language=target_language)
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(text)
        print(f'Transcription Done! See {output_filename}')
    except sr.UnknownValueError:
        print(f'Error: Cannot recognize language in {input_filename}')
        return
    except sr.RequestError as e:
        print(f'Error: {e}, check your net connection or proxy server setting')
        return


if __name__ == '__main__':
    transcribe_audio(*parse_args())
