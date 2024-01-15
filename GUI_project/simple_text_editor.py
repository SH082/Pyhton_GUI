import tkinter as tk
from tkinter import filedialog

class SimpleNotepad:
    def __init__(self, master):
        self.master = master
        self.master.title("간단한 메모장")
        self.master.geometry("600x400")

        # 텍스트 위젯 생성
        self.text = tk.Text(self.master, wrap="word", undo=True)
        self.text.pack(expand=True, fill="both")

        # 메뉴바 생성
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # 파일 메뉴
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="파일", menu=self.file_menu)
        self.file_menu.add_command(label="새로 만들기", command=self.new_file)
        self.file_menu.add_command(label="열기", command=self.open_file)
        self.file_menu.add_command(label="저장", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="끝내기", command=self.master.destroy)

    def new_file(self):
        self.text.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text.get(1.0, tk.END)
                file.write(content)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleNotepad(root)
    root.mainloop()