import tkinter as tk
from tkinter import filedialog
import pyttsx3
from PIL import Image, ImageTk


class SpeakingAvatar:
    def __init__(self, root):
        self.root = root
        self.root.title("Speaking Avatar")

        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()

        # Create and configure GUI
        self.create_gui()

    def create_gui(self):
        # Text Entry
        self.text_entry = tk.Entry(self.root, width=40)
        self.text_entry.pack(pady=10)

        # Speak Button
        speak_button = tk.Button(self.root, text="Speak", command=self.speak_text)
        speak_button.pack(pady=5)

        # Image Display
        self.avatar_image = Image.open("C:\\Users\\Lenovo\\Desktop\\man.gif")
 # Replace "avatar.png" with your avatar image
        self.avatar_photo = ImageTk.PhotoImage(self.avatar_image)
        self.avatar_label = tk.Label(self.root, image=self.avatar_photo)
        self.avatar_label.pack(pady=10)

        # Load Image Button
        load_image_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        load_image_button.pack(pady=5)

    def speak_text(self):
        text = self.text_entry.get()
        if text:
            self.engine.say(text)
            self.engine.runAndWait()

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.avatar_image = Image.open(file_path)
            self.avatar_photo = ImageTk.PhotoImage(self.avatar_image)
            self.avatar_label.config(image=self.avatar_photo)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeakingAvatar(root)
    root.mainloop()

