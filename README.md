# PyTranscriber

[PyTranscriber](https://github.com/duruyao/PyTranscriber) transcribes audio or video to text.

## 1. Prerequisites

### 1.1. OS Dependencies

- [Python 3.X](https://www.python.org)
- [FFmpeg](https://ffmpeg.org)

Make sure you have [Python 3.X](https://www.python.org) installed, then run the command `python3 --version` to verify.

Make sure you have [FFmpeg](https://ffmpeg.org) installed, then run the command `ffmpeg -version` to verify.

### 1.2. Python Dependencies

- [tqdm](https://pypi.org/project/tqdm)
- [pydub](https://pypi.org/project/pydub)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition)

Run the command `pip3 install -r requirements.txt` to install the required Python packages.

## 2. Usage

Just run the command `python3 main.py <INPUT_FILENAME>` to transcribe your media to text.

Run the command `python3 main.py --help` to show help manual.

```text
usage: main.py [-h] [-o OUTPUT] [-l {en-GB,en-US,zh-CN,zh-TW}] input

positional arguments:
  input                 input media filename

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output text filename (default: INPUT.out.txt)
  -l {en-GB,en-US,zh-CN,zh-TW}, --language {en-GB,en-US,zh-CN,zh-TW}
                        target language (default: en-US)
```