from tkinter import *
root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

#첫번째 줄이런식
btn1 =Button(root,text="F16",width=5,height=2)
btn2 =Button(root,text="F17",width=5,height=2)
btn3 =Button(root,text="F18",width=5,height=2)
btn4 =Button(root,text="F19",width=5,height=2)

btn1.grid(row=0,column=0 ,sticky=N+E+W+S, padx=3, pady=3)
btn2.grid(row=0,column=1,sticky=N+E+W+S, padx=3, pady=3)
btn3.grid(row=0,column=2,sticky=N+E+W+S, padx=3, pady=3)
btn4.grid(row=0,column=3,sticky=N+E+W+S, padx=3, pady=3)
#두번째 줄
btn5 =Button(root,text="clear",width=5,height=2)
btn6 =Button(root,text="=",width=5,height=2)
btn7 =Button(root,text="/",width=5,height=2)
btn8 =Button(root,text="*",width=5,height=2)

btn5.grid(row=1,column=0,sticky=N+E+W+S, padx=3, pady=3)
btn6.grid(row=1,column=1,sticky=N+E+W+S, padx=3, pady=3)
btn7.grid(row=1,column=2,sticky=N+E+W+S, padx=3, pady=3)
btn8.grid(row=1,column=3,sticky=N+E+W+S, padx=3, pady=3)
#세번째 줄
btn9 =Button(root,text="7",width=5,height=2)
btn10 =Button(root,text="8",width=5,height=2)
btn11=Button(root,text="9",width=5,height=2)
btn12 =Button(root,text="-",width=5,height=2)

btn9.grid(row=2,column=0,sticky=N+E+W+S, padx=3, pady=3)
btn10.grid(row=2,column=1,sticky=N+E+W+S, padx=3, pady=3)
btn11.grid(row=2,column=2,sticky=N+E+W+S, padx=3, pady=3)
btn12.grid(row=2,column=3,sticky=N+E+W+S, padx=3, pady=3)
#네번째 줄
btn13=Button(root,text="4",width=5,height=2)
btn14 =Button(root,text="5",width=5,height=2)
btn15=Button(root,text="6",width=5,height=2)
btn16=Button(root,text="+",width=5,height=2)

btn13.grid(row=3,column=0,sticky=N+E+W+S, padx=3, pady=3)
btn14.grid(row=3,column=1,sticky=N+E+W+S, padx=3, pady=3)
btn15.grid(row=3,column=2,sticky=N+E+W+S, padx=3, pady=3)
btn16.grid(row=3,column=3,sticky=N+E+W+S, padx=3, pady=3)
#다섯번째 줄
btn17=Button(root,text="1",width=5,height=2)
btn18=Button(root,text="2",width=5,height=2)
btn19=Button(root,text="3",width=5,height=2)
btn20=Button(root,text="enter",width=5,height=2)

btn17.grid(row=4,column=0,sticky=N+E+W+S, padx=3, pady=3)
btn18.grid(row=4,column=1,sticky=N+E+W+S, padx=3, pady=3)
btn19.grid(row=4,column=2,sticky=N+E+W+S, padx=3, pady=3)
btn20.grid(row=4,column=3,rowspan=2,sticky=N+E+W+S, padx=3, pady=3) #현재위치에서 row(아래로)몇줄을 합쳐주기
#여섯번째 줄
btn21=Button(root,text="0",width=5,height=2) 
btn23=Button(root,text=".",width=5,height=2)


btn21.grid(row=5,column=0, columnspan=2,sticky=N+E+W+S, padx=3, pady=3) #현재 위치에서 column(오른쪽)으로 합쳐주기

btn23.grid(row=5,column=2,sticky=N+E+W+S, padx=3, pady=3)





root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건