import tkinter as tk
from tkinter import scrolledtext

from assistant import VoiceAssistant


class VoiceAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Intelligent Voice Command Desktop Assistant")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.assistant = VoiceAssistant()

        title = tk.Label(root, text="Voice Assistant", font=("Arial", 20, "bold"))
        title.pack(pady=(20, 10))

        self.output = scrolledtext.ScrolledText(
            root,
            width=80,
            height=18,
            wrap=tk.WORD,
            font=("Arial", 11),
        )
        self.output.pack(padx=20, pady=10)
        self.output.insert(tk.END, "Assistant ready...\n")

        self.start_button = tk.Button(
            root,
            text="Start Listening",
            width=20,
            height=2,
            font=("Arial", 11, "bold"),
            command=self.handle_listen,
        )
        self.start_button.pack(pady=(5, 20))

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def append_output(self, text: str):
        self.output.insert(tk.END, text + "\n")
        self.output.see(tk.END)

    def handle_listen(self):
        self.start_button.config(state="disabled")
        self.append_output("Listening...")

        command = self.assistant.listen()

        if command:
            self.append_output(f"You said: {command}")
            response = self.assistant.handle_command(command)
            self.append_output(f"Assistant: {response}")
            self.assistant.speak(response)
        else:
            self.append_output("I did not hear a command.")
            self.assistant.speak("I did not hear a command.")

        self.start_button.config(state="normal")

    def on_close(self):
        self.assistant.running = False
        self.root.destroy()


def main():
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
