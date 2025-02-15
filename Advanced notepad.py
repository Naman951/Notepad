import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Success", "File saved successfully!")

def toggle_dark_mode():
    global dark_mode
    if dark_mode:
        root.config(bg="white")
        text_area.config(bg="white", fg="black", insertbackground="black")
        dark_mode = False
    else:
        root.config(bg="black")
        text_area.config(bg="black", fg="white", insertbackground="white")
        dark_mode = True

def change_font():
    new_font = simpledialog.askstring("Font", "Enter font (e.g., Arial, Courier, Times New Roman):")
    new_size = simpledialog.askinteger("Size", "Enter font size (e.g., 12, 14, 16):")
    if new_font and new_size:
        text_area.config(font=(new_font, new_size))

def find_replace():
    find_text = simpledialog.askstring("Find", "Enter text to find:")
    replace_text = simpledialog.askstring("Replace", "Enter replacement text:")
    content = text_area.get(1.0, tk.END)
    new_content = content.replace(find_text, replace_text)
    text_area.delete(1.0, tk.END)
    text_area.insert(1.0, new_content)

def word_count():
    content = text_area.get(1.0, tk.END)
    words = len(content.split())
    messagebox.showinfo("Word Count", f"Total words: {words}")

# Creating GUI Window
root = tk.Tk()
root.title("Advanced Notepad")
root.geometry("600x400")

# Dark Mode Flag
dark_mode = False  

# Creating Menu Bar
menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Find & Replace", command=find_replace)
edit_menu.add_command(label="Word Count", command=word_count)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Options Menu
options_menu = tk.Menu(menu_bar, tearoff=0)
options_menu.add_command(label="Toggle Dark Mode", command=toggle_dark_mode)
options_menu.add_command(label="Change Font", command=change_font)
menu_bar.add_cascade(label="Options", menu=options_menu)

root.config(menu=menu_bar)

# Text Area
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")

# Run the application
root.mainloop()
