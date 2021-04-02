from tkinter import *

root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

Label(root, text = "시계를 골라 주세요").pack() # 따로 여러개 만들게 아니라면 이렇게 바로 lable만들기 가능

watch_var = IntVar() #체크박스와다르게 한개만 만든다
watch1 = Radiobutton(root, text="갤럭시워치", value=1, variable=watch_var)
watch2 = Radiobutton(root, text="애플워치", value=2, variable=watch_var)
watch3 = Radiobutton(root, text="샤오밍워치", value=3, variable=watch_var)
watch1.select()
watch1.pack()
watch2.pack()
watch3.pack()

Label(root, text = "이어폰을 골라 주세요").pack() # 따로 여러개 만들게 아니라면 이렇게 바로 lable만들기 가능
earphone_var = StringVar() # var값을 글자로 받는다
earphone1 = Radiobutton(root, text="버즈",value="버즈",variable=earphone_var)
earphone2 = Radiobutton(root, text="에어팟",value="에어팟",variable=earphone_var)
earphone3 = Radiobutton(root, text="QCY",value="QCY",variable=earphone_var)
earphone1.select()
earphone1.pack()
earphone2.pack()
earphone3.pack()

def cmd():
    print(watch_var.get()) # 선택된 라이도의 항목의 값(value)출력
    print(earphone_var.get())
    print("-----------")

btn = Button(root, text="버튼", command = cmd)
btn.pack()

root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건