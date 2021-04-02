from tkinter import *

root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

btn1 = Button(root, text="버튼1") #버튼1이란 버튼만들기
btn1.pack() #버튼을 만들기위한 필수조건

btn2 = Button(root, padx=5, pady=5, text="버튼2") #pad x,y 는 글자를 중심으로 x,y로만큼의 여백들어간 크기의 버튼 (글자가 많아지면 버튼이커짐)
btn2.pack() #버튼을 만들기위한 필수조건

btn3 = Button(root, width=5, height=5, text="버튼3") #width,height는 말크대로 버튼의 크기 (글자수와 상관없이 일정한 크기)
btn3.pack() #버튼을 만들기위한 필수조건

btn4 = Button(root, fg="white",bg="black", text="버튼4") #fg글자색,bg버튼의 배경색
btn4.pack() #버튼을 만들기위한 필수조건

photo = PhotoImage(file="Game/내공.png") #이미지불러오기
btn6 = Button(root, image=photo)  #불러온 이미지로 버튼만들기
btn6.pack()

def btn7_cmd(): #버튼이 눌렸을때 하는 동작을 함수로 정의
    print("동작")

btn7 = Button(root, text="동작버튼",command=btn7_cmd) # command로 버튼이 눌렸을때 함수를 실행한다
btn7.pack()


root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건