import pyautogui
import time
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def autotyper(text, delay):
    messagebox.showinfo("Info", "Switch to the window where you want the text to be typed...")
    time.sleep(5)
    
    for char in text:
        pyautogui.write(char)
        time.sleep(delay)

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    entry_file_path.delete(0, tk.END)
    entry_file_path.insert(0, file_path)

def start_typing():
    file_path = entry_file_path.get()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_to_type = file.read()
        delay_between_characters = float(entry_delay.get())
        autotyper(text_to_type, delay_between_characters)
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {file_path}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid delay (a number).")
    except UnicodeDecodeError:
        messagebox.showerror("Error", f"Could not decode the file '{file_path}'. Try using a different encoding.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Auto Typer Script by AreyMadhav")

# File path input
tk.Label(root, text="Text File Path:").grid(row=0, column=0, padx=10, pady=10)
entry_file_path = tk.Entry(root, width=50)
entry_file_path.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=10, pady=10)

# Delay input
tk.Label(root, text="Delay between characters (seconds):").grid(row=1, column=0, padx=10, pady=10)
entry_delay = tk.Entry(root, width=10)
entry_delay.grid(row=1, column=1, padx=10, pady=10)
entry_delay.insert(0, "0.1")

# Start button
tk.Button(root, text="Start Typing", command=start_typing).grid(row=2, column=0, columnspan=3, pady=20)

# Run the application
root.mainloop()
