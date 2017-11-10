import helper #switch-case 
import math   #sin/cos
import PointMod #point (position) and point modification
import JitCom
import PlayYard
import copy
from tkinter import * 


root = Tk()

jit = 'NONE'
FP = Label (root, text ='First String Position')
Another = Label (root, text ='angleZX        angleZY        String')
X = Entry(root, width = 7)
Y = Entry(root, width = 7)
Z = Entry(root, width = 7)
angleZX = Entry(root, width = 10)
angleZY = Entry(root, width = 10)
stringN= Entry(root, width = 10)
answer = Text(root, width = 50, height = 20)

FP.grid(row = 2, column = 1, columnspan=6)
X.grid(row = 3, column = 1, pady=10)
Y.grid(row = 3, column = 3, pady=10)
Z.grid(row = 3, column = 5, pady=10)
Another.grid(row = 4, column = 1, padx=10, pady=10, columnspan=6)
angleZX.grid(row = 5, column = 1, padx=10, pady=10)
angleZY.grid(row = 5, column = 3, padx=10, pady=10)
stringN.grid(row = 5, column = 5, padx=10, pady=10)
answer.grid(row = 3,  column = 8, padx=10, rowspan = 5, columnspan=7)

X.insert(0, '60')
Y.insert(0, '0')
Z.insert(0, '45')
angleZX.insert(0, '0')
angleZY.insert(0, '0')
stringN.insert(0, '2')

def button_clicked():
    answer.delete('1.0', END)
    f = open('jit.txt', 'w')        #open text-file for JITs
    FirstPoint = PointMod.point(float(X.get()), float(Y.get()), float(Z.get()), 0, 0, 0)
    jit = PlayYard.Play(int(stringN.get()), float(angleZX.get()), float(angleZX.get()), 10, 'D', FirstPoint)
    
    answer.insert(INSERT, jit)
    f.write(jit)                     #writing JITs down to the file
    f.close()
    
def button2_clicked():      #Gamma
    N = 10
    answer.delete('1.0', END)
    f = open('jit.txt', 'w')        #open text-file for JITs
    jit = 'N'+str(N) + ' LOOP'
    FirstPoint = PointMod.point(float(X.get()), float(Y.get()), float(Z.get()), 0, 0, 0)
    for x in range(1,5):
        jit = jit + PlayYard.Play(x, float(angleZX.get()), float(angleZY.get()), N, 'D', FirstPoint)
    for x in range(5, 0, -1):
        jit = jit + PlayYard.Play(x, float(angleZX.get()), float(angleZY.get()), N, 'U', FirstPoint)
    jit = jit + 'N'+str(N) + ' ENDLOOP'
    answer.insert(INSERT, jit)
    f.write(jit)         #writing JITs down to the file
    f.close()

def main():

             
    root.title( 'PlayGround' )    # window parameters
    root.geometry( '700x400' )
    #PlayYard.Load(float(angleZX.get()), float(angleZY.get()), N, 'D', PointMod.point(float(X.get()), float(Y.get()), float(Z.get()), 0, 0, 0))
    Button( root, text=' Make JITS ', command=button_clicked). grid(row = 6, column = 1, columnspan=2, pady=10)
    Button( root, text=' Make Gamma ', command=button2_clicked). grid(row = 6, column = 4, columnspan=2, pady=10)
    root.mainloop()
    


if __name__ == '__main__':
    main()
