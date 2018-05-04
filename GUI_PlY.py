import helper #switch-case 
import math   #sin/cos
import PointMod #point (position) and point modification
import G_Com
import PlayYard
import copy
try:
    from tkinter import *
    from tkinter.filedialog import askopenfilename
    from tkinter.filedialog import asksaveasfile
except ImportError:
    from Tkinter import *
    from tkFileDialog.filedialog import askopenfilename


root = Tk()
G_CMD = 'NULL'

position_lable = Label (root, text ='First String Position')
slope_lable = Label (root, text ='angle_ZX        angle_ZY        String')
position_x = Entry(root, width = 7)
position_y = Entry(root, width = 7)
position_z = Entry(root, width = 7)
angle_ZX = Entry(root, width = 10)
angle_ZY = Entry(root, width = 10)
string_number= Entry(root, width = 10)
mode = Entry(root, width = 10)
answer = Text(root, width = 60, height = 20)


position_lable.grid(row = 2, column = 1, columnspan=6)
position_x.grid(row = 3, column = 1, pady=10)
position_y.grid(row = 3, column = 3, pady=10)
position_z.grid(row = 3, column = 5, pady=10)
slope_lable.grid(row = 4, column = 1, padx=10, pady=10, columnspan=6)
angle_ZX.grid(row = 5, column = 1, padx=10, pady=10)
angle_ZY.grid(row = 5, column = 3, padx=10, pady=10)
string_number.grid(row = 5, column = 5, padx=10, pady=10)
mode.grid(row = 6, column = 3, padx=10, pady=10)
answer.grid(row = 3,  column = 8, padx=10, rowspan = 6, columnspan=7)

position_x.insert(0, '60')
position_y.insert(0, '0')
position_z.insert(0, '45')
angle_ZX.insert(0, '-60')
angle_ZY.insert(0, '0')
string_number.insert(0, '1')
mode.insert(0, 'D')

def button_clicked():
    answer.delete('1.0', END)
    f = open('G_CMD.txt', 'w')        #open text-file for Gts
    FirstPoint = PointMod.point(float(position_x.get()), float(position_y.get()), float(position_z.get()), 0, 0, 0)
    G_CMD = PlayYard.Play(int(string_number.get()), float(angle_ZX.get()), float(angle_ZY.get()), 10, mode.get(), FirstPoint, 0)
    
    answer.insert(INSERT, G_CMD)
    f.write(G_CMD)                     #writing Gts down to the file
    f.close()
    
def button2_clicked():      #Gamma
    answer.delete('1.0', END)
    answer.insert(INSERT, "Currently under development")
    
def load_clicked():
    ftabs = asksaveasfile(mode='w', defaultextension=".txt")
    if ftabs:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
                ftabs.write(G_CMD)
            except:                     
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
    ftabs.close()

def loadTB_clicked():
    global G_CMD
    
    ftabs = open(askopenfilename(), 'r')
    if ftabs:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:                     
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            

    
    tabsGP = list( ftabs.readlines())
    
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
            

    FirstPoint = PointMod.point(float(position_x.get()), float(position_y.get()), float(position_z.get()), 0, 0, 0)  
    G_CMD = PlayYard.PlayTabs(PrepTABs(tabs), float(angle_ZX.get()), float(angle_ZY.get()), 10, mode.get(), FirstPoint)
    
    answer.delete('1.0', END)
    answer.insert(INSERT, G_CMD)
    ftabs.close()

def PrepTABs(obj):  #prepares your tabs (".tab") for translating into G-cmds. returns: list[1..4]( = strings) of lists( = tacts).
                    #Deletes all useless symbols and the first symbol '-' in every tact
                    #Better to save files in python's folder
    tacts = list()
    strings = list()
    
    for y in range(0, 4):
        s = 0
        strings.append(list())
        while s < len(obj):
            temp = obj[y+s]
            tacts.append(0)
            for x in range(0, len(temp)):
                if temp[x]=='|':
                    tacts.append(x+1)
                            
            for x in range(0, len(tacts)-1):
                strings[y].append(temp[tacts[x]+1: tacts[x+1]-1])
            tacts = list()
            s = s+4
    return strings
    
    
    

def main():

             
    root.title( 'PlayGround' )    # window parameters
    root.geometry( '800x400' )
    
    Button( root, text=' Make JITS ', command=button_clicked). grid(row = 7, column = 1, columnspan=2, pady=10)
    Button( root, text=' PVI connection ', command=button2_clicked). grid(row = 7, column = 4, columnspan=2, pady=10)
    Button (root, text = 'Load Tabs', command = loadTB_clicked). grid (row = 8, column = 1, columnspan=2, pady=10)
    Button (root, text = 'Save Tabs', command = load_clicked). grid (row = 8, column = 5, columnspan=2, pady=10)
    root.mainloop()
    


if __name__ == '__main__':
    main()
