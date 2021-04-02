import tkinter.messagebox as msg #메세지박스를 이용하기위해 메세지박스 라이브러리를 불러온다
from tkinter import *
root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

def info(): 
    msg.showinfo("알림입니다","메세지가왔습니다")
def warn():
    msg.showwarning("경고입니다","위험을 감지하였습니다")
def error():
    msg.showerror("에러입니다","오류가 발생하였습니다")
def okcancel():
    msg.askokcancel("확인/취소입니다","확인하셨습니다")
def retrycancel():
    msg.askretrycancel("재시도/취소입니다","재시도하시겠습니까?")
def ask():
    msg.askyesno("예/아니요입니다","확인하시겠습니까?")

def askcancel():
    response = msg.askyesnocancel(title= None, message="예:누르면 저장후 종료 \n아니요:누르면 저장하지않고 종료 \n취소: 프로그램취소(현재화면에서계속작업)")
    print("응답:",response) #예=(1,True), 아니요=(0,False), 취소=(그외,None)
    if response == 1:
        print("예를 눌렀네요")
    elif response == 0:
        print("아니오를 눌렀네요")
    else:
        print("취소를 눌렀네요") 

Button(root,text="알림" ,command=info).pack()
Button(root,text="경고" ,command=warn).pack()
Button(root,text="에러" ,command=error).pack()
Button(root,text="확인/취소" ,command=okcancel).pack()
Button(root,text="재시도/취소" ,command=retrycancel).pack()
Button(root,text="예/아니요" ,command=ask).pack()
Button(root,text="예/아니요/취소" ,command=askcancel).pack()

root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건