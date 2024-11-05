from tkinter import *
from tkinter import messagebox


# обробник події натискання кнопки "Завершити тест"
def elem_rez():
    messagebox.showinfo('Тест', 'Тест завершено.')
    root.destroy()


# функції при натисненні на кнопки "Зберегти відповідь"
# Radiobutton1
def result():
    if var.get() == 2:
        b1['bg'] = 'pale green'
    else:
        b1['bg'] = 'red'
    b1['state'] = 'disabled'


# Radiobutton2
def result1():
    if var0.get() == 2:
        b2['bg'] = 'pale green'
    else:
        b2['bg'] = 'red'
    b2['state'] = 'disabled'


# CheckButton
def result2():
    if var2.get() == 1 and var4.get() == 1 and var5.get() == 1:
        b3['bg'] = 'pale green'
    else:
        b3['bg'] = 'red'
    b3['state'] = 'disabled'


# створення головного вікна форми
root = Tk()
root.title('Актуалізація поточних знань PYTON')
root.geometry('400x1000')  # геометричні параметри вікна форми

# розміщення елементів для введення особистих даних
L1 = Label(root, text="Прізвище ім'я")
L2 = Label(root, text="Група")
e1 = Entry(root)
e2 = Entry(root)
L_R0 = Label(root, text="")
L1.pack()  # метод розміщення елемента керування на формі
e1.pack()
L2.pack()
e2.pack()
L_R0.pack()

# групування елементів першого питання на фреймі 1
frame1 = Frame(root, bg="ivory3", bd=5, relief='groove')
label1 = Label(frame1, text='1.Функція, що визначає належність аргументу до вказаного типу:')
var = IntVar()
var.set(1)  # метод встановлення значення параметра
rad1 = Radiobutton(frame1, text="type()", variable=var, value=1)
rad2 = Radiobutton(frame1, text="isinstance()", variable=var, value=2)
rad3 = Radiobutton(frame1, text="format()", variable=var, value=3)
b1 = Button(frame1, text="Зберегти відповідь", state="active", bg="ivory4", command=result)
frame1.pack()
label1.pack()
rad1.pack()
rad2.pack()
rad3.pack()
b1.pack()

L_R1 = Label(root, text="")
L_R1.pack()

# групування елементів другого питання на фреймі 2
frame2 = Frame(root, bg="ivory3", bd=5, relief='groove')
label2 = Label(frame2, text='2.Функція, що розбиває рядок по роздільнику:')
var0 = IntVar()
var0.set(1)  # метод встановлення значення параметра
rad11 = Radiobutton(frame2, text="s.find()", variable=var0, value=1)
rad22 = Radiobutton(frame2, text="s.split()", variable=var0, value=2)
rad33 = Radiobutton(frame2, text="s.join()", variable=var0, value=3)
rad44 = Radiobutton(frame2, text="s.zfill()", variable=var0, value=4)
b2 = Button(frame2, text="Зберегти відповідь", state="active", bg="ivory4", command=result1)
frame2.pack()
label2.pack()
rad11.pack()
rad22.pack()
rad33.pack()
rad44.pack()
b2.pack()

L_R2 = Label(root, text="")
L_R2.pack()

# групування елементів третього питання на фреймі 3
frame3 = Frame(root, bg="ivory3", bd=5, relief='groove')
label3 = Label(frame3, text='3.Серед поданих значень оберіть ідентифікатори Pyton:')
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

check1 = Checkbutton(frame3, text='alpha', variable=var1, onvalue=1, offvalue=0)
check2 = Checkbutton(frame3, text='lambda ', variable=var2, onvalue=1, offvalue=0)
check3 = Checkbutton(frame3, text='global', variable=var3, onvalue=1, offvalue=0)
check4 = Checkbutton(frame3, text='enter ', variable=var4, onvalue=1, offvalue=0)
check5 = Checkbutton(frame3, text='except ', variable=var5, onvalue=1, offvalue=0)
b3 = Button(frame3, text="Зберегти відповідь", state="active", bg="ivory4", command=result2)
frame3.pack()
label3.pack()
check1.pack()
check2.pack()
check3.pack()
check4.pack()
check5.pack()
b3.pack()

L_R3 = Label(root, text="")
L_R3.pack()
# групування елементів четвертого питання на фреймі 4
frame4 = Frame(root, bg="ivory3", bd=5)
label4 = Label(frame4, text='4.Чим list відрізняється від set? Дайте розгорнуту відповідь.')
text1 = Text(frame4, height=10, width=35, font='ubuntu 12', wrap=WORD, bd=5)
frame4.pack()
label4.pack()
text1.pack()

L_R4 = Label(root, text="")
L_R4.pack()
# кнопка завершення тестування
button1 = Button(root, text='Завершити тест', bg="ivory3", width=20, height=3, font='ubuntu 10', command=elem_rez)
button1.pack()
# запуск головного циклу обробника форми
root.mainloop()

