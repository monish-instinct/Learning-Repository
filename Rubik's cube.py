import twophase.solver  as sv
import pyperclip
from tkinter import messagebox
from tkinter import *
import socket
import twophase.face
import twophase.cubie as cubie
c=[]
DEFAULT_HOST = 'localhost'
DEFAULT_PORT = '8080'
width = 60  
facelet_id = [[[0 for col in range(3)] for row in range(3)] for face in range(6)]
colorpick_id = [0 for i in range(6)]
curcol = None
b=None
t = ("U", "R", "F", "D", "L", "B")
cols = ("yellow", "green", "red", "white", "blue", "orange")
def show_text(txt):
    """Display messages."""
    display.insert(INSERT, txt)
    d=root.update_idletasks()


def create_facelet_rects(a):
    offset = ((1, 0), (2, 1), (1, 1), (1, 2), (0, 1), (3, 1))
    for f in range(6):
        for row in range(3):
            y = 10 + offset[f][1] * 3 * a + row * a
            for col in range(3):
                x = 10 + offset[f][0] * 3 * a + col * a
                facelet_id[f][row][col] = canvas.create_rectangle(x, y, x + a, y + a, fill="grey")
                if row == 1 and col == 1:
                    canvas.create_text(x + width // 2, y + width // 2, font=("", 14), text=t[f], state=DISABLED)
    for f in range(6):
        canvas.itemconfig(facelet_id[f][1][1], fill=cols[f])


def create_colorpick_rects(a):
    """Initialize the "paintbox" on the canvas."""
    global curcol
    global cols
    for i in range(6):
        x = (i % 3)*(a+5) + 7*a
        y = (i // 3)*(a+5) + 7*a
        colorpick_id[i] = canvas.create_rectangle(x, y, x + a, y + a, fill=cols[i])
        canvas.itemconfig(colorpick_id[0], width=4)
        curcol = cols[0]


def get_definition_string():
    color_to_facelet = {}
    for i in range(6):
        color_to_facelet.update({canvas.itemcget(facelet_id[i][1][1], "fill"): t[i]})
    s = ''
    for f in range(6):
        for row in range(3):
            for col in range(3):
                s += color_to_facelet[canvas.itemcget(facelet_id[f][row][col], "fill")]
    return s

def click(event):
    global curcol
    global b
    idlist = canvas.find_withtag('current')
    if len(idlist) > 0:
        if idlist[0] in colorpick_id:
            curcol = canvas.itemcget('current','fill')
            for i in range(6):
                canvas.itemconfig(colorpick_id[i], width=1)
            canvas.itemcget('current', '')
        else:
            canvas.itemconfig('current',fill=curcol)
        b=''
        if curcol=='yellow':
            b='y'
            c.append(b)
        elif curcol=='red':
            b='r'
            c.append(b)
        elif curcol=='blue':
           b='b'
           c.append(b)
        elif curcol=='orange':
           b='o'
           c.append(b)
        elif curcol=='green':
          b='g'
          c.append(b)
        elif curcol=='white':
          b='w'
          c.append(b)
        show_text(b)
def final():
    p=''
    global c
    global b
    global ans
    global q
    for i in c:
        p+=i
    b=list(p)
    for i in range(len(b)):

        if 'y' in b[i]:
            b[i]='U'

        if 'b' in b[i]:
            b[i]='L'

        if 'r' in b[i]:
            b[i]='F'

        if 'g' in b[i]:
            b[i]='R'

        if 'o' in b[i]:
            b[i]='B'

        if 'w' in b[i]:
            b[i]='D'
    w=''
    for l in b:
        w+=l
    print(w)
    q=[]

    cubestring = w
    ans=sv.solve(cubestring)
    print(ans)
    list(ans)
    a=ans.replace(' ','')
    b=list(a)

    for i in range(0,len(b)-3,2):

        d=b[i]+b[i+1]
        q.append(d)
    q.pop()

    for j in range(len(q)):
        if 'U1' in q[j]:
            q[j]=1

        elif 'U2' in q[j]:
            q[j]=2

        elif 'U3' in q[j]:
            q[j]=3

        elif 'R1' in q[j]:
            q[j]=4

        elif 'R2' in q[j]:
            q[j]=5

        elif 'R3' in q[j]:
            q[j]=6

        elif 'F1' in q[j]:
            q[j]=7

        elif 'F2' in q[j]:
            q[j]=8

        elif 'F3' in q[j]:
            q[j]=9

        elif 'D1' in q[j]:
            q[j]=10

        elif 'D2' in q[j]:
            q[j]=11

        elif 'D3' in q[j]:
            q[j]=12

        elif 'L1' in q[j]:
            q[j]=13

        elif 'L2' in q[j]:
            q[j]=14

        elif 'L3' in q[j]:
            q[j]=15

        elif 'B1' in q[j]:
            q[j]=16

        elif 'B2' in q[j]:
            q[j]=17

        elif 'B3' in q[j]:
            q[j]=18
    c=str(q)
    b=c.replace('[','{')
    d=b.replace(']','}')
    q='int s_array[]='
    w=';'
    z=q+d+w
    def emp():
        pyperclip.copy(z)

    window=Tk()
    window.configure(width=800,height=150)

    command = lambda: [emp(),window.destroy()]

    button=Button(window,text='Copy',height=1,borderwidth=2,relief='solid',width=5,\
                     activebackground='azure2',command=command,cursor='hand2')
    button.place(x=400,y=100)

    namelbl=Label(window,text=ans,borderwidth=2,width=100,height=2,relief='solid')
    namelbl.place(x=50,y=20)


    

root = Tk()
root.wm_title('Color Input')
canvas = Canvas(root, width=12 * width + 20, height=9 * width + 20)
canvas.pack()

display = Text(height=7, width=39)
text_window = canvas.create_window(10 + 6.5 * width, 10 + .5 * width, anchor=NW, window=display)

command = lambda: [final(), root.destroy()]
button=Button(root,text='>>> ',height=1,borderwidth=2,relief='solid',width=5,activebackground='azure2',command=command,cursor='hand2')
button.place(x=650,y=500)
    
canvas.bind("<Button-1>", click)
create_facelet_rects(width)
create_colorpick_rects(width)
root.mainloop()



