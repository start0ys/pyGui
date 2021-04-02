import tkinter.ttk as ttk # 프로그래스바 를 사용하려면 tkinter.ttk을 import해줘야하고 길기때문에 편의상ttk로 사용하기위해 as처리
from tkinter import *

root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("480x540+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

#파일 추가 선택삭제 버튼
frame0=Frame(root,padx=5)
Button(frame0,text="파일추가",padx=25,pady=5).pack(side="left")
Button(frame0,text="선택삭제",padx=25,pady=5).pack(side="right")
frame0.pack(side="top",expand=True,fill="both")


#선택한 파일이 보이는곳(listbox,scrollbar)
frame1=Frame(root,padx=5,pady=5)

scroll=Scrollbar(frame1)
scroll.pack(side="right",fill="y")
listbox=Listbox(frame1,yscrollcommand=scroll.set)
listbox.pack(side="left",expand="True",fill="both")
scroll.config(command=listbox.yview)
frame1.pack(expand=True,fill="both")


#저장경로 가 보이는 곳(entry,button)
frame2=LabelFrame(root,text="저장경로",padx=5,pady=5)
Entry(frame2).pack(side="left",expand="True",fill="x",padx=3)
Button(frame2,text="찾아보기",padx=10,pady=2).pack(side="right",padx=3)
frame2.pack(expand=True,fill="both")


#옵션이 보이는 곳 (label,combobox)
frame3=LabelFrame(root,text="옵션",padx=5,pady=5)

#가로넓이

Label(frame3,text="가로넓이").pack(side="left",padx=5)
val_1=["원본유지",1024,800,640]
cbb1=ttk.Combobox(frame3,width=10,value=val_1 ,state="readonly")
cbb1.pack(side="left",padx=5)
cbb1.set("원본유지")


#간격
val_2=["없음","좁게","보통","넓게"]
Label(frame3,text="간격").pack(side="left",padx=5)
cbb2=ttk.Combobox(frame3,width=10,value=val_2 ,state="readonly")
cbb2.pack(side="left",padx=5)
cbb2.set("없음")


#포맷
val_3=["PNG","JPG","BMP"]
Label(frame3,text="포맷").pack(side="left",padx=5)
cbb3=ttk.Combobox(frame3,width=10,value=val_3 ,state="readonly")
cbb3.pack(side="left",padx=5)
cbb3.set("PNG")

frame3.pack(fill="both")


#진행상황 (progressbar)
frame4=LabelFrame(root,text="진행상황",padx=5)
ttk.Progressbar(frame4).pack(expand="True",fill="x")
frame4.pack(expand=True,fill="both")


#시작 삭제
frame5=Frame(root,padx=5,pady=5)
Button(frame5,text="닫기",padx=25,pady=5).pack(side="right",padx=10)
Button(frame5,text="시작",padx=25,pady=5).pack(side="right")
frame5.pack(side="bottom",expand=True,fill="both")

root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건