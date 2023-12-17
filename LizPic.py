import tkinter as tk
import tkinter.filedialog as fd
import script as sc
import tkinter.messagebox as mb


def choose_file():
    file_name[0] = fd.askopenfilename(title="открыть файл")
    label3["text"] = f"Изображение \"{file_name[0]}\" загружен"

def main():
    sizer = 10
    if len(entry2.get())!=0:
        sizer = int(entry2.get())
    try:
        img = sc.Open_image(file_name[0],sizer)
    except:
        mb.showerror(title="Error", message="Неверный файл")

    chars = sc.chars
    if len(entry1.get())!=0:
        chars = [c for c in entry1.get()]
        chars.reverse()
    text_img = sc.Pic_to_text(img,chars)

    sc.Write(text_img, file_name[0].split('.')[0])
    label4["text"]=f"Текст {file_name[0].split('.')[0]}.txt выгружен"

window = tk.Tk()
window.geometry('400x400')
window.title('LizaPic')
file_name = ['']


label1 = tk.Label(text = "Символьный градиент(от светлого к темному)"
                      "\n по умолчанию используеться ( .:;x$&)")
label1.pack()

entry1 = tk.Entry()
entry1.pack()

label2 = tk.Label(text = "Величина уменьшения изображения"
                         "\n по умолчанию 10")
label2.pack()

entry2 = tk.Entry()
entry2.pack()

label3 = tk.Label()
label3.pack()
label4 = tk.Label()
label4.pack()




butt = tk.Button(text="Выбрать картинку", command=choose_file)
butt.pack()

ok_but = tk.Button(text = "OK", command=main)
ok_but.pack()

window.mainloop()