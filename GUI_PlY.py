import helper #switch-case 
import math   #sin/cos
import PointMod #point (position) and point modification
import JitCom
import PlayYard
import copy
try:
    from tkinter import *
    from tkinter.filedialog import askopenfilename
except ImportError:
    from Tkinter import *
    from tkFileDialog.filedialog import askopenfilename


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
mode = Entry(root, width = 10)
answer = Text(root, width = 60, height = 20)


FP.grid(row = 2, column = 1, columnspan=6)
X.grid(row = 3, column = 1, pady=10)
Y.grid(row = 3, column = 3, pady=10)
Z.grid(row = 3, column = 5, pady=10)
Another.grid(row = 4, column = 1, padx=10, pady=10, columnspan=6)
angleZX.grid(row = 5, column = 1, padx=10, pady=10)
angleZY.grid(row = 5, column = 3, padx=10, pady=10)
stringN.grid(row = 5, column = 5, padx=10, pady=10)
mode.grid(row = 6, column = 3, padx=10, pady=10)
answer.grid(row = 3,  column = 8, padx=10, rowspan = 6, columnspan=7)

X.insert(0, '60')
Y.insert(0, '0')
Z.insert(0, '45')
angleZX.insert(0, '0')
angleZY.insert(0, '0')
stringN.insert(0, '2')
mode.insert(0, 'D')

def button_clicked():
    answer.delete('1.0', END)
    f = open('jit.txt', 'w')        #open text-file for JITs
    FirstPoint = PointMod.point(float(X.get()), float(Y.get()), float(Z.get()), 0, 0, 0)
    jit = PlayYard.Play(int(stringN.get()), float(angleZX.get()), float(angleZY.get()), 10, mode.get(), FirstPoint, 0)
    
    answer.insert(INSERT, jit)
    f.write(jit)                     #writing JITs down to the file
    f.close()
    
def button2_clicked():      #Gamma
    answer.delete('1.0', END)
    answer.insert(INSERT, "Currently under development")
    
def load_clicked():
    ftabs = open(askopenfilename(), 'r')
    if ftabs:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            
    FirstPoint = PointMod.point(float(X.get()), float(Y.get()), float(Z.get()), 0, 0, 0)
    
    tabs = list(map(int, ftabs.readlines()))
    
    
    
    answer.delete('1.0', END)
    answer.insert(INSERT, PlayYard.TabsProc(tabs,  float(angleZX.get()), float(angleZY.get()), 10, mode.get(), FirstPoint))
    ftabs.close()

def loadTB_clicked():
    ftabs = open(askopenfilename(), 'r')
    if ftabs:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            

    
    tabsGP = list( ftabs.readlines())
    #tabsGP = [line.rstrip() for line in tabsGP]
    tabs = list(copy.deepcopy(tabsGP))
    for t in tabsGP:
        if t.find('|') == -1:
            tabs.remove(t)
    for x in range(0, len(tabs)):
        temp= tabs[x]
        tabs[x] = temp[(temp.find('|-')+1): len(temp)]

        if x<4:
            temp= tabs[x]
            tabs[x] = temp[(temp.find('|-')+1): len(temp)]
             # tabs[tabs.index(t)].remove([0])
            #else:
             # tabs[tabsGP.index(t)] = ( '|'+t)

    FirstPoint = PointMod.point(float(X.get()), float(Y.get()), float(Z.get()), 0, 0, 0)  
    PlayYard.PlayTabs(EasyWay(tabs), float(angleZX.get()), float(angleZY.get()), 10, mode.get(), FirstPoint)
    
    answer.delete('1.0', END)
    answer.insert(INSERT, PlayYard.PlayTabs(EasyWay(tabs), float(angleZX.get()), float(angleZY.get()), 10, mode.get(), FirstPoint))
    ftabs.close()

def EasyWay(obj):
    step = len(obj)/4
    tacts = list()
    strings = list()
    
    
        
    for y in range(0, 4):
        s = 0
        strings.append(list())
        while s < len(obj):
            temp = obj[y+s]
            print (temp)
            tacts.append(0)
            for x in range(0, len(temp)):
                if temp[x]=='|':
                    tacts.append(x+1)
                            
            for x in range(0, len(tacts)-1):
                strings[y].append(temp[tacts[x]+1: tacts[x+1]-1])
            tacts = list()
            s = s+4

    for y in range(0, len(strings)):
        for x in range(0, len(strings[y])):
            print(strings[y][x])
        print('\n')
    return strings
    
    
    

def main():

             
    root.title( 'PlayGround' )    # window parameters
    root.geometry( '800x400' )
    #PlayYard.Load(float(angleZX.get()), float(angleZY.get()), N, 'D', PointMod.point(float(X.get()), float(Y.get()), float(Z.get()), 0, 0, 0))
    Button( root, text=' Make JITS ', command=button_clicked). grid(row = 7, column = 1, columnspan=2, pady=10)
    Button( root, text=' PVI connection ', command=button2_clicked). grid(row = 7, column = 4, columnspan=2, pady=10)
    Button (root, text = 'Load Tabs', command = load_clicked). grid (row = 8, column = 1, columnspan=2, pady=10)
    Button (root, text = 'Load Tabs GP', command = loadTB_clicked). grid (row = 8, column = 5, columnspan=2, pady=10)
    root.mainloop()
    


if __name__ == '__main__':
    main()
