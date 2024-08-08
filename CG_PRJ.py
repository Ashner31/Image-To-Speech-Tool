import tkinter as tk
from tkinter import filedialog, messagebox
import pytesseract
from PIL import Image
import pyttsx3
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    try:
        print(f"Opening image from path: {image_path}")
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        messagebox.showerror("Error", f"Error reading image: {e}")
        return ""

def text_to_voice(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        messagebox.showerror("Error", f"Error converting text to voice: {e}")

def open_file():
    file_path = filedialog.askopenfilename(
        title="Select Image File",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff;*.tif")]
    )
    if file_path:
        text = image_to_text(file_path)
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, text)

def convert_to_voice():
    text = text_box.get(1.0, tk.END).strip()
    if text:
        text_to_voice(text)
    else:
        messagebox.showwarning("Warning", "No text to convert to voice!")

# main window
root = tk.Tk()
root.title("Image to Voice Converter")

# frame for the buttons
frame = tk.Frame(root)
frame.pack(pady=10)

# open file and convert to voice
open_button = tk.Button(frame, text="Open Image", command=open_file)
open_button.pack(side=tk.LEFT, padx=10)

convert_button = tk.Button(frame, text="Convert to Voice", command=convert_to_voice)
convert_button.pack(side=tk.LEFT, padx=10)

# Add a text box to display the extracted text
text_box = tk.Text(root, wrap='word', width=50, height=15)
text_box.pack(padx=10, pady=10)

# Run the GUI event loop
root.mainloop()
