# PyTranscriber

[PyTranscriber](https://github.com/duruyao/PyTranscriber) transcribes audio or video to text.

## 1. Prerequisites

- [Python 3.X](https://www.python.org)
- [FFmpeg](https://ffmpeg.org)
- [pydub](https://pypi.org/project/pydub)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition)

Make sure you have [Python 3.X](https://www.python.org) installed, then run the command `python3 --version` to verify.

Run the command `python3 setup.py install` to install other Python dependencies and OS dependencies.

## 2. Usage

Just run the command `python3 main.py <INPUT_FILENAME>` to transcribe your media to text.

Run the command `python3 main.py --help` to show help manual.

```text
usage: main.py [-h] [-o OUTPUT] [--language {en-GB,en-US,zh-CN,zh-TW}] input

positional arguments:
  input                 input media filename

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output text filename
  --language {en-GB,en-US,zh-CN,zh-TW}
                        target language
```