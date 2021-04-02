import tkinter.ttk as ttk
from tkinter import *
root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

#메뉴 만들기 
menu=Menu(root)
#메모장 만들기 
def text_make():
    frame=Frame(root)
    frame.pack(fill="both")
    scroll=Scrollbar(frame)
    scroll.pack(side="right",fill="y")
    text=Text(frame,yscrollcommand=scroll.set)
    text.pack(side="left",fill="both")
    scroll.config(command=text.yview)
# 캡쳐 도구 만들기
def capture_make():
    #버튼만들기(버튼)
    frame1=Frame(root)
    frame1.pack(fill="x")
    Button(frame1,text="캡쳐 시작",width=15,height=3).pack(side="left")
    #그림만들기(라벨로 하고 캡처하면 사진변경하기)
    frame2=LabelFrame(root,text="이미지")
    global photo #####함수밖에서도 기능을 수행해야하기 때문에 전역변수처리 #####
    photo = PhotoImage(file="GUI/캡처해주세요.PNG")
    label=Label(frame2,image=photo)
    label.pack()
    frame2.pack(fill="x")
    #저장 경로 만들기(entry,버튼)
    frame3=LabelFrame(root,text="저장 경로")
    Entry(frame3).pack(side="left",expand="True",fill="x",padx=10,ipady=3)
    Button(frame3,text="저장경로찾기",height=1).pack(side="right",padx=10)
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