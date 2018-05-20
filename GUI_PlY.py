import point_Mod #point (position) and point modification
import playYard
import g_cmd
import copy
try:
    from tkinter import *
    from tkinter.filedialog import askopenfilename
    from tkinter.filedialog import asksaveasfile
except ImportError:
    from Tkinter import *
    from tkFileDialog.filedialog import askopenfilename


root = Tk()
jit_CMD = 'NULL'

position_lable = Label (root, text ='First String Position')
slope_lable = Label (root, text ='angle_ZX        angle_ZY        String')
position_x = Entry(root, width = 7)
position_y = Entry(root, width = 7)
position_z = Entry(root, width = 7)
angle_ZX = Entry(root, width = 10)
angle_ZY = Entry(root, width = 10)
string_number = Entry(root, width = 10)
duration = Entry(root, width = 10)
punch_mode = Entry(root, width = 10)
result_JIT = Text(root, width = 60, height = 20)



position_lable.grid(row = 2, column = 1, columnspan=6)
position_x.grid(row = 3, column = 1, pady=10)
position_y.grid(row = 3, column = 3, pady=10)
position_z.grid(row = 3, column = 5, pady=10)
slope_lable.grid(row = 4, column = 1, padx=10, pady=10, columnspan=6)
angle_ZX.grid(row = 5, column = 1, padx=10, pady=10)
angle_ZY.grid(row = 5, column = 3, padx=10, pady=10)
string_number.grid(row = 5, column = 5, padx=10, pady=10)
punch_mode.grid(row = 6, column = 3, padx=10, pady=10)
duration.grid(row = 6, column = 1, padx=10, pady=10)
result_JIT.grid(row = 3,  column = 8, padx=10, rowspan = 6, columnspan=7)

position_x.insert(0, '-494')
position_y.insert(0, '-149.09')
position_z.insert(0, '478')
angle_ZX.insert(0, '-66')
angle_ZY.insert(0, '0')
string_number.insert(0, '1')
duration.insert(0, '2')
punch_mode.insert(0, 'D')

def connection_button():     
    result_JIT.delete('1.0', END)
    result_JIT.insert(INSERT, "Currently under development")
    
def save_button():
    file_tabs = asksaveasfile(mode='w', defaultextension=".txt")
    if file_tabs:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
                file_tabs.write(jit_CMD)
            except:                     
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
    file_tabs.close()

def loadTB_button():
    global jit_CMD
     
    file_tabs = open(askopenfilename(), 'r')
    if file_tabs:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:                     
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
    tabs_bck = list(file_tabs.readlines())
    tabs = copy.deepcopy(tabs_bck)
    for t in list(tabs_bck):
        if t.find('|') == -1: 
            tabs.remove(t)
    for x in range(0, len(tabs)):
        temp= tabs[x]
        tabs[x] = temp[(temp.find('|-')+1): len(temp)]
       
      #  if x<4:
      #      temp= tabs[x]
      #      tabs[x] = temp[(temp.find('|-')+1): len(temp)]
      #      print(tabs[x])    
    file_tabs.close()
    first_point = point_Mod.point(float(position_x.get()), float(position_y.get()), float(position_z.get()), 0, 0, 0)  
    g_Inf = g_cmd.guitar_Info(prep_TABs(tabs), float(angle_ZX.get()), float(angle_ZY.get()), 10, punch_mode.get(), first_point, int(duration.get()))
    jit_CMD = playYard.play_TABs(g_Inf)
    
    result_JIT.delete('1.0', END)
    result_JIT.insert(INSERT, jit_CMD)
    

def prep_TABs(tabs):  #prepares your tabs (".tab") for translating into J-cmds. returns: list[1..4]( = strings) of lists( = tacts).
                    #Deletes all useless symbols and the first symbol '-' in every tact
                    #Better to save files in python's folder
    tacts = list()
    strings = list()
    
    for string_num in range(0, 4):
        string_counter = 0
        strings.append(list())
        while string_counter  < len(tabs):
            temp = tabs[string_num + string_counter]
            tacts.append(0)
            for x in range(0, len(temp)):
                if temp[x]=='|':
                    tacts.append(x+1)                            
            for x in range(0, len(tacts)-1):
                strings[string_num].append(temp[tacts[x]+1: tacts[x+1]-1])
            tacts = list()
            string_counter+=4 
            
    return strings
    
    
    

def main():

             
    root.title( 'PlayGround' )    # window parameters
    root.geometry( '800x400' )

   
    Button(root, text=' OPC UA connection ', command=connection_button).grid(row = 7, column = 4, columnspan=2, pady=10)
    Button(root, text = 'Load Tabs', command=loadTB_button).grid(row = 8, column = 1, columnspan=2, pady=10)
    Button(root, text = 'Save Tabs', command=save_button).grid(row = 8, column = 5, columnspan=2, pady=10)
    
    root.mainloop()
    


if __name__ == '__main__':
    main()
