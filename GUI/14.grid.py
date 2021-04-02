from tkinter import *
root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

btn1 =Button(root,text="0,0")
btn2 =Button(root,text="0,1")

btn4 =Button(root,text="1,1")

btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)

btn4.grid(row=1,column=1)



root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건