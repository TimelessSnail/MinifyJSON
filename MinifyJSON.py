import json
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def minify_json():
    filepath = filedialog.askopenfilename(
        title="Choose a JSON file",
        filetypes=[("JSON files", "*.json")]
    )

    if not filepath:
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        output_dir = filedialog.askdirectory(title="Choose a folder to saved the minified file")

        if not output_dir:
            return

        filename = os.path.splitext(os.path.basename(filepath))[0]
        new_path = os.path.join(output_dir, filename)

        with open(new_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, separators=(',', ':'))

        messagebox.showinfo("Succes", f"Minified file saved :\n{new_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occured :\n{e}")

root = tk.Tk()
root.title("Minify JSON")
root.geometry("300x100")

button = tk.Button(root, text="Choose a JSON file", command=minify_json)
button.pack(pady=30)

root.mainloop()
