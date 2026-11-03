# Intelligent Voice Command Desktop Assistant

A simple desktop voice assistant built in Python with:
- voice input using SpeechRecognition
- voice output using pyttsx3
- GUI using Tkinter
- basic automation for opening apps, web search, time/date, and notes

## Features
- Start the assistant from a desktop window
- Speak commands such as:
  - "hello"
  - "what time is it"
  - "what is the date"
  - "open chrome"
  - "search for python tutorials"
  - "note this is my meeting reminder"
  - "exit"

## Setup
1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
   On Windows:
   ```bash
   .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python main.py
   ```

## Notes
- If `PyAudio` fails to install on Linux, install PortAudio:
  ```bash
  sudo apt-get install portaudio19-dev
  ```
- On Windows, ensure your microphone is enabled and working.
- The app uses Google Speech Recognition online, so internet access is required.

## Project Idea
This project is a strong beginner/intermediate desktop assistant concept for a CSE mini-project or final-year project.
