from tkinter import Tk, Button, filedialog
from tkinter.scrolledtext import ScrolledText
import tkinter
import codecs

root = Tk()
root.geometry("500x400")
root.title("初めての狂ったエディタ")

scrolledtext = ScrolledText(root, state="normal", font=("", 15), bg="#F2F2F2")
scrolledtext.place(x=20, y=20, width=480, height=340)

# テキストをファイルに保存するsave関数
def save(self):
    # ダイアログ表示
    name = filedialog.asksaveasfilename()
    text = scrolledtext.get("1.0", tkinter.END)
    # ファイルを作成
    f = codecs.open(name, "w", "utf-8")
    f.write(text)
    f.close()

btn = Button(root, text="保存", bg="#CED8F6")
btn.place(x=400, y=370, width=80, height=20)
btn.bind("<ButtonRelease-1>", save)

root.mainloop()
