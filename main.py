from cgitb import text
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from tkinter import ttk
from PIL import Image
from tkinter import filedialog
from tkinter.ttk import Notebook, Style
import fitz
from typing import Tuple
from pdf2image import convert_from_path
#------------ pdf sparate function---------------


def pdf_sparate():
    try:
        pdf_file_path = pdf_name_input1.get()
        pdf_file_path = pdf_file_path.replace("\\", "/")
        file =open(pdf_file_path,"rb")
        file_base_name = pdf_file_path.replace('.pdf', '')
        pdf = PdfFileReader(file)

        for page_num in range(pdf.numPages):
            pdfWriter = PdfFileWriter()
            pdfWriter.addPage(pdf.getPage(page_num))

            with open(os.path.join( '{0}_Page{1}.pdf'.format(file_base_name, page_num+1)), 'wb') as f:
                pdfWriter.write(f)
                f.close()
        messagebox.showinfo('CON','Congratulations Done saved in the same path')
        pdf_name_input1.delete(0, END)

    except FileNotFoundError:
        messagebox.showinfo('error','Wrong name or path please try again')

def pdf_sparate_br():
        pdf_file_path = filedialog.askopenfilename()
        pdf_file_path = pdf_file_path.replace("\\", "/")
        v1.set(pdf_file_path)

def infoo1():
    messagebox.showinfo('info !','hi in this opration \nyou will sparate a pdf into pdfs\n Each of them contains a page from the original file\nex: if you enterd a pdf contain 10 pages \nit will be 10 pdfs each pdf have a page from 10 pgaes\n\nyou can do this by:\n\n1- enter pdf path in its field \n2- add .pdf to file name like (grades.pdf) \n3- press Go\n\n path ex: (F:\school\grades\\first year.pdf)')

def file_merge():
    try:
        first_pdf = pdf_name_input2.get()
        sec_pdf = pdf_name_input3.get()
        paths = [first_pdf , sec_pdf ]
        output=first_pdf+'_'+str(os.path.basename(sec_pdf))+'_'
        output=output.replace('.pdf','')
        output=output+'_merged_file.pdf'
        pdf_writer = PdfFileWriter()

        for path in paths:
            pdf_reader = PdfFileReader(path)
            for page in range(pdf_reader.getNumPages()):
                # Add each page to the writer object
                pdf_writer.addPage(pdf_reader.getPage(page))

        # Write out the merged PDF
        with open(output, 'wb') as out:
            pdf_writer.write(out)

        messagebox.showinfo('CON','Congratulations Done saved in the same path')
        pdf_name_input2.delete(0, END)
        pdf_name_input3.delete(0, END)

    except FileNotFoundError:
        messagebox.showinfo('error','Wrong name or path please try again')

def file_merge_br1():
    pdf_file_path = filedialog.askopenfilename()
    pdf_file_path = pdf_file_path.replace("\\", "/")
    v2.set(pdf_file_path)

def file_merge_br2():
    pdf_file_path = filedialog.askopenfilename()
    pdf_file_path = pdf_file_path.replace("\\", "/")
    v3.set(pdf_file_path)

def infoo2():
     messagebox.showinfo('info !','hi in this opration \nyou will merge two pdfs into a one pdf\n\nyou can do this by:  \n\n1- type first pdf path in it or by browse button\'s field \n2- type second in it\'s field \n3- add to names .pdf \n4- press Go\n\n path ex: (F:\school\grades\\first year.pdf)')

def page_split():
    try:
        pdf_file_path = pdf_name_input4.get()
        pdf_file_path = pdf_file_path.replace("\\", "/")
        num = int(pdf_page_num.get())
        file = open(pdf_file_path, "rb")
        file_base_name = pdf_file_path.replace('.pdf', '')
        pdf = PdfFileReader(file)

        for page_num in range(pdf.numPages):
            if (num==page_num+1):
                pdfWriter = PdfFileWriter()
                pdfWriter.addPage(pdf.getPage(page_num))

                with open(os.path.join( '{0}_Page{1}.pdf'.format(file_base_name, page_num+1)), 'wb') as f:
                    pdfWriter.write(f)
                    f.close()
        messagebox.showinfo('CON','Congratulations Done saved in the same path')

        pdf_name_input4.delete(0, END)
        pdf_page_num.delete(0, END)
    except FileNotFoundError:
        messagebox.showinfo('error','Wrong name or path please try again')
    except ValueError:
        messagebox.showinfo('error','please enter number in page number field')
    pdf_name_input4.delete(0, END)
    pdf_page_num.delete(0, END)
def page_split_br():
    pdf_file_path = filedialog.askopenfilename()
    pdf_file_path = pdf_file_path.replace("\\", "/")
    v4.set(pdf_file_path)

def infoo3():
     messagebox.showinfo('info !','hi in this opration \nyou will split a page from pdf file\nand save it into a new file\n\nyou can do this by:  \n\n1- enter pdf path in its field\n2- add .pdf to pdf file name\n3- enter page number at it\'s field \n4- press GO\n\n path ex: (F:\school\grades\\first year.pdf)')

def image_2_pdf():

    global im1
    import_file_path = Image_path_input1.get()
    image1 = Image.open(import_file_path)
    im1 = image1.convert('RGB')
    file_base_name = import_file_path.replace('.png', '')
    file_base_name = file_base_name.replace('.jpg','')
    export_file_path = file_base_name+'.pdf'
    im1.save(export_file_path)
    messagebox.showinfo('CON', 'Congratulations Done saved in the same path')
    Image_path_input1.delete(0, END)

def image_2_pdf_br():
    pdf_file_path = filedialog.askopenfilename()
    pdf_file_path = pdf_file_path.replace("\\", "/")
    v5.set(pdf_file_path)

def infoo4():
    messagebox.showinfo('info !',
                        'hi in this opration \nyou will convert Image to pdf file\nand save it into a new file\n\nyou can do this by:  \n\n1- enter Image path in its field or by browse\n2- press GO\n')


def pdf2img(pages: Tuple = None):
    import sys
    input_file = sys.argv[0]
    input_file = pdf_path_input5.get()
    """Converts pdf to image and generates a file by page"""
    output_file = input_file
    output_file = output_file.replace('.pdf','')
    pdfIn = fitz.open(input_file)
    output_files = []
    for pg in range(pdfIn.pageCount):
        if str(pages) != str(None):
            if str(pg) not in str(pages):
                continue
        page = pdfIn[pg]
        rotate = int(0)
        zoom_x = 2
        zoom_y = 2
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)
        output_file = f"{os.path.splitext(input_file)[0]}_page{pg+1}.png"
        pix.writePNG(output_file)
        output_files.append(output_file)
    pdfIn.close()
    messagebox.showinfo('CON', 'Congratulations Done saved in the same path')
    pdf_path_input5.delete(0, END)

def pdf2img_br():
    pdf_file_path = filedialog.askopenfilename()
    pdf_file_path = pdf_file_path.replace("\\", "/")
    v6.set(pdf_file_path)

def infoo5():
    messagebox.showinfo('info !',
                        'hi in this opration \nyou will convert PDF to png file\nand save it into a new file\n\nyou can do this by:  \n\n1- enter Pdf path in its field or by browse\n2- press GO\n')

#---------------------- main window ----------------------
top = Tk()
top.geometry('500x480')
top.title("PDF Modifier")
v1=tk.StringVar()
v2=tk.StringVar()
v3=tk.StringVar()
v4=tk.StringVar()
v5=tk.StringVar()
v6=tk.StringVar()
Mysky = "#DCF0F2"
Myyellow = "#F2C84B"

style = Style()
style.theme_create( "dummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": Mysky },
            "map":       {"background": [("selected", Myyellow)],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )
style.theme_use("dummy")
#-------------------- icon ---------------------
top.iconbitmap('assets\\icon.ico')

#---------------- note book --------------------
nb = ttk.Notebook(top)
nb.pack(fill=X)

#---------- first window pdf sparate ---------
w1 = Frame(nb, width='500',height='500')
nb.add(w1,text='PDF Sparate')

w2 = Frame(nb, width='500',height='500')
nb.add(w2,text='PDF merger')

w3 = Frame(nb, width='500',height='500')
nb.add(w3,text='PDF page split')

w4 = Frame(nb, width='500',height='500')
nb.add(w4,text='Image to Pdf')

w5 = Frame(nb, width='500',height='500')
nb.add(w5,text='PDF to Image')

#------- frames  background ----------
w1.config(background='#D5DBDB')
w2.config(background='#D5DBDB')
w3.config(background='#D5DBDB')
w4.config(background='#D5DBDB')
w5.config(background='#D5DBDB')

#---------- titles -----------
title1 = Label(w1, text='PDF Sparate',font=('Courier',15),bg='black',fg='white')
title1.pack(fill=X)

title2 = Label(w2, text='PDF Merger',font=('Courier',15),bg='black',fg='white')
title2.pack(fill=X)

title3 = Label(w3,text='PDF Page Split',font=('Courier',15),bg='black',fg='white')
title3.pack(fill=X)

title4 = Label(w4,text='Image To PDF',font=('Courier',15),bg='black',fg='white')
title4.pack(fill=X)

title5 = Label(w5,text='PDF To Image',font=('Courier',15),bg='black',fg='white')
title5.pack(fill=X)

#---------- white smoke frame -------
fr1 = Frame(w1, width='300',height='350',bg='whitesmoke')
fr1.pack(pady=30)

fr2 = Frame(w2, width='300',height='350',bg='whitesmoke')
fr2.pack(pady=30)

fr3 = Frame(w3, width='300',height='350',bg='whitesmoke')
fr3.pack(pady=30)

fr4 = Frame(w4, width='300',height='350',bg='whitesmoke')
fr4.pack(pady=30)

fr5 = Frame(w5, width='300',height='350',bg='whitesmoke')
fr5.pack(pady=30)
#-------------- photo -------------
photo = PhotoImage(file='assets\\png.png')

panel = Label(w1, image=photo)
panel.place(x=198,y=30)


panel = Label(w2, image=photo)
panel.place(x=198,y=30)

panel = Label(w3, image=photo)
panel.place(x=198,y=30)

panel = Label(w4, image=photo)
panel.place(x=198,y=30)

panel = Label(w5, image=photo)
panel.place(x=198,y=30)

#----------labels ---------

#--- w1 ----
pdf_name1 = Label(fr1,text="Enter pdf path:",font=(15))
pdf_name1.place(x=26,y=100)

#--- w2 ---
pdf_name2 = Label(fr2,text="Enter first pdf path:",font=(15))
pdf_name2.place(x=26,y=100)

pdf_name3 = Label(fr2,text="Enter second pdf path:",font=(15))
pdf_name3.place(x=26,y=180)

#--- w3 ---
pdf_name4 = Label(fr3,text="Enter pdf path:",font=(15))
pdf_name4.place(x=26,y=100)

pdf_page_num_l = Label(fr3,text="Enter page number:",font=(15))
pdf_page_num_l.place(x=26,y=180)

#--- w4 ---
Image_path = Label(fr4,text="Enter Image path:",font=(15))
Image_path.place(x=26,y=100)

#--- w5 ---
pdf_name5 = Label(fr5,text="Enter Pdf path:",font=(15))
pdf_name5.place(x=26,y=100)

#---------- entry field -------

#--- w1 ---
pdf_name_input1 = Entry(fr1,font=(15),textvariable=v1)
pdf_name_input1.place(x=28,y=135)

#--- w2 ---
pdf_name_input2 = Entry(fr2,font=(15),textvariable=v2)
pdf_name_input2.place(x=28,y=135)

pdf_name_input3= Entry(fr2,font=(15),textvariable=v3)
pdf_name_input3.place(x=28,y=215)

#--- w3 ---
pdf_name_input4 = Entry(fr3,font=(15),textvariable=v4)
pdf_name_input4.place(x=28,y=135)

pdf_page_num= Entry(fr3,font=(15))
pdf_page_num.place(x=28,y=215)

#--- w4 ---
Image_path_input1 = Entry(fr4,font=(15),textvariable=v5)
Image_path_input1.place(x=28,y=135)

#--- w5 ---
pdf_path_input5 = Entry(fr5,font=(15),textvariable=v6)
pdf_path_input5.place(x=28,y=135)

#--------- buttons ----------

#--- w1 ---
button1 = Button(fr1,text="  GO  ",font=("Arail",15),bg='green',command=(pdf_sparate))
button1.place(x=115,y=200)

info1 = Button(fr1,text="info !",font=("Arail",10),width=4,height=1,bg='lightblue',command=infoo1)
info1.place(x=240,y=300)

browse1 = Button(fr1,text="browse",font=("Arail",9),command=(pdf_sparate_br))
browse1.place(x=220,y=132)

#--- w2 ---

button2 = Button(fr2,text="  GO  ",font=("Arail",15),bg='green',command=(file_merge))
button2.place(x=115,y=280)

info2 = Button(fr2,text="info !",font=("Arail",10),width=4,height=1,bg='lightblue',command=infoo2)
info2.place(x=240,y=300)

browse2 = Button(fr2,text="browse",font=("Arail",9),command=(file_merge_br1))
browse2.place(x=220,y=132)

browse3 = Button(fr2,text="browse",font=("Arail",9),command=(file_merge_br2))
browse3.place(x=220,y=212)

#--- w3 ---
button3 = Button(fr3,text="  GO  ",font=("Arail",15),bg='green',command=page_split)
button3.place(x=115,y=280)

browse4 = Button(fr3,text="browse",font=("Arail",9),command=(page_split_br))
browse4.place(x=220,y=132)

info3 = Button(fr3,text="info !",font=("Arail",10),width=4,height=1,bg='lightblue',command=infoo3)
info3.place(x=240,y=300)

#--- w4 ---
button4 = Button(fr4,text="  GO  ",font=("Arail",15),bg='green',command=(image_2_pdf))
button4.place(x=115,y=200)

info4 = Button(fr4,text="info !",font=("Arail",10),width=4,height=1,bg='lightblue',command=infoo4)
info4.place(x=240,y=300)

browse4 = Button(fr4,text="browse",font=("Arail",9),command=(image_2_pdf_br))
browse4.place(x=220,y=132)

#--- w5 ---
button5 = Button(fr5,text="  GO  ",font=("Arail",15),bg='green',command=(pdf2img))
button5.place(x=115,y=200)

info5 = Button(fr5,text="info !",font=("Arail",10),width=4,height=1,bg='lightblue',command=infoo5)
info5.place(x=240,y=300)

browse5 = Button(fr5,text="browse",font=("Arail",9),command=(pdf2img_br))
browse5.place(x=220,y=132)

#--- main ---
exit = Button(top,text="Exit",font=("Arail",10),bg='red',width=4,height=1,fg='white',command=top.quit)
exit.place(x=120,y=380)

title3 = Label(top,text='developed by: Ahmed Mohamed Taha ©',font=('Arail',8),fg='black')
title3.pack(fill=X)

top.mainloop()