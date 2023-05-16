## Audio Transcription using OpenAI API
This Python script uses OpenAI's API to transcribe audio files. Specifically, it takes an MP3 file as input, transcribes it using OpenAI's Audio API, and then writes the transcription into a text file.

## Dependencies
* os: This module provides a way of using operating system dependent functionality. We are using it to fetch environment variables.
* openai: This is OpenAI's Python client library. It is used to interact with OpenAI's APIs.
* librosa: This is a Python library for music and audio analysis.
* pydub: This library allows you to manipulate audio with a simple and easy high level interface. It is not used in the code but may be needed for additional audio processing tasks.
* tempfile: This module generates temporary files and directories. It allows the program to handle large amounts of data that won't fit into memory.

# Steps
The script follows these steps:

1. It fetches your OpenAI API key from the environment variable 'OPENAI_API_KEY' and sets it as the API key for the OpenAI client.
2. It fetches the name of the MP3 file you want to transcribe from the environment variable 'MP3_FILENAME'.
3. It opens the specified MP3 file in binary read mode.
4. It uses the OpenAI API to transcribe the audio file. Note that the model identifier "whisper-1" is hardcoded in this script. If OpenAI has other models available for audio transcription, you might want to change this identifier.
5. It prints the transcribed text to the console.
6. It writes the transcribed text into a file named 'transcription.txt'.
7. It prints a message to the console indicating that the transcription has been saved.

# Usage
To use this script, you need to set the following environment variables:

`OPENAI_API_KEY`: Your OpenAI API key.

`MP3_FILENAME`: The name of the MP3 file you want to transcribe.

After setting these environment variables, you can run the script using a Python interpreter. The transcribed text will be written into a file named 'transcription.txt' in the same directory as the script.

# Note
Please ensure that you have the required permissions to read the MP3 file and write to the directory where the script is running.

Also, this script does not handle any exceptions. In a production environment, you should add error handling code to manage potential issues like the MP3 file not being found, the OpenAI API returning an error, etc.

# How To Use

```
export OPENAI_API_KEY='sk-xxx'
export MP3_FILENAME='sample.mp3'
python3 transcription.py
```