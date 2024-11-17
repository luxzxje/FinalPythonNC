import tkinter as tk
from tkinter import font

# Hàm xử lý sự kiện khi bấm nút
def button_click(value):
    current_text = entry.get()
    if value == "C":  # Xóa màn hình
        entry.delete(0, tk.END)
    elif value == "=":  # Tính toán
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif value == "±":  # Đổi dấu
        if current_text:
            if current_text[0] == "-":
                entry.delete(0, tk.END)
                entry.insert(0, current_text[1:])
            else:
                entry.delete(0, tk.END)
                entry.insert(0, "-" + current_text)
    elif value == "%":  # Phần trăm
        try:
            result = float(current_text) / 100
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:  # Thêm ký tự vào màn hình
        entry.insert(tk.END, value)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x600")
root.resizable(False, False)
root.configure(bg="#000000")

# Font chữ
entry_font = font.Font(family="Helvetica", size=30, weight="bold")
button_font = font.Font(family="Helvetica", size=20, weight="bold")

# Màn hình hiển thị
entry = tk.Entry(
    root, font=entry_font, bg="#333333", fg="#FFFFFF", 
    justify="right", bd=0, insertbackground="white"
)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10, ipady=10)

# Cấu hình nút
buttons = [
    ("C", 1, 0, "#FF9500"), ("±", 1, 1, "#505050"), ("%", 1, 2, "#505050"), ("/", 1, 3, "#FF9500"),
    ("7", 2, 0, "#505050"), ("8", 2, 1, "#505050"), ("9", 2, 2, "#505050"), ("*", 2, 3, "#FF9500"),
    ("4", 3, 0, "#505050"), ("5", 3, 1, "#505050"), ("6", 3, 2, "#505050"), ("-", 3, 3, "#FF9500"),
    ("1", 4, 0, "#505050"), ("2", 4, 1, "#505050"), ("3", 4, 2, "#505050"), ("+", 4, 3, "#FF9500"),
    ("0", 5, 0, "#505050"), (".", 5, 2, "#505050"), ("=", 5, 3, "#FF9500"),
]

# Tạo các nút
for text, row, col, color in buttons:
    if text == "0":  # Nút "0" kéo dài 2 cột
        btn = tk.Button(
            root, text=text, font=button_font, bg=color, fg="white",
            activebackground="#D4D4D2", activeforeground="black",
            command=lambda t=text: button_click(t), bd=0, relief="flat"
        )
        btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
    else:
        btn = tk.Button(
            root, text=text, font=button_font, bg=color, fg="white",
            activebackground="#D4D4D2", activeforeground="black",
            command=lambda t=text: button_click(t), bd=0, relief="flat"
        )
        btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Điều chỉnh tỉ lệ dòng và cột
for i in range(6):  # Dòng
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # Cột
    root.grid_columnconfigure(j, weight=1)

# Chạy ứng dụng
root.mainloop()
