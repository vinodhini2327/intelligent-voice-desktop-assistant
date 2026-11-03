import datetime
import os
import subprocess
import webbrowser
from pathlib import Path
from urllib.parse import quote

import pyttsx3
import speech_recognition as sr


class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 170)
        self.running = True

    def speak(self, text: str) -> None:
        if not text:
            return
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self) -> str:
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=10)

            command = self.recognizer.recognize_google(audio)
            return command.strip()

        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

    def open_app(self, app_name: str) -> str:
        app_name = app_name.lower().strip()
        if not app_name:
            return "Which application do you want to open?"

        if os.name == "nt":
            apps = {
                "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                "google chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                "notepad": "notepad.exe",
                "calculator": "calc.exe",
                "paint": "mspaint.exe",
                "file explorer": "explorer.exe",
            }

            if app_name in apps:
                try:
                    subprocess.Popen(apps[app_name])
                    return f"Opening {app_name}."
                except FileNotFoundError:
                    return f"{app_name} is not installed on this computer."

            if "chrome" in app_name:
                try:
                    subprocess.Popen(apps["google chrome"])
                    return "Opening Chrome."
                except FileNotFoundError:
                    return "Chrome is not installed on this computer."

            if "notepad" in app_name:
                try:
                    subprocess.Popen("notepad.exe")
                    return "Opening Notepad."
                except FileNotFoundError:
                    return "Notepad is not available."

            return f"I do not know how to open {app_name}."

        app_commands = {
            "chrome": "google-chrome",
            "google chrome": "google-chrome",
            "browser": "xdg-open https://www.google.com",
            "notepad": "gedit",
            "calculator": "gnome-calculator",
            "terminal": "gnome-terminal",
        }

        if app_name in app_commands:
            try:
                if app_name == "browser":
                    os.system(app_commands[app_name])
                else:
                    subprocess.Popen(app_commands[app_name])
                return f"Opening {app_name}."
            except Exception:
                return f"I could not open {app_name}."

        return f"I do not know how to open {app_name}."

    def save_note(self, content: str) -> str:
        notes_dir = Path.home() / "voice_assistant_notes"
        notes_dir.mkdir(exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"note_{timestamp}.txt"
        file_path = notes_dir / filename

        file_path.write_text(content, encoding="utf-8")
        return f"Note saved at {file_path}"

    def handle_command(self, command: str) -> str:
        if not command:
            return "I did not hear anything clearly."

        command = command.lower().strip()

        if "hello" in command or "hi" in command:
            return "Hello! I am your voice assistant. How can I help you?"

        if "who are you" in command:
            return "I am an intelligent voice command desktop assistant."

        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}."

        if "date" in command:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            return f"Today is {current_date}."

        if "open " in command or "launch " in command:
            app_name = command.replace("open ", "").replace("launch ", "").strip()
            return self.open_app(app_name)

        if "search for " in command:
            query = command.replace("search for ", "").strip()
            url = "https://www.google.com/search?q=" + quote(query)
            webbrowser.open_new_tab(url)
            return f"Searching the web for {query}."

        if "note " in command:
            note_text = command.replace("note ", "", 1).strip()
            if not note_text:
                return "Please provide the note text after the word note."
            return self.save_note(note_text)

        if "exit" in command or "quit" in command or "stop" in command:
            self.running = False
            return "Goodbye!"

        if "thank you" in command:
            return "You are welcome!"

        return "I heard you. I can help with time, date, searching, opening apps, and creating notes."
