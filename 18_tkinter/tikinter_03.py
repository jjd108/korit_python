import tkinter

root = tkinter.Tk()
root.title("회원가입")
root.geometry("500x200")

id_label = tk.Label(root, text="아이디")
id_label.grid(row=0, column=0, padx=10)

id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=5)

#entry옆에 버튼 하나 만들고 해당 버튼 클릭시
#아이디 출력
#아이디 밑에 비밀번호도 똑같이 만드세요

root = tkinter.Tk()
root.title("아이디")
root.title("비밀번호")
root.geometry("500x200")

id_label =tk.label(root, text="아이디")
pasword_label =tk.label(root, text="비밀번호")




root.mainloop()