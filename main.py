from random import randint
from tkinter import *

def main():    
    g=3
    bb=0
    cc=0
    for i in range(g):        
        def prg():
            b=bb
            c=cc
            t = ["rock", "paper", "scissor"]
            computer = t[randint(0,2)]
            player=inputtxt.get(1.0,"end-1c")
            if player == computer:
                
                lbl=Label(a,text='Tie  your_point:%s  computer_point:%s' %(b,c))
                lbl.pack()
                

            elif player == "rock":
                if computer == "paper":
                    
                    b=b-1
                    c=c+1
                    
                    lbl=Label(a,text='You_loose  your_point:%s  computer_point:%s' %(b,c))
                    lbl.pack()                   

                else:
                    b=b+1
                    c=c-1
                    
                    lbl=Label(a,text='You_win  your_point:%s  computer_point:%s' %(b,c))
                    lbl.pack()

            elif player == "paper":
                if computer == "scissor":
                    
                    b=b-1
                    c=c+1
                   
                    lbl=Label(a,text='You_loose  your_point:%s  computer_point:%s' %(b,c))
                    lbl.pack()
                    
                else:
                    
                    b=b+1
                    c=c-1
                    
                    lbl=Label(a,text='You_win  your_point:%s  computer_point:%s' %(b,c))
                    lbl.pack()

            elif player == "scissor":
                if computer == "rock":
                    
                    b=b-1
                    c=c+1
                    
                    lbl=Label(a,text='You_loose  your_point:%s  computer_point:%s' %(b,c))
                    lbl.pack()
                    

                else:
                    
                    b=b+1
                    c=c-1
                    
                    lbl=Label(a,text='You_win  your_point:%s  computer_point:%s' %(b,c))
                    lbl.pack()
                    

            else:
               
                lbl=Label(a,text='Check spelling  your_point:%s  computer_point:%s' %(b,c))
                lbl.pack()
            a.update_idletasks()
                
    printbutton=Button(a,text='print',command=prg)
    printbutton.pack()

    lbl = Label(a, text = "")
    lbl.pack()

    #a.update_idletasks()
            #player was set to True, but we want it to be False so the loop continues
            
            
        
    #set player to True
        


a=Tk()
a.title('Rock Paper Scissor')
a.geometry('400x200')
lbl=Label(a,text='rock, paper, scissor?')
lbl.pack()

inputtxt=Text(a,height=1,width=14)
inputtxt.pack()


main()

a.mainloop()
