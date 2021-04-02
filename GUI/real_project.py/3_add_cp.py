import os
import keyboard
import tkinter.ttk as ttk
from tkinter.messagebox import *
from tkinter import *
from tkinter.filedialog import*
from PIL import Image
from PIL import ImageGrab



root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
#root.resizable(False,False)  #창크기(가로,세로) 값 변경불가


#메뉴 만들기 
menu=Menu(root)
#text이름
file="my_note"
#메모장 만들기 
def text_make():
    frame=Frame(root)
    frame.pack(fill="both")
    scroll=Scrollbar(frame)
    scroll.pack(side="right",fill="y")
    global text
    text=Text(frame,yscrollcommand=scroll.set)
    text.pack(side="left",fill="both")
    scroll.config(command=text.yview)
def write():
    with open (file,"w",encoding="utf8") as w:
        w.write(text.get("1.0",END) )

def read():
    if os.path.isfile(file):
        with open (file, "r",encoding="utf8") as r:
            text.delete("1.0",END)
            text.insert(END,r.read())
     

# 캡쳐 도구 만들기
def capture_make():
    #버튼만들기(버튼)
    def screenshot():
        img = ImageGrab.grab()
        small_img = img.resize((798,423), Image.ANTIALIAS )
        small_img.save("시작.png")
        img_path="C:/Users/Administrator/Desktop/파이썬/시작.png"
    
        if os.path.isfile(img_path):
            global change_photo
            change_photo = PhotoImage(file=img_path)
            label.config(image=change_photo)
    
    def start():
        showinfo("시작알림","캡처기능 활성화")
        keyboard.add_hotkey("ctrl+s",screenshot) #스크린샷 저장
        
    frame1=Frame(root)
    frame1.pack(fill="x")
    Button(frame1,text="캡쳐 시작",width=15,height=3,command=start).pack(side="left")
    
    #그림만들기(라벨로 하고 캡처하면 사진변경하기)
    frame2=LabelFrame(root,text="이미지")
    global photo #####함수밖에서도 기능을 수행해야하기 때문에 전역변수처리 #####
    photo = PhotoImage(file="GUI/캡처해주세요.PNG")
    label=Label(frame2,image=photo)
    label.pack()
    frame2.pack(fill="x")
    #저장 경로 만들기(entry,버튼)
    frame3=LabelFrame(root,text="저장 경로")
    def find():
        save_path = askdirectory()
        if save_path == "":
            return
        path.delete(0,END)
        path.insert(0,save_path)

    path=Entry(frame3)
    path.pack(side="left",expand="True",fill="x",padx=10,ipady=3)
    Button(frame3,text="저장경로찾기",height=1,command=find).pack(side="right",padx=10)
    frame3.pack(fill="x")
    
     #포맷 옵션 만들기(버튼,콤보박스)
    frame4=LabelFrame(root,text="옵션")

    val=["PNG","JPG","BMP"]
    cbb=ttk.Combobox(frame4,width=25,state="readonly",value=val)
    cbb.pack(side="right",padx=5)
    cbb.current(0)
    Label(frame4,text="포맷").pack(side="right",padx=5)
    
    frame4.pack(fill="x")


#메모장 메뉴 만들기
menu_text=Menu(menu, tearoff=0)
menu_text.add_command(label="메모장 열기",command=text_make)
menu_text.add_separator()
menu_text.add_command(label="저장",command=write)
menu_text.add_command(label="열기",command=read)
menu.add_cascade(label="메모장",menu=menu_text)


#캡쳐도구 메뉴 만들기
menu_capture=Menu(menu, tearoff=0)
menu_capture.add_command(labe="캡쳐 도구 열기",command=capture_make)
menu_capture.add_separator()
menu_capture.add_command(labe="사진 저장하기")
menu.add_cascade(label="캡쳐 도구",menu=menu_capture)
#끝내기 메뉴 만들기
menu.add_cascade(label="끝내기",command=root.quit)


root.config(menu=menu) #메뉴 활성화
root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건