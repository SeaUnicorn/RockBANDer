import helper #switch-case 
import math   #sin/cos
import PointMod #point (position) and point modification
import JitCom
import PlayYard
import PointMod
import copy
from tkinter import * 


root = Tk()

jit = StringVar()
jit.set('NONE')
FP = Label (root, text ='First String Position')
Another = Label (root, text ='angleZX        angleZY        String')
X = Entry(root, width = 7)
Y = Entry(root, width = 7)
Z = Entry(root, width = 7)

angleZX = Entry(root, width = 15)
angleZY = Entry(root, width = 15)

stringN= Entry(root, width = 15)

answer = Text(root, width = 40, height = 20)

FP.grid(row = 2, column = 1, columnspan=8)

X.grid(row = 3, column = 1, pady=10)
Y.grid(row = 3, column = 3, pady=10)
Z.grid(row = 3, column = 5, pady=10)

Another.grid(row = 4, column = 1, padx=10, pady=10, columnspan=9)

angleZX.grid(row = 5, column = 1, padx=10, pady=10)
angleZY.grid(row = 5, column = 3, padx=10, pady=10)
stringN.grid(row = 5, column = 5, padx=10, pady=10)
answer.grid(row = 7,  column = 1, padx=10, columnspan=9)

X.insert(0, '60')
Y.insert(0, '0')
Z.insert(0, '45')
angleZX.insert(0, '0')
angleZY.insert(0, '0')
stringN.insert(0, '2')

def button_clicked():
    answer.delete('1.0', END)
    FirstPoint = PointMod.point(float(X.get()), float(Y.get()), float(Z.get()), 0, 0, 0)
    PlayYard.Play(int(stringN.get()), float(angleZX.get()), float(angleZX.get()), 10, 'D', FirstPoint)
    f = open('jit.txt', 'r+')
    answer.insert(INSERT,f.read())
    f.close()
 

def main():

              # окно результата
    root.title( 'PlayGround' )    # окно пиложения
    root.geometry( '340x500' )
    Button( root, text=' Make JITS ', command=button_clicked). grid(row = 6, column = 2, columnspan=2, pady=10)
    
   
    
    
    
    
    root.mainloop()
    


if __name__ == '__main__':
    main()
