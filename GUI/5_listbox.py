from tkinter import *

root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

listbox = Listbox(root, selectmode="extended", height=0) 
#selectmode가 extended면 여러개를 한번에 선택가능 single이면 한개씩만 선택가능 
#height이 0이면 리스트를 전체보여주고 다른숫자면 숫자만큼의 리스트만보여주고 그 이상의 것은 위로올리거나 내리면서 볼수있다
listbox.insert(0,"첫번째") #앞에 0은 순서 리스트를 위에서 부터 0번째에 두겠다는의미 
listbox.insert(1,"두번째")
listbox.insert(2,"세번째")
listbox.insert(3,"네번째")  #여기서 3을 1로 바꾸면 "네번째"가 1번위치로가고 나머지가 한개씩 밀려난다
listbox.insert(END,"다섯번째") #END는 맨뒤에 두겠단 의미
listbox.pack()



def cmd():
    #갯수 확인
    print("리스트에는",listbox.size(),"개가 있다")
    #삭제
    listbox.delete(END) #리스트를 아래부터 삭제 ()안에를 0으로 하면 위에서부터 삭제이고 1을 넣으면 1번부분부터 삭제되면서 0번위치는 삭제되지않는다
    #갯수 확인
    print("리스트에는",listbox.size(),"개가 있다")
    #항목 확인
    
    print("1번부터 3번까지의 항목:", listbox.get(0,2)) # 0,1,2의 항목을 불러온다
    #선택된 항목 위치 확인
    print("선택된 항목의 index값 : ",listbox.curselection())
  
btn = Button(root, text="버튼", command = cmd)
btn.pack()

root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건