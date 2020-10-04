import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect("fdbms.db")
cursor = conn.cursor()
def exot():
    exit(0)
#insering into club
def insertClub():
    
    def saveClub():
        cursor.execute('INSERT INTO CLUBS VALUES(?,?,?,?,?,?,?,?)',(cEntry0.get(),cEntry1.get(),cEntry2.get(),cEntry3.get(),cEntry4.get(),cEntry5.get(),cEntry6.get(),cEntry7.get()))
        conn.commit()
        messagebox.showinfo("Success!","Insertion successful!",command=insertData())
        ()
    clubWindow = Tk()
    clubWindow.title("Insert Club data")
    clubWindow.geometry("750x750")
    clubLabel = Label(clubWindow, text="Enter Club details:",anchor=CENTER,font=("helvetica",25,"bold"))
    clubInsert = Button(clubWindow, text="INSERT",width=20,height=2,command=saveClub,bg="white",fg="BLACK",font=("bold"))
    clubExit = Button(clubWindow,text="BACK",width=20,height=2,command=clubWindow.destroy,fg="red",bg="black",font=("bold"))
    
    
    cLabel0 = Label(clubWindow,text="Club ID",fg="red",font=("bold"))
    cLabel1 = Label(clubWindow,text="Club Name",fg="red",font=("bold"))
    cLabel2 = Label(clubWindow,text="Rating",fg="red",font=("bold"))
    cLabel3 = Label(clubWindow,text="Manager",fg="red",font=("bold"))
    cLabel4 = Label(clubWindow,text="Chairman",fg="red",font=("bold"))
    cLabel5 = Label(clubWindow,text="League",fg="red",font=("bold"))
    cLabel6 = Label(clubWindow,text="Titles",fg="red",font=("bold"))
    cLabel7 = Label(clubWindow,text="Year Founded",fg="red",font=("bold"))
    
    cEntry0 = Entry(clubWindow, bd =5)
    cEntry1 = Entry(clubWindow, bd =5)
    cEntry2 = Entry(clubWindow, bd =5)
    cEntry3 = Entry(clubWindow, bd =5)
    cEntry4 = Entry(clubWindow, bd =5)
    cEntry5 = Entry(clubWindow, bd =5)
    cEntry6 = Entry(clubWindow, bd =5)
    cEntry7 = Entry(clubWindow, bd =5)
    
    cLabel0.grid(row=0,column=0,padx=100,pady=10)
    cLabel1.grid(row=1,column=0,padx=100,pady=10)
    cLabel2.grid(row=2,column=0,padx=100,pady=10)
    cLabel3.grid(row=3,column=0,padx=100,pady=10)
    cLabel4.grid(row=4,column=0,padx=100,pady=10)
    cLabel5.grid(row=5,column=0,padx=100,pady=10)
    cLabel6.grid(row=6,column=0,padx=100,pady=10)
    cLabel7.grid(row=7,column=0,padx=100,pady=10)

    cEntry0.grid(row=0,column=1,pady=10)
    cEntry1.grid(row=1,column=1,pady=10)
    cEntry2.grid(row=2,column=1,pady=10)
    cEntry3.grid(row=3,column=1,pady=10)
    cEntry4.grid(row=4,column=1,pady=10)
    cEntry5.grid(row=5,column=1,pady=10)
    cEntry6.grid(row=6,column=1,pady=10)
    cEntry7.grid(row=7,column=1,pady=10)
    clubInsert.grid(row=8,column=0,pady=50)
    clubExit.grid(row=8,column=1,padx=50,pady=50,columnspan=2)
    clubWindow.mainloop()


#insert into agents
def insertAgent():
    
    def saveAgent():
        cursor.execute('INSERT INTO AGENTS VALUES(?,?,?)',(aEntry0.get(),aEntry1.get(),aEntry2.get()))
        conn.commit()
        messagebox.showinfo("Success!","Insertion successful!")
        ()
   
    
    agentWindow = Tk()
    agentWindow.title("Insert Agent data")
    agentWindow.geometry("750x750")
    agentLabel = Label(agentWindow, text="Enter Agent details:",anchor=CENTER,font=("helvetica",25,"bold"))
    agentInsert = Button(agentWindow, text="INSERT",width=20,height=2,command=saveAgent,bg="white",fg="BLACK",font=("bold"))
    agentExit = Button(agentWindow,text="BACK",width=20,height=2,command=agentWindow.destroy,fg="red",bg="black",font=("bold"))
    
    aLabel0 = Label(agentWindow,text="Agent Name",fg="red",font=("bold"))
    aLabel1 = Label(agentWindow,text="Nationality",fg="red",font=("bold"))
    aLabel2 = Label(agentWindow,text="Rating",fg="red",font=("bold"))
    
    aEntry0 = Entry(agentWindow, bd =5)
    aEntry1 = Entry(agentWindow, bd =5)
    aEntry2 = Entry(agentWindow, bd =5)
    
    aLabel0.grid(row=0,column=0,padx=100,pady=10)
    aLabel1.grid(row=1,column=0,padx=100,pady=10)
    aLabel2.grid(row=2,column=0,padx=100,pady=10)
    
    aEntry0.grid(row=0,column=1,pady=10)
    aEntry1.grid(row=1,column=1,pady=10)
    aEntry2.grid(row=2,column=1,pady=10)
    
    agentInsert.grid(row=3,column=0,pady=50)
    agentExit.grid(row=3,column=1,padx=50,pady=50,columnspan=2)

    

    agentWindow.mainloop()





#insert into nationals
def insertNational():
    
    def saveNational():
        cursor.execute('INSERT INTO NATIONALS VALUES(?,?,?,?)',(nEntry0.get(),nEntry1.get(),nEntry2.get(),nEntry3.get()))
        conn.commit()
        nationalWindow.destroy()
        messagebox.showinfo("Success!","Insertion successful!")
        ()
        
    nationalWindow = Tk()
    nationalWindow.title("Insert National Team data")
    nationalWindow.geometry("750x750")
    nationalLabel = Label(nationalWindow, text="Enter National Team details:",anchor=CENTER,font=("helvetica",25,"bold"))
    nationalInsert = Button(nationalWindow, text="INSERT",width=20,height=2,command=saveNational,bg="white",fg="BLACK",font=("bold"))
   
    nationalExit = Button(nationalWindow,text="BACK",width=20,height=2,command=nationalWindow.destroy,fg="red",bg="black",font=("bold"))
   
    
    nLabel0 = Label(nationalWindow,text="Nation",fg="red",font=("bold"))
    nLabel1 = Label(nationalWindow,text="Manager",fg="red",font=("bold"))
    nLabel2 = Label(nationalWindow,text="World Cups won",fg="red",font=("bold"))
    nLabel3 = Label(nationalWindow,text="Rating",fg="red",font=("bold"))
    
    nEntry0 = Entry(nationalWindow, bd =5)
    nEntry1 = Entry(nationalWindow, bd =5)
    nEntry2 = Entry(nationalWindow, bd =5)
    nEntry3 = Entry(nationalWindow, bd =5)

    nLabel0.grid(row=0,column=0,padx=100,pady=10)
    nLabel1.grid(row=1,column=0,padx=100,pady=10)
    nLabel2.grid(row=2,column=0,padx=100,pady=10)
    nLabel3.grid(row=3,column=0,padx=100,pady=10)
    
    nEntry0.grid(row=0,column=1,pady=10)
    nEntry1.grid(row=1,column=1,pady=10)
    nEntry2.grid(row=2,column=1,pady=10)
    nEntry3.grid(row=3,column=1,pady=10)
    
    nationalInsert.grid(row=4,column=0,pady=50)
    nationalExit.grid(row=4,column=1,padx=50,pady=50,columnspan=2)
   
    nationalWindow.mainloop()
#insert into players
def insertPlayer():
    
    def savePlayer():
        cursor.execute('INSERT INTO PLAYERS VALUES(?,?,?,?,?,?,?,?,?)',(pEntry0.get(),pEntry1.get(),pEntry2.get(),pEntry3.get(),pEntry4.get(),pEntry5.get(),pEntry6.get(),pEntry7.get(),pEntry8.get()))
        conn.commit()
        messagebox.showinfo("Success!","Insertion successful!")
        ()
    playerWindow = Tk()
    playerWindow.title("Insert Player data")
    playerWindow.geometry("750x750")
    playerLabel = Label(playerWindow, text="Enter Player details:",anchor=CENTER,fg="red",font=("helvetica",25,"bold"))
    playerInsert = Button(playerWindow, text="INSERT",width=20,height=2,command=savePlayer,bg="white",fg="BLACK",font=("bold"))
    playerExit = Button(playerWindow,text="BACK",width=20,height=2,command=playerWindow.destroy,fg="red",bg="black",font=("bold"))
    

    pLabel0 = Label(playerWindow,text="First Name",fg="red",font=("bold"))
    pLabel1 = Label(playerWindow,text="Last Name",fg="red",font=("bold"))
    pLabel2 = Label(playerWindow,text="Nationality",fg="red",font=("bold"))
    pLabel3 = Label(playerWindow,text="Club Name",fg="red",font=("bold"))
    pLabel4 = Label(playerWindow,text="Age",fg="red",font=("bold"))
    pLabel5 = Label(playerWindow,text="Years At Club",fg="red",font=("bold"))
    pLabel6 = Label(playerWindow,text="Agent Name",fg="red",font=("bold"))
    pLabel7 = Label(playerWindow,text="Rating",fg="red",font=("bold"))
    pLabel8 = Label(playerWindow,text="Position",fg="red",font=("bold"))


    pEntry0 = Entry(playerWindow, bd =5)
    pEntry1 = Entry(playerWindow, bd =5)
    pEntry2 = Entry(playerWindow, bd =5)
    pEntry3 = Entry(playerWindow, bd =5)
    pEntry4 = Entry(playerWindow, bd =5)
    pEntry5 = Entry(playerWindow, bd =5)
    pEntry6 = Entry(playerWindow, bd =5)
    pEntry7 = Entry(playerWindow, bd =5)
    pEntry8 = Entry(playerWindow, bd =5)
    
    pLabel0.grid(row=0,column=0,padx=100,pady=10)
    pLabel1.grid(row=1,column=0,padx=100,pady=10)
    pLabel2.grid(row=2,column=0,padx=100,pady=10)
    pLabel3.grid(row=3,column=0,padx=100,pady=10)
    pLabel4.grid(row=4,column=0,padx=100,pady=10)
    pLabel5.grid(row=5,column=0,padx=100,pady=10)
    pLabel6.grid(row=6,column=0,padx=100,pady=10)
    pLabel7.grid(row=7,column=0,padx=100,pady=10)
    pLabel8.grid(row=8,column=0,padx=100,pady=10)

    pEntry0.grid(row=0,column=1,pady=10)
    pEntry1.grid(row=1,column=1,pady=10)
    pEntry2.grid(row=2,column=1,pady=10)
    pEntry3.grid(row=3,column=1,pady=10)
    pEntry4.grid(row=4,column=1,pady=10)
    pEntry5.grid(row=5,column=1,pady=10)
    pEntry6.grid(row=6,column=1,pady=10)
    pEntry7.grid(row=7,column=1,pady=10)
    pEntry8.grid(row=8,column=1,pady=10)

    playerInsert.grid(row=9,column=0,pady=30)
    playerExit.grid(row=9,column=1,padx=50,pady=30,columnspan=2)
    playerWindow.mainloop()


#defining data disp window

def insertData():
    insertWindow = Tk()
    insertWindow.title("Insert data")
    insertWindow.geometry("550x550")
    insertLabel = Label(insertWindow, text="Which table to enter data into?",anchor=CENTER,font=("helvetica",25,"bold"))
    insertButton1 = Button(insertWindow,text="CLUBS",width=20,height=2,command=insertClub,bg="white",fg="BLACK",font=("bold"))
    insertButton2 = Button(insertWindow,text="AGENTS",width=20,height=2,command=insertAgent,bg="white",fg="BLACK",font=("bold"))
    insertButton3 = Button(insertWindow,text="NATIONAL TEAM",width=20,height=2,command=insertNational,bg="white",fg="BLACK",font=("bold"))
    insertButton4 = Button(insertWindow,text="PLAYERS",width=20,height=2,command=insertPlayer,bg="white",fg="BLACK",font=("bold"))
    insertExit = Button(insertWindow,text="BACK",width=20,height=2,command=insertWindow.destroy,bg="black",fg="red",font=("bold"))
    insertLabel.pack(fill=X,anchor=CENTER)
    insertButton1.pack(anchor=CENTER,pady=20)
    insertButton2.pack(anchor=CENTER,pady=20)
    insertButton3.pack(anchor=CENTER,pady=20)
    insertButton4.pack(anchor=CENTER,pady=20)
    insertExit.pack(anchor=CENTER,pady=20)
    ()
    insertWindow.mainloop()




#defining view data window
def viewalldata():
        def viewNation():
            def allNation():
                    class ScrolledFrame(Frame):

                                def __init__(self, parent, vertical=True, horizontal=False):
                                    super().__init__(parent)

                                    #self._canvas = tk.Canvas(self)
                                    self._canvas = Canvas(self,height=700,width=1200)
                                    self._canvas.grid(row=0, column=0)

                                    self._vertical_bar = Scrollbar(self, orient="vertical", command=self._canvas.yview)
                                    if vertical:
                                        self._vertical_bar.grid(row=0, column=1, sticky="ns")
                                    self._canvas.configure(yscrollcommand=self._vertical_bar.set)

                                    self._horizontal_bar = Scrollbar(self, orient="horizontal", command=self._canvas.xview)
                                    if horizontal:
                                        self._horizontal_bar.grid(row=1, column=0, sticky="we")
                                    self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

                                    self.frame = Frame(self._canvas)
                                    self._canvas.create_window((0, 0), window=self.frame, anchor="nw")

                                    self.frame.bind("<Configure>", self.resize)

                                def resize(self, event=None): 
                                    self._canvas.configure(scrollregion=self._canvas.bbox("all"))

                            # --- functions ---

                    def display_nation(master, data):

                                headers = [
                                   ("Nation", 10),
                                   ("Manager", 10),
                                   ("World Cups Won", 10),
                                   ("Rating", 10),
                                ]

                                # create row with headers
                                for col, (header, size) in enumerate(headers):
                                    l = Label(master, text=header, width=size,fg="red",font=("helvetica",25,"bold"))
                                    l.grid(row=0, column=col)

                                # create rows with players
                                for row, nation in enumerate(data, 1):
                                    for col in range(4):
                                        l = Label(master, text=nation[col],font=("bold"))
                                        l.grid(row=row, column=col)

                            # --- main ---

                            # - create random data for test -

                            #import random
                            #import string

                            #data = []
                            #for rows in range(20):
                            #    row = []
                            #    for cols in range(9):
                            #        row.append(random.choice(string.ascii_letters))
                            #    data.append(row)

                            # - start -

                    root = Tk()

                            # ---

                            # create scrolled frame with vertical and horizontal scrollbar
                    sf = ScrolledFrame(root, True, True) 
                    sf.pack()

                            # you  have to use `sf.frame` as parent for widgets
                    cursor.execute("SELECT * from NATIONALS order by nation")
                    data=cursor.fetchall()
            
                    display_nation(sf.frame, data)

                    root.mainloop()

            
            
            
            
            def displayNation(data):
                master = Tk()
                master.geometry('500x500')
                master.title('All Nations')
                Label1 = Label(master, text="Nation", width=10,fg="red",font=("helvetica",25,"bold"))
                Label1.grid(row=0, column=0)
                Label2 = Label(master, text="Manager", width=10,fg="red",font=("helvetica",25,"bold"))
                Label2.grid(row=0, column=1)
                Label3 = Label(master, text="World Cups Won", width=10,fg="red",font=("helvetica",25,"bold"))
                Label3.grid(row=0, column=2)
                Label4 = Label(master, text="Rating", width=10,fg="red",font=("helvetica",25,"bold"))
                Label4.grid(row=0, column=3)
                
                
        
                for index, dat in enumerate(data):
                        Label(master, text=dat[0],font=("bold")).grid(row=index+1, column=0)
                        Label(master, text=dat[1],font=("bold")).grid(row=index+1, column=1)
                        Label(master, text=dat[2],font=("bold")).grid(row=index+1, column=2)
                        Label(master, text=dat[3],font=("bold")).grid(row=index+1, column=3)
            

            def nameNation():
                def searchName3():
                        cursor.execute('select * from  NATIONALS  where Nation  like ?',(nEntry.get()+'%',))
                        data=cursor.fetchall()
                        displayNation(data)
                            
                name=Tk()
                name.title("Search Nation name")
                name.geometry("750x750")
                nameLabel = Label(name, text="Enter a Nation Name",anchor=CENTER,font=("helvetica",25,"bold"))
                name1 = Label(name,text="Nation Name",font=("bold"))
                name1.grid(row=2,column=0,padx=100,pady=20)
                nEntry = Entry(name, bd =5)
                nEntry.grid(row=2,column=2,pady=20)
                print(nEntry.get())
                nameSearch = Button(name, text="SEARCH",width=20,height=2,command=searchName3,bg="white",fg="BLACK",font=("bold"))
                nameSearch.grid(row=5,column=0,pady=30)
                
                nameExit = Button(name,text="BACK",width=20,height=2,command=name.destroy,fg="red",bg="black",font=("bold"))
                nameExit.grid(row=5,column=2,padx=50,pady=30,columnspan=2)
                
                name.mainloop()
            def manNation():
                def searchManager():
                        cursor.execute('select * from  NATIONALS  where MANAGER  like ?',(nEntry.get()+'%',))
                        data=cursor.fetchall()
                        displayNation(data)
                            
                name=Tk()
                name.title("Search Nation name")
                name.geometry("750x750")
                nameLabel = Label(name, text="Enter Manager",anchor=CENTER,font=(None,20,"bold"))
                name1 = Label(name,text="Manager",font=("bold"))
                name1.grid(row=2,column=0,padx=100,pady=20)
                nEntry = Entry(name, bd =5)
                nEntry.grid(row=2,column=2,pady=20)
                print(nEntry.get())
                nameSearch = Button(name, text="SEARCH",width=20,height=2,command=searchManager,bg="white",fg="BLACK",font=("bold"))
                nameSearch.grid(row=5,column=0,pady=30)
                
                nameExit = Button(name,text="BACK",width=20,height=2,command=name.destroy,fg="red",bg="black",font=("bold"))
                nameExit.grid(row=5,column=2,padx=50,pady=30,columnspan=2)
                
                name.mainloop()
            def ratingNation():
                def searchRating():
                        cursor.execute('select * from  NATIONALS  where RATING BETWEEN ? AND ?',(nEntry1.get(),nEntryy.get()))
                        data=cursor.fetchall()
                        displayNation(data)
                            
                name=Tk()
                name.title("Search by rating")
                name.geometry("750x750")
                nameLabel = Label(name, text="Rating of NAtion",anchor=CENTER,font=("helvetica",25,"bold"))
                name1 = Label(name,text="Minimum",fg="red",font=("bold"))
                name1.grid(row=2,column=0,padx=100,pady=20)
                name2 = Label(name,text="Maximum",fg="red",font=("bold"))
                name2.grid(row=3,column=0,padx=100,pady=20)
                nEntry = Entry(name, bd =5)
                nEntry.grid(row=2,column=2,pady=20)
                nEntryy = Entry(name, bd =5)
                nEntryy.grid(row=3,column=2,pady=20)
                nameSearch = Button(name, text="SEARCH",width=20,height=2,command=searchRating,bg="white",fg="BLACK",font=("bold"))
                nameSearch.grid(row=5,column=0,pady=30)
                nameExit = Button(name,text="BACK",width=20,height=2,command=name.destroy,fg="red",bg="black",font=("bold"))
                nameExit.grid(row=5,column=2,padx=50,pady=30,columnspan=2)
                
                name.mainloop()
 #defining viewing window
            Nation = Tk()
            Nation.title("Search Nation")
            Nation.geometry("750x750")
            viewLabel = Label(Nation, text="Which data?",anchor=CENTER,font=(None,20,"bold")).pack()
            NationButton1 = Button(Nation,text="ALL",width=20,height=2,command=allNation,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=25)
            NationButton2 = Button(Nation,text="Nation Name",width=20,height=2,command=nameNation,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=25)
            NationButton3 = Button(Nation,text="Manager",width=20,height=2,command=manNation,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=25)
            NationButton5 = Button(Nation,text="Rating",width=20,height=2,command=ratingNation,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=25)
            NationExit = Button(Nation,text="BACK",width=20,height=2,command=Nation.destroy,fg="red",bg="black",font=("bold")).pack(anchor=CENTER,pady=25)
        
            


        def viewPlayer():
            def allPlayer():
                    class ScrolledFrame(Frame):

                        def __init__(self, parent, vertical=True, horizontal=False):
                            super().__init__(parent)

                            
                            self.columnconfigure(0, weight=1) # changed
                            self.rowconfigure(0, weight=1) # changed
                            self._canvas = Canvas(self,height=1200,width=1500)
                            self._canvas.grid(row=0, column=0)

                            self._vertical_bar = Scrollbar(self, orient="vertical", command=self._canvas.yview)
                            if vertical:
                                self._vertical_bar.grid(row=0, column=1, sticky="nw")
                            self._canvas.configure(yscrollcommand=self._vertical_bar.set)

                            self._horizontal_bar = Scrollbar(self, orient="horizontal", command=self._canvas.xview)
                            if horizontal:
                                self._horizontal_bar.grid(row=1, column=0, sticky="we")
                            self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

                            self.frame = Frame(self._canvas)
                            self._canvas.create_window((0, 0), window=self.frame, anchor="nw")

                            self.frame.bind("<Configure>", self.resize)

                        def resize(self, event=None): 
                            self._canvas.configure(scrollregion=self._canvas.bbox("all"))

                    # --- functions ---

                    def display_players(master, data):
                            
                        headers = [
                           ("First Name", 20),
                           ("Last Name", 20),
                           ("Nationality", 20),
                           ("Club", 20),
                           ("Age", 10),
                           ("Years at Club", 10),
                           ("Agent", 20),
                           ("Rating", 10),
                           ("Position", 10),
                        ]

                        # create row with headers
                        for col, (header, size) in enumerate(headers):
                            l = Label(master, text=header, width=size,fg="red",font=("helvetica",25,"bold"))
                            l.grid(row=0, column=col)

                        # create rows with players
                        for row, player in enumerate(data, 1):
                            for col in range(9):
                                l = Label(master, text=player[col],font=("bold"))
                                l.grid(row=row, column=col)

                    # --- main ---

                    # - create random data for test -

                    #import random
                    #import string

                    #data = []
                    #for rows in range(20):
                    #    row = []
                    #    for cols in range(9):
                    #        row.append(random.choice(string.ascii_letters))
                    #    data.append(row)

                    # - start -

                    root = Tk()
                    root.geometry("1000x1000")
                    # ---

                    # create scrolled frame with vertical and horizontal scrollbar
                    sf = ScrolledFrame(root, True, True)
                    
                    sf.pack(fill='both', expand=True)
                    
                    #sf.frame.geometry("1000x1000")
                    # you  have to use `sf.frame` as parent for widgets
                    cursor.execute("SELECT * from Players")
                    data=cursor.fetchall()
            
                    display_players(sf.frame, data)

                    root.mainloop()

            def displayPlayer(data):
                
                master = Tk()
                master.geometry('750x750')
                master.title('All Players')
                Label1 = Label(master, text="First Name", width=20,fg="red",font=("helvetica",25,"bold"))
                Label1.grid(row=0, column=0)
                Label2 = Label(master, text="Last Name", width=20,fg="red",font=("helvetica",25,"bold"))
                Label2.grid(row=0, column=1)
                Label3 = Label(master, text="Nationality", width=20,fg="red",font=("helvetica",25,"bold"))
                Label3.grid(row=0, column=2)
                Label4 = Label(master, text="Club", width=20,fg="red",font=("helvetica",25,"bold"))
                Label4.grid(row=0, column=3)
                Label5 = Label(master, text="Age", width=10,fg="red",font=("helvetica",25,"bold"))
                Label5.grid(row=0, column=4)
                Label6 = Label(master, text="Years at Club", width=10,fg="red",font=("helvetica",25,"bold"))
                Label6.grid(row=0, column=5)
                Label7 = Label(master, text="Agent", width=20,fg="red",font=("helvetica",25,"bold"))
                Label7.grid(row=0, column=6)
                Label8 = Label(master, text="Rating", width=10,fg="red",font=("helvetica",25,"bold"))
                Label8.grid(row=0, column=7)
                Label9 = Label(master, text="Position", width=10,fg="red",font=("helvetica",25,"bold"))
                Label9.grid(row=0, column=8)
                
        
                for index, dat in enumerate(data):
                        Label(master, text=dat[0],font=("bold")).grid(row=index+1, column=0)
                        Label(master, text=dat[1],font=("bold")).grid(row=index+1, column=1)
                        Label(master, text=dat[2],font=("bold")).grid(row=index+1, column=2)
                        Label(master, text=dat[3],font=("bold")).grid(row=index+1, column=3)
                        Label(master, text=dat[4],font=("bold")).grid(row=index+1, column=4)
                        Label(master, text=dat[5],font=("bold")).grid(row=index+1, column=5)
                        Label(master, text=dat[6],font=("bold")).grid(row=index+1, column=6)
                        Label(master, text=dat[7],font=("bold")).grid(row=index+1, column=7)
                        Label(master, text=dat[8],font=("bold")).grid(row=index+1, column=8)
            def namePlayer():
                def searchName4():
                        cursor.execute('select * from  Players  where first_name  like ? OR last_name like ?',(nEntry.get()+'%',nEntry.get()+'%'))
                        data=cursor.fetchall()
                        displayPlayer(data)
                            
                name=Tk()
                name.title("Search Player name")
                name.geometry("750x750")
                nameLabel = Label(name, text="Enter a Player Name",anchor=CENTER,font=("helvetica",25,"bold"))
                name1 = Label(name,text="Player Name",fg="red",font=("bold"))
                name1.grid(row=2,column=0,padx=100,pady=20)
                nEntry = Entry(name, bd =5)
                nEntry.grid(row=2,column=2,pady=20)
                print(nEntry.get())
                nameSearch = Button(name, text="SEARCH",width=20,height=2,command=searchName4,bg="white",fg="BLACK",font=("bold"))
                nameSearch.grid(row=5,column=0,pady=30)
                
                nameExit = Button(name,text="BACK",width=20,height=2,command=name.destroy,fg="red",bg="black",font=("bold"))
                nameExit.grid(row=5,column=2,padx=50,pady=30,columnspan=2)
                
                name.mainloop()
            def clubPlayer():
                def searchPclub():
                        cursor.execute('select * from  Players  where club__name  like ?',(nEntry.get()+'%',))
                        data=cursor.fetchall()
                        displayPlayer(data)
                            
                name=Tk()
                name.title("Search Club")
                name.geometry("750x750")
                nameLabel = Label(name, text="Enter Club",anchor=CENTER,font=("helvetica",20,"bold"))
                name1 = Label(name,text="Club Name",fg="red",font=("bold"))
                name1.grid(row=2,column=0,padx=100,pady=20)
                nEntry = Entry(name, bd =5)
                nEntry.grid(row=2,column=2,pady=20)
                print(nEntry.get())
                nameSearch = Button(name, text="SEARCH",width=20,height=2,command=searchPclub,bg="white",fg="BLACK",font=("bold"))
                nameSearch.grid(row=5,column=0,pady=30)
                
                nameExit = Button(name,text="BACK",width=20,height=2,command=name.destroy,fg="red",bg="black",font=("bold"))
                nameExit.grid(row=5,column=2,padx=50,pady=30,columnspan=2)
                
                name.mainloop()
            def ratingPlayer():
                def searchRating():
                        cursor.execute('select * from  Players  where RATING BETWEEN ? AND ?  AND POSITION LIKE ?',(nEntry1.get(),nEntry2.get(),nEntry3.get()))
                        data=cursor.fetchall()
                        displayPlayer(data)
                            
                name=Tk()
                name.title("Search Rating")
                name.geometry("750x750")
                nameLabel = Label(name, text="Enter Rating & Position",anchor=CENTER,font=("helvetica",25,"bold"))
                name1 = Label(name,text="Minimum",fg="red",font=("bold"))
                name1.grid(row=2,column=0,padx=100,pady=20)
                name2 = Label(name,text="Maximum",fg="red",font=("bold"))
                name2.grid(row=3,column=0,padx=100,pady=20)
                name3 = Label(name,text="Position",fg="red",font=("bold"))
                name3.grid(row=4,column=0,padx=100,pady=20)
                nEntry1 = Entry(name, bd =5)
                nEntry1.grid(row=2,column=1,pady=20)
                nEntry2 = Entry(name, bd =5)
                nEntry2.grid(row=3,column=1,pady=20)
                nEntry3 = Entry(name, bd =5)
                nEntry3.grid(row=4,column=1,pady=20)
                print(nEntry1.get())
                print(nEntry2.get())
                print(nEntry3.get())
                nameSearch = Button(name, text="SEARCH",width=20,height=2,command=searchRating,bg="white",fg="BLACK",font=("bold"))
                nameSearch.grid(row=5,column=0,pady=30)
                
                nameExit = Button(name,text="BACK",width=20,height=2,command=name.destroy,fg="red",bg="black",font=("bold"))
                nameExit.grid(row=5,column=1,padx=50,pady=30,columnspan=2)
                
                name.mainloop()

            def nationPlayer():
                def searchNation():
                        cursor.execute('select * from  Players  where Nationality LIKE ? ',(nEntry.get()+'%',))
                        data=cursor.fetchall()
                        displayPlayer(data)
                            
                name=Tk()
                name.title("Search Nation")
                name.geometry("600x600")
                nameLabel = Label(name, text="Enter Nation",anchor=CENTER,font=("helvetica",20,"bold"))
                name1 = Label(name,text="Nation",fg="red",font=("bold"))
                name1.grid(row=2,column=0,padx=100,pady=20)
                nEntry = Entry(name, bd =5)
                nEntry.grid(row=2,column=2,pady=20)
                print(nEntry.get())
                
                nameSearch = Button(name, text="SEARCH",width=20,height=2,command=searchNation,bg="white",fg="BLACK",font=("bold"))
                nameSearch.grid(row=5,column=0,pady=30)
                
                nameExit = Button(name,text="BACK",width=20,height=2,command=name.destroy,fg="red",bg="black",font=("bold"))
                nameExit.grid(row=5,column=2,padx=50,pady=30,columnspan=2)
                
                name.mainloop()                
                
            def agentPlayer():
                def searchAgent():
                        cursor.execute('select * from  Players  where AGENT_NAME LIKE ? ',(nEntry.get()+'%',))
                        data=cursor.fetchall()
                        displayPlayer(data)
                            
                name=Tk()
                name.title("Search Agent")
                name.geometry("750x750")
                nameLabel = Label(name, text="Enter Agent",anchor=CENTER,font=("helvetica",20,"bold"))
                name1 = Label(name,text="Agent",fg="red",font=("bold"))
                name1.grid(row=2,column=0,padx=100,pady=20)
                nEntry = Entry(name, bd =5)
                nEntry.grid(row=2,column=2,pady=20)
                print(nEntry.get())
                
                nameSearch = Button(name, text="SEARCH",width=20,height=2,command=searchAgent,bg="white",fg="BLACK",font=("bold"))
                nameSearch.grid(row=5,column=0,pady=30)
                
                nameExit = Button(name,text="BACK",width=20,height=2,command=name.destroy,fg="red",bg="black",font=("bold"))
                nameExit.grid(row=5,column=2,padx=50,pady=30,columnspan=2)
                
                name.mainloop()     
#defining viewing window
            Player = Tk()
            Player.geometry("750x750")
            viewLabel = Label(Player, text="Which data?",anchor=CENTER,font=(None,20,"bold")).pack()
            PlayerButton1 = Button(Player,text="ALL",width=20,height=2,command=allPlayer,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=15)
            PlayerButton2 = Button(Player,text="Player Name",width=20,height=2,command=namePlayer,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=15)
            PlayerButton3 = Button(Player,text="Club",width=20,height=2,command=clubPlayer,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=15)
            PlayerButton4 = Button(Player,text="Nation",width=20,height=2,command=nationPlayer,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=15)
            PlayerButton4 = Button(Player,text="Agent",width=20,height=2,command=agentPlayer,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=15)
            PlayerButton6 = Button(Player,text="Rating & Position",width=20,height=2,command=ratingPlayer,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=15)
            PlayerExit = Button(Player,text="BACK",width=20,height=2,command=Player.destroy,fg="red",bg="black",font=("bold")).pack(anchor=CENTER,pady=15)


        def viewAgent():
            def ratingAgent():
                def searchArating():
                    cursor.execute('select * from agents where rating between ? AND ?',(nEntry.get(),nEntryy.get()))
                    data=cursor.fetchall()
                    master = Tk()
                    master.geometry('500x500')
                    master.title('AGENTS')
                    Label1 = Label(master, text="NAME", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label1.grid(row=0, column=0)
                    Label2 = Label(master, text="NATIONALITY", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label2.grid(row=0, column=1)
                    Label3 = Label(master, text="RATING", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label3.grid(row=0, column=2)
          
                
        
                    for index, dat in enumerate(data):
                        Label(master, text=dat[0],font=("bold")).grid(row=index+1, column=0)
                        Label(master, text=dat[1],font=("bold")).grid(row=index+1, column=1)
                        Label(master, text=dat[2],font=("bold")).grid(row=index+1, column=2)

                name=Tk()
                name.title("Search by rating")
                name.geometry("750x750")
                nameLabel = Label(name, text="Rating of the agent",anchor=CENTER,font=("helvetica",25,"bold"))
                name1 = Label(name,text="Minimum Rating",fg="red",font=("bold"))
                name1.grid(row=2,column=0,padx=100,pady=20)
                name2 = Label(name,text="Maximum Rating",fg="red",font=("bold"))
                name2.grid(row=3,column=0,padx=100,pady=20)
                nEntry = Entry(name, bd =5)
                nEntry.grid(row=2,column=2,pady=20)
                nEntryy = Entry(name, bd =5)
                nEntryy.grid(row=3,column=2,pady=20)
                nameSearch = Button(name, text="SEARCH",width=20,height=2,command=searchArating,bg="white",fg="BLACK",font=("bold"))
                nameSearch.grid(row=5,column=0,pady=30)
                nameExit = Button(name,text="BACK",width=20,height=2,command=name.destroy,fg="red",bg="black",font=("bold"))
                nameExit.grid(row=5,column=2,padx=50,pady=30,columnspan=2)
                
                name.mainloop()

            def naAgent():
                def searchNname():
                    cursor.execute('select * from agents where nationality  like ? order by name',(nEntry.get()+'%',))
                    data=cursor.fetchall()
                    master = Tk()
                    master.geometry('500x500')
                    master.title('AGENTS')
                    Label1 = Label(master, text="NAME", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label1.grid(row=0, column=0)
                    Label2 = Label(master, text="NATIONALITY", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label2.grid(row=0, column=1)
                    Label3 = Label(master, text="RATING", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label3.grid(row=0, column=2)
          
                
        
                    for index, dat in enumerate(data):
                        Label(master, text=dat[0],font=("bold")).grid(row=index+1, column=0)
                        Label(master, text=dat[1],font=("bold")).grid(row=index+1, column=1)
                        Label(master, text=dat[2],font=("bold")).grid(row=index+1, column=2)
                name=Tk()
                name.title("Agent")
                name.geometry("750x750")
                nameLabel = Label(name, text="Enter NAtionality",anchor=CENTER,font=("helvetica",25,"bold"))
                name1 = Label(name,text="Nationality",fg="red",font=("bold"))
                name1.grid(row=2,column=0,padx=100,pady=20)
                nEntry = Entry(name, bd =5)
                nEntry.grid(row=2,column=2,pady=20)
                print(nEntry.get())
                nameSearch = Button(name, text="SEARCH",width=20,height=2,command=searchNname,bg="white",fg="BLACK",font=("bold"))
                nameSearch.grid(row=5,column=0,pady=30)
               
                
                nameExit = Button(name,text="BACK",width=20,height=2,command=name.destroy,fg="red",bg="black",font=("bold"))
                nameExit.grid(row=5,column=2,padx=50,pady=30,columnspan=2)
                
                name.mainloop()
            def nameAgent():
                def searchAname():
                    cursor.execute('select * from agents where name  like ? order by name',(nEntry.get()+'%',))
                    data=cursor.fetchall()
                    master = Tk()
                    master.geometry('500x500')
                    master.title('AGENTS')
                    Label1 = Label(master, text="NAME", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label1.grid(row=0, column=0)
                    Label2 = Label(master, text="NATIONALITY", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label2.grid(row=0, column=1)
                    Label3 = Label(master, text="RATING", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label3.grid(row=0, column=2)
          
                
        
                    for index, dat in enumerate(data):
                        Label(master, text=dat[0],font=("bold")).grid(row=index+1, column=0)
                        Label(master, text=dat[1],font=("bold")).grid(row=index+1, column=1)
                        Label(master, text=dat[2],font=("bold")).grid(row=index+1, column=2)
                name=Tk()
                name.title("Agent Name")
                name.geometry("750x750")
                nameLabel = Label(name, text="Enter Agent Name",anchor=CENTER,font=('Helvetica',20,"bold"))
                name1 = Label(name,text="Agent Name",fg="red",font=("bold"))
                name1.grid(row=2,column=0,padx=100,pady=20)
                nEntry = Entry(name, bd =5)
                nEntry.grid(row=2,column=2,pady=20)
                print(nEntry.get())
                nameSearch = Button(name, text="SEARCH",width=20,height=2,command=searchAname,bg="white",fg="BLACK",font=("bold"))
                nameSearch.grid(row=5,column=0,pady=30)
               
                
                nameExit = Button(name,text="BACK",width=20,height=2,command=name.destroy,fg="red",bg="black",font=("bold"))
                nameExit.grid(row=5,column=2,padx=50,pady=30,columnspan=2)
                
                name.mainloop()
            def allAgent():
                class ScrolledFrame(Frame):

                        def __init__(self, parent, vertical=True, horizontal=False):
                            super().__init__(parent)

                            #self._canvas = tk.Canvas(self)
                            self._canvas = Canvas(self,height=700,width=1200)
                            self._canvas.grid(row=0, column=0)

                            self._vertical_bar = Scrollbar(self, orient="vertical", command=self._canvas.yview)
                            if vertical:
                                self._vertical_bar.grid(row=0, column=1, sticky="ns")
                            self._canvas.configure(yscrollcommand=self._vertical_bar.set)

                            self._horizontal_bar = Scrollbar(self, orient="horizontal", command=self._canvas.xview)
                            if horizontal:
                                self._horizontal_bar.grid(row=1, column=0, sticky="we")
                            self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

                            self.frame = Frame(self._canvas)
                            self._canvas.create_window((0, 0), window=self.frame, anchor="nw")

                            self.frame.bind("<Configure>", self.resize)

                        def resize(self, event=None): 
                            self._canvas.configure(scrollregion=self._canvas.bbox("all"))

                    # --- functions ---

                def display_agents(master, data):

                        headers = [
                           ("Name", 20),
                           ("Nationality", 10),
                           ("Rating", 10),
                        ]

                        # create row with headers
                        for col, (header, size) in enumerate(headers):
                            l = Label(master, text=header, width=size,fg="red",font=('Helvetica',25,"bold"))
                            l.grid(row=0, column=col)

                        # create rows with players
                        for row, agent in enumerate(data, 1):
                            for col in range(3):
                                l = Label(master, text=agent[col],font=("bold"))
                                l.grid(row=row, column=col)
                root = Tk()

                    # ---

                    # create scrolled frame with vertical and horizontal scrollbar
                sf = ScrolledFrame(root, True, True) 
                sf.pack()

                    # you  have to use `sf.frame` as parent for widgets
                cursor.execute("SELECT * from AGENTS order by name")
                data=cursor.fetchall()
                display_agents(sf.frame, data)
                root.mainloop()
                
            Agent = Tk()
            Agent.title("Agents")
            Agent.geometry("750x750")
            viewLabel = Label(Agent, text="Which data?",anchor=CENTER,fg="red",font=("helvetica",25,"bold")).pack()
            AgentButton1 = Button(Agent,text="ALL",width=20,height=2,command=allAgent,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=25)
            AgentButton2 = Button(Agent,text="Agent Name",width=20,height=2,command=nameAgent,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=25)
            AgentButton3 = Button(Agent,text="Nationality",width=20,height=2,command=naAgent,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=25)
            AgentButton5 = Button(Agent,text="Rating",width=20,height=2,command=ratingAgent,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=25)
            AgentExit = Button(Agent,text="BACK",width=20,height=2,command=Agent.destroy,fg="red",bg="black",font=("bold")).pack(anchor=CENTER,pady=25)


    
        def viewClub():
            def ratingClub():
                def searchRating():
                    cursor.execute('select * from clubs where club_rating between ? AND ?',(nEntry.get(),nEntryy.get()))
                    daata=cursor.fetchall()
                    master = Tk()
                    master.geometry('500x500')
                    master.title('CLUBS')
                    Label1 = Label(master, text="CLUB ID", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label1.grid(row=0, column=0)
                    Label2 = Label(master, text="CLUB NAME", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label2.grid(row=0, column=1)
                    Label3 = Label(master, text="RATING", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label3.grid(row=0, column=2)
                    Label1 = Label(master, text="MANAGER", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label1.grid(row=0, column=3)
                    Label1 = Label(master, text="CHAIRMAN", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label1.grid(row=0, column=4)
                    Label1 = Label(master, text="LEAGUE", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label1.grid(row=0, column=5)
                    Label1 = Label(master, text="TITLES", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label1.grid(row=0, column=6)
                    Label1 = Label(master, text="YEAR FOUNDED", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label1.grid(row=0, column=7)
                    
        
                    for index, dat in enumerate(daata):
                        Label(master, text=dat[0],font=("bold")).grid(row=index+1, column=0)
                        Label(master, text=dat[1],font=("bold")).grid(row=index+1, column=1)
                        Label(master, text=dat[2],font=("bold")).grid(row=index+1, column=2)
                        Label(master, text=dat[3],font=("bold")).grid(row=index+1, column=3)
                        Label(master, text=dat[4],font=("bold")).grid(row=index+1, column=4)
                        Label(master, text=dat[5],font=("bold")).grid(row=index+1, column=5)
                        Label(master, text=dat[6],font=("bold")).grid(row=index+1, column=6)
                        Label(master, text=dat[7],font=("bold")).grid(row=index+1, column=7)

                name=Tk()
                name.title("Search by rating")
                name.geometry("750x750")
                nameLabel = Label(name, text="Rating of the club",anchor=CENTER,font=("helvetica",25,"bold"))
                name1 = Label(name,text="Minimum",fg="red",font=("bold"))
                name1.grid(row=2,column=0,padx=100,pady=20)
                name2 = Label(name,text="Maximum",fg="red",font=("bold"))
                name2.grid(row=3,column=0,padx=100,pady=20)
                nEntry = Entry(name, bd =5)
                nEntry.grid(row=2,column=2,pady=20)
                nEntryy = Entry(name, bd =5)
                nEntryy.grid(row=3,column=2,pady=20)
                nameSearch = Button(name, text="SEARCH",width=20,height=2,command=searchRating,bg="white",fg="BLACK",font=("bold"))
                nameSearch.grid(row=5,column=0,pady=30)
                nameExit = Button(name,text="BACK",width=20,height=2,command=name.destroy,fg="red",bg="black",font=("bold"))
                nameExit.grid(row=5,column=2,padx=50,pady=30,columnspan=2)
                
                name.mainloop()

            def manClub():
                def searchMan():
                    cursor.execute('select * from clubs where club_manager  like ? order by club_name',(nEntry.get()+'%',))
                    daata=cursor.fetchall()
                    #return cursor.fetchall()
                
                    master = Tk()
                    master.geometry('500x500')
                    master.title('CLUBS')
                    Label1 = Label(master, text="CLUB ID", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label1.grid(row=0, column=0)
                    Label2 = Label(master, text="CLUB NAME", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label2.grid(row=0, column=1)
                    Label3 = Label(master, text="RATING", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label3.grid(row=0, column=2)
                    Label1 = Label(master, text="MANAGER", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label1.grid(row=0, column=3)
                    Label1 = Label(master, text="CHAIRMAN", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label1.grid(row=0, column=4)
                    Label1 = Label(master, text="LEAGUE", width=15,fg="red",font=('Helvetica',25,"bold"))
                    Label1.grid(row=0, column=5)
                    Label1 = Label(master, text="TITLES", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label1.grid(row=0, column=6)
                    Label1 = Label(master, text="YEAR FOUNDED", width=10,fg="red",font=('Helvetica',25,"bold"))
                    Label1.grid(row=0, column=7)
                    
        
                    for index, dat in enumerate(daata):
                        Label(master, text=dat[0],font=("bold")).grid(row=index+1, column=0)
                        Label(master, text=dat[1],font=("bold")).grid(row=index+1, column=1)
                        Label(master, text=dat[2],font=("bold")).grid(row=index+1, column=2)
                        Label(master, text=dat[3],font=("bold")).grid(row=index+1, column=3)
                        Label(master, text=dat[4],font=("bold")).grid(row=index+1, column=4)
                        Label(master, text=dat[5],font=("bold")).grid(row=index+1, column=5)
                        Label(master, text=dat[6],font=("bold")).grid(row=index+1, column=6)
                        Label(master, text=dat[7],font=("bold")).grid(row=index+1, column=7)

                name=Tk()
                name.title("Search Manager name")
                name.geometry("750x750")
                nameLabel = Label(name, text="Enter Manager Name",anchor=CENTER,font=("helvetica",25,"bold"))
                name1 = Label(name,text="Manager Name",fg="red",font=("bold"))
                name1.grid(row=2,column=0,padx=100,pady=20)
                nEntry = Entry(name, bd =5)
                nEntry.grid(row=2,column=2,pady=20)
                print(nEntry.get())
                nameSearch = Button(name, text="SEARCH",width=20,height=2,command=searchMan,bg="white",fg="BLACK",font=("bold"))
                nameSearch.grid(row=5,column=0,pady=30)
               
                
                nameExit = Button(name,text="BACK",width=20,height=2,command=name.destroy,fg="red",bg="black",font=("bold"))
                nameExit.grid(row=5,column=2,padx=50,pady=30,columnspan=2)
                
                name.mainloop()

            
            def allClub():
                    class ScrolledFrame(Frame):

                        def __init__(self, parent, vertical=True, horizontal=False):
                            super().__init__(parent)

                            #self._canvas = tk.Canvas(self)
                            self._canvas = Canvas(self,height=700,width=1200)
                            self._canvas.grid(row=0, column=0)

                            self._vertical_bar = Scrollbar(self, orient="vertical", command=self._canvas.yview)
                            if vertical:
                                self._vertical_bar.grid(row=0, column=1, sticky="ns")
                            self._canvas.configure(yscrollcommand=self._vertical_bar.set)

                            self._horizontal_bar = Scrollbar(self, orient="horizontal", command=self._canvas.xview)
                            if horizontal:
                                self._horizontal_bar.grid(row=1, column=0, sticky="we")
                            self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

                            self.frame = Frame(self._canvas)
                            self._canvas.create_window((0, 0), window=self.frame, anchor="nw")

                            self.frame.bind("<Configure>", self.resize)

                        def resize(self, event=None): 
                            self._canvas.configure(scrollregion=self._canvas.bbox("all"))

                    # --- functions ---

                    def display_clubs(master, data):

                        headers = [
                           ("Club ID", 10),
                           ("Club Name", 10),
                           ("Rating", 10),
                           ("Manager", 10),
                           ("Chairman", 10),
                           ("League", 15),
                           ("Titles Won", 10),
                           ("Year founded", 10),
                        ]

                        # create row with headers
                        for col, (header, size) in enumerate(headers):
                            l = Label(master, text=header, width=size,fg="red",font=('Helvetica',25,"bold"))
                            l.grid(row=0, column=col)

                        # create rows with players
                        for row, club in enumerate(data, 8):
                            for col in range(8):
                                l = Label(master, text=club[col],font=("bold"))
                                l.grid(row=row, column=col)

                    # --- main ---

                    # - create random data for test -

                    #import random
                    #import string

                    #data = []
                    #for rows in range(20):
                    #    row = []
                    #    for cols in range(9):
                    #        row.append(random.choice(string.ascii_letters))
                    #    data.append(row)

                    # - start -

                    root = Tk()

                    # ---

                    # create scrolled frame with vertical and horizontal scrollbar
                    sf = ScrolledFrame(root, True, True) 
                    sf.pack()

                    # you  have to use `sf.frame` as parent for widgets
                    cursor.execute("SELECT * from CLUBS order by club_name")
                    data=cursor.fetchall()
            
                    display_clubs(sf.frame, data)

                    root.mainloop()

            def nameClub():
               
                    

                def searchName():
                        cursor.execute('select * from clubs where club_name  like ? order by club_name',(nEntry.get()+'%',))
                        dataa=cursor.fetchall()
                        names=Tk()
                        names.geometry('500x500')
                        names.title('Search Display')
                        Label1 = Label(names, text="CLUB ID", width=10,fg="red",font=('Helvetica',25,"bold"))
                        Label1.grid(row=0, column=0)
                        Label2 = Label(names, text="CLUB Name", width=10,fg="red",font=('Helvetica',25,"bold"))
                        Label2.grid(row=0, column=1)
                        Label3 = Label(names, text="RATING", width=10,fg="red",font=('Helvetica',25,"bold"))
                        Label3.grid(row=0, column=2)
                        Label1 = Label(names, text="MANAGER", width=10,fg="red",font=('Helvetica',25,"bold"))
                        Label1.grid(row=0, column=3)
                        Label1 = Label(names, text="CHAIRMAN", width=10,fg="red",font=('Helvetica',25,"bold"))
                        Label1.grid(row=0, column=4)
                        Label1 = Label(names, text="LEAGUE", width=15,fg="red",font=('Helvetica',25,"bold"))
                        Label1.grid(row=0, column=5)
                        Label1 = Label(names, text="TITLES", width=10,fg="red",font=('Helvetica',25,"bold"))
                        Label1.grid(row=0, column=6)
                        Label1 = Label(names, text="YEAR FOUNDED", fg="red",width=10,font=('Helvetica',25,"bold"))
                        Label1.grid(row=0, column=7)
                        
                        for index, dat in enumerate(dataa):
                            Label(names, text=dat[0],font=("bold")).grid(row=index+1, column=0)
                            Label(names, text=dat[1],font=("bold")).grid(row=index+1, column=1)
                            Label(names, text=dat[2],font=("bold")).grid(row=index+1, column=2)
                            Label(names, text=dat[3],font=("bold")).grid(row=index+1, column=3)
                            Label(names, text=dat[4],font=("bold")).grid(row=index+1, column=4)
                            Label(names, text=dat[5],font=("bold")).grid(row=index+1, column=5)
                            Label(names, text=dat[6],font=("bold")).grid(row=index+1, column=6)
                            Label(names, text=dat[7],font=("bold")).grid(row=index+1, column=7)
                
                name=Tk()
                name.title("Search Club name")
                name.geometry("550x550")
                nameLabel = Label(name, text="Enter a Club Name",anchor=CENTER,font=('Helvetica',25,"bold"))
                name1 = Label(name,text="Club Name",fg="red",font=("bold"))
                name1.grid(row=2,column=0,padx=100,pady=20)
                nEntry = Entry(name, bd =5)
                nEntry.grid(row=2,column=2,pady=20)
                print(nEntry.get())
                nameSearch = Button(name, text="SEARCH",width=20,height=2,command=searchName,bg="white",fg="BLACK",font=("bold"))
                nameSearch.grid(row=5,column=0,pady=30)
               
                
                nameExit = Button(name,text="BACK",width=20,height=2,command=name.destroy,fg="red",bg="black",font=("bold"))
                nameExit.grid(row=5,column=2,padx=50,pady=30,columnspan=2)
                
                name.mainloop()

 
 #defining viewing window
            club = Tk()
            club.geometry("750x750")
            viewLabel = Label(club, text="Which data?",anchor=CENTER,font=("helvetica",25,"bold")).pack()
            clubButton1 = Button(club,text="ALL",width=20,height=2,command=allClub,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=25)
            clubButton2 = Button(club,text="Club Name",width=20,height=2,command=nameClub,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=25)
            clubButton3 = Button(club,text="Manager",width=20,height=2,command=manClub,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=25)
            clubButton5 = Button(club,text="Rating",width=20,height=2,command=ratingClub,bg="white",fg="BLACK",font=("bold")).pack(anchor=CENTER,pady=25)
            clubExit = Button(club,text="BACK",width=20,height=2,command=club.destroy,fg="red",bg="black",font=("bold")).pack(anchor=CENTER,pady=25)


        viewWindow = Tk()
        viewWindow.title("view data")
        viewWindow.geometry("600x600")
        viewLabel = Label(viewWindow, text="Which data to look into?",anchor=CENTER,font=('Helvetica',25,"bold"))
        viewButton1 = Button(viewWindow,text="CLUBS",width=20,height=2,command=viewClub,bg="white",fg="BLACK",font=("bold"))
        viewButton2 = Button(viewWindow,text="AGENTS",width=20,height=2,command=viewAgent,bg="white",fg="BLACK",font=("bold"))
        viewButton3 = Button(viewWindow,text="NATIONAL TEAM",width=20,height=2,bg="white",fg="BLACK",font=("bold"),command=viewNation)
        viewButton4 = Button(viewWindow,text="PLAYERS",width=20,height=2,bg="white",fg="BLACK",font=("bold"),command=viewPlayer)
        viewExit = Button(viewWindow,text="BACK",width=20,height=2,command=viewWindow.destroy,bg="black",fg="red",font=("bold"))
    
        viewLabel.pack(fill=X,anchor=CENTER)
        viewButton1.pack(anchor=CENTER,pady=25)
        viewButton2.pack(anchor=CENTER,pady=25)
        viewButton3.pack(anchor=CENTER,pady=25)
        viewButton4.pack(anchor=CENTER,pady=25)    
        viewExit.pack()




def mainPage():
    mWindow = Tk()
    mWindow.configure(background="white")
    mWindow.title("Choose option")
    mWindow.geometry("750x750")
    MLabel1 = Label(mWindow, text="What would you like to do?",anchor=CENTER,font=("helvetica",25,"bold"))
    MButton1 = Button(mWindow,text="Insert data",width=10,height=2,command=insertData,bg="white",fg="BLACK",font=("bold"))
    MButton2 = Button(mWindow,text="View all data",width=10,height=2,command=viewalldata,bg="white",fg="BLACK",font=("bold"))
    MExit = Button(mWindow,text="Exit",width=10,height=2,command=exot,fg="red",bg="black",font=("bold"))
    
    MLabel1.pack(fill=X,anchor=CENTER)
    MButton1.pack(side=LEFT,anchor=SW)
    MButton2.pack(side=RIGHT,anchor=SE)
    MExit.pack(side=BOTTOM,anchor=S)
    mWindow.mainloop()


def login():
   
    root = Toplevel()
    root.title("Log In")
    root.configure(bg="white")
    root.geometry("500x500")
    
    
    
    def abcde():
        if E1.get() == 'abc' and E2.get() == 'def':
            messagebox.showinfo("Success","Logged in")
            root.destroy()
            frontpage.destroy()
            mainPage()
        else:
             messagebox.showinfo("Failure","Incorrect info")
             
             root.destroy()

   
            
    L1 = Label(root, text="User Name",font=("bold"))
    L1.config(bg="white")
    E1 = Entry(root, bd =5)
    L2 = Label(root, text="Password",font=("bold"))
    L2.config(bg="white")
    E2 = Entry(root, bd =5,show='*')
    B1=Button(root,text="Log In",width=10,height=1,command=abcde,font=("bold"))
    B2=Button(root,text="Exit",width=10,height=1,command=root.destroy,fg="red",bg="black",font=("bold"))

    L1.grid(row=0,column=0,padx=100,pady=100)
    E1.grid(row=0,column=1,pady=10,columnspan=2)
    L2.grid(row=1,column=0,pady=50)
    E2.grid(row=1,column=1,pady=50)
    B1.grid(row=3,column=0,pady=10)
    B2.grid(row=3,column=1,pady=10)
    
    
    root.mainloop()
    
    

frontpage = Tk()
frontpage.geometry("500x500")
frontpage.title("Start Page")
B = Label(frontpage, text ="Welcome to football database",font=("times", 16,"bold"),fg="red").pack()
from PIL import Image, ImageTk

image = Image.open('ab.jpg')
photo_image = ImageTk.PhotoImage(image)
label =Label(frontpage, image = photo_image)
label.pack()
button1 = Button(frontpage,text="Start",width=20,height=2,command=login,bg="white",fg="BLACK",font=("bold"))
button2 = Button(frontpage,text="Exit",width=20,height=2,command=exot,fg="red",bg="black",font=("bold"))
#B.pack(fill=X,anchor=CENTER)
button1.pack(side=LEFT,anchor=SW)
button2.pack(side=RIGHT,anchor=SE)
#frontpage.iconify()

frontpage.mainloop()        
    
