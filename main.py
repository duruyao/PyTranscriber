#!/usr/bin/env python3

import config

import argparse
from typing import Any, Tuple, Union

from tqdm import tqdm
from pydub import AudioSegment
import speech_recognition as sr


def error_ln(*args: Any, sep: str = ' ', end: str = '\n'):
    """

    :param args:
    :param sep:
    :param end:
    :return:
    """
    print('\033[0;32;31m', sep.join([str(x) for x in args]), '\033[m', sep='', end=end)


def parse_args() -> Tuple[str, str, str]:
    """

    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str,
                        help='input media filename')
    parser.add_argument('-o', '--output', required=False, type=str,
                        help='output text filename (default: INPUT.out.txt)')
    parser.add_argument('-l', '--language', required=False, type=str,
                        help='target language (default: en-US)',
                        default='en-US', choices=['en-GB', 'en-US',
                                                  'zh-CN', 'zh-TW'])
    args = parser.parse_args()
    input_filename = args.input
    output_filename = args.output if args.output else f'{input_filename}.out.txt'
    target_language = args.language
    return input_filename, output_filename, target_language


def transcribe_audio(input_filename: str, output_filename: str, target_language: str) -> Union[str, None]:
    """

    :param input_filename:
    :param output_filename:
    :param target_language:
    :return:
    """
    with tqdm(total=100, desc="Transcribing", unit="%", ncols=100) as pbar:
        temp_filename = f'{input_filename}.temp.wav'
        try:
            audio = AudioSegment.from_file(input_filename)
            pbar.update(10)
            audio.export(temp_filename, format='wav')
            pbar.update(10)
        except Exception as e:
            return f'{e}'

        recognizer = sr.Recognizer()
        with sr.AudioFile(temp_filename) as source:
            audio_data = recognizer.record(source)
            pbar.update(10)
        try:
            text = recognizer.recognize_google(audio_data=audio_data,
                                               key=config.api_keys['google'][0], language=target_language)
            pbar.update(60)
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(text)
            pbar.update(10)
            return None
        except sr.UnknownValueError as e:
            return f'{e} (the speech in file \'{input_filename}\' is unintelligible)'
        except sr.RequestError as e:
            return f'{e} (check your API key, internet connection and proxy setting)'


def main():
    input_filename, output_filename, target_language = parse_args()
    err = transcribe_audio(input_filename, output_filename, target_language)
    if err is not None:
        error_ln(f'\nError: {err}')
        exit(1)
    print(f'\nTranscription Done! See file \'{output_filename}\'')


if __name__ == '__main__':
    main()
