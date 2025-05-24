import tkinter as tk
from tkinter import messagebox
import pyshorteners

# Function to shorten URL
def shorten_url():
    original_url = url_entry.get()
    if not original_url:
        messagebox.showwarning("Warning", "Please enter a URL")
        return

    try:
        # Create a Shortener object using TinyURL (default)
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(original_url)
        result_label.config(text=f"Shortened URL:\n{short_url}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to shorten URL: {e}")

# Create main window
root = tk.Tk()
root.title("URL Link Shortener - Python")
root.geometry("400x250")
root.resizable(False, False)

# Heading label
heading = tk.Label(root, text="Python URL Shortener", font=("Arial", 18, "bold"))
heading.pack(pady=10)

# URL Entry field
url_entry = tk.Entry(root, font=("Arial", 14), width=40)
url_entry.pack(pady=10)

# Shorten Button
shorten_button = tk.Button(root, text="Shorten URL", font=("Arial", 14), command=shorten_url)
shorten_button.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue", wraplength=350)
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
