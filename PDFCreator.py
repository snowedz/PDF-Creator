from tkinter import *
import tkinter.filedialog as fd
import img2pdf
import os
from PIL import Image, ImageTk

# place an image on the grid
def display_logo(url, row, column):
    img = Image.open(url)
    img = img.resize((int(img.size[0]/2),int(img.size[1]/2)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg="#3d3d3d")
    img_label.image = img
    img_label.grid(column=0, row=0)


# initiallize a Tkinter root object
root = Tk()
root.geometry("300x400")
root.configure(background='#3d3d3d')
root.title("PDF Creator")

# header area - logo & browse button
header = Frame(root, width=200, height=150, bg="#3d3d3d")
header.grid(columnspan=3, rowspan=3, row=0)
display_logo('logo.png', 0, 0)

# main content area - text and image extraction
main_content = Frame(root, width=400, height=100, bg="#3d3d3d")
main_content.grid(columnspan=3, rowspan=3, row=3)
# load a JPG file
def openfile():
    global file
    file = fd.askopenfilenames(parent=root, filetypes=[("JPG File", ".JPG")])
    file = list(file)
    return file
# save PDF
def finalfile():
    finalfile = fd.asksaveasfilename(parent=root, filetypes=[("PDF","*.pdf")], title ="Dê um nome")
    with open(finalfile+".pdf","wb") as f:
        f.write(img2pdf.convert(file))

# Botões
save_img_menu = Frame(root, width=200, height=95, bg="#4b4b4b")
save_img_menu.grid(columnspan=1, rowspan=2, row=2)
openFile_btn = Button(root, text="Selecionar Imagens", command=lambda:openfile(), font=("shanti", 10), height=0, width=15)
openFile_btn.grid(row=2,column=0)
saveAll_btn = Button(root, text="Salvar PDF", command=lambda:finalfile(), font=("shanti", 10), height=0, width=15)
saveAll_btn.grid(row=3,column=0)


root.mainloop()
