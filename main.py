from tkinter import Entry,Button,Tk,messagebox,Label,PhotoImage
font=('Bell Mt',20,'bold')

ramz_dic={'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9',
    'j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19',
    't':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26',' ':'27'}
unramz_dic={v:k for k,v in ramz_dic.items()}

def ramz_konande (txt):
    char_ramz=[ramz_dic.get(char,char) for char in txt]
    return ' '.join(char_ramz)

def un_ramz (txt):
    char_unramz=[unramz_dic.get(char,char) for char in txt.split()]
    return ''.join(char_unramz)

def btn_code ():
    txt=en_txt.get().lower()
    txt_ramz=ramz_konande(txt)
    en_code.delete(0,'end')
    en_code.insert(0,txt_ramz)

def btn_decode ():
    txt=en_code_de.get().lower()
    txt_unramz=un_ramz(txt)
    en_txt_de.delete(0,'end')
    en_txt_de.insert(0,txt_unramz)


root=Tk()
#تنظیمات
root.geometry('900x600')
root.title('Coder')

#بک گراند
img=PhotoImage(file='R2.png')
lbl_bg=Label(root,image=img)
lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

#ساخت لیبل
til_coder=Label(root,text="Coder",font=font,bg="black",fg='white')
til_coder.grid(row=0,column=0,padx=10,pady=10)

lbl_txt=Label(root,text="Text: ",font=font,bg="black",fg='white')
lbl_txt.grid(row=1,column=0,padx=10,pady=10)

lbl_code=Label(root,text="Code: ",font=font,bg="black",fg='white')
lbl_code.grid(row=2,column=0,padx=10,pady=10)

til_decoder=Label(root,text="Decoder",font=font,bg="black",fg="white")
til_decoder.grid(row=0,column=2,padx=10,pady=10)

lbl_code_de=Label(root,text='Code: ',font=font,bg="black",fg="white")
lbl_code_de.grid(row=1,column=2,padx=10,pady=10)

lbl_txt_de=Label(root,text='Text: ',font=font,bg="black",fg="white")
lbl_txt_de.grid(row=2,column=2,padx=10,pady=10)

#ساحت اینتری
en_txt=Entry(root,font=font,bg="black",fg="white")
en_txt.grid(row=1,column=1,padx=10,pady=10)

en_code=Entry(root,font=font,bg="black",fg="white")
en_code.grid(row=2,column=1,padx=10,pady=10)

en_code_de=Entry(root,font=font,bg="black",fg="white")
en_code_de.grid(row=1,column=3,padx=10,pady=10)

en_txt_de=Entry(root,font=font,bg="black",fg="white")
en_txt_de.grid(row=2,column=3,padx=10,pady=10)

#دکمه
btn_code=Button(root,text="Code",font=font,bg="black",fg='white',command=btn_code)
btn_code.grid(row=4,column=1)

btn_de=Button(root,text="Decode",font=font,bg="black",fg="white",command=btn_decode)
btn_de.grid(row=4,column=3)



root.mainloop()