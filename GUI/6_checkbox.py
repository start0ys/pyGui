from tkinter import *

root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가


chkvar = IntVar() # chkvar 에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text="갤럭시워치",variable=chkvar)
#chkbox.select() # 자동 체크 처리
#chkbox.deselect() # 체크 해제 처리

chkbox.pack()


chkvar2 = IntVar() # chkvar 에 int 형으로 값을 저장한다
chkbox2 = Checkbutton(root, text="애플워치",variable=chkvar2)
#chkbox2.select() # 자동 체크 처리
#chkbox2.deselect() # 체크 해제 처리

chkbox2.pack()


def cmd():
    print(chkvar.get()) #체크 박스 값 가져오기 0:체크해제 1:체크
    print(chkvar2.get()) #체크 박스 값 가져오기 0:체크해제 1:체크
    print("-----------")

btn = Button(root, text="버튼", command = cmd)
btn.pack()

root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건