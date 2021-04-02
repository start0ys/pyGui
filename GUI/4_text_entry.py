from tkinter import *

root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

txt = Text(root, width = 30 ,height=5) #메모장과 같은 글을쓸수있는 창을 만든다 창의 크기를 넘어서까지 글을쓰면 위에쓴 글은 올라가 보이지않음
txt.pack()

txt.insert(END,"시작") #메모장에 첫실행화면부터 "시작"이라는 글씨를 삽입

e = Entry(root , width=30 ) #엔터를 칠수없고 한줄이상 사용할수없다 아이디,비번창을 쓸떄 사용
e.pack()

e.insert(0,"한줄만 쓰시오")

def cmd():
    print(txt.get("1.0",END)) #txt의 내용을 가져오는데 txt창의 처음(1.0)부터 끝(END)까지 가져오기 "1,0"이 처음부터란뜻이고 1은 1번Line, 0은 컬럼의 처음부터
    print(e.get())

    #버튼을 눌렀을떄 위의 txt와 e 안의 내용을 출력하고 txt와 e 안의 내용을 삭제하기
    txt.delete("1.0",END) 
    e.delete(0,END)

btn = Button(root, text="작성한 글 print하기", command = cmd)
btn.pack()

root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건