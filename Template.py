from tkinter import *
from Object import * 
from DataAccessObject import *
from Traitement import Metiers

class TestTnm:
    __window = None
    __Patient = None
    __Organe = None
    __date = None
    __T = None
    __N = None
    __M = None
    __stade = None
    __frame = None
    __List_Button_tnm = None
    __Button_m1 = None
    __Button_m2 = None
    def __init__(self):
        AddPersonne()
        self.__window = Tk()
        self.__window.title("Cancer TNM")
        self.__window.geometry("425x500")
        self.__window.minsize(425,500)
        self.__window.maxsize(425,500)
        self.__window.config(background='#CFE3BC')

        #Titre 
        label1 = Label(self.__window, text="TNM Cancer",font=("ravie",10),background='#CFE3BC' ,fg='white')
        label5 = Label(self.__window,text="Teste Tnm",background='#CFE3BC')
        
        #Les Patient
        self.__Patient = StringVar()
        Label2 = Label(self.__window,text="Patient")
        personne =  Connexion().Find(Personne,"Personne")
        list_option1 = list()
        for i in personne:
            list_option1.append(i.get_nom()+"_id:"+str(i.get_id())+"")
        option = OptionMenu(self.__window, self.__Patient, *list_option1)

        #Organe tester
        self.__Organe = StringVar()
        Label3 = Label(self.__window,text="Organes affecter")
        list_option2 = ["Cerveaux","Foi","Uterus","Prostate"]
        option2 = OptionMenu(self.__window, self.__Organe, *list_option2)

        #Date de teste 
        Label4 = Label(self.__window,text="Date du test")
        self.__date = Entry(self.__window)

        #Tumeur
        Label6 = Label(self.__window,text="T")
        self.__T = Entry(self.__window)

        #le N
        Label7 = Label(self.__window,text="N")
        self.__N = Entry(self.__window)

        #le M 
        Label8 = Label(self.__window,text="M")
        self.__M = Entry(self.__window)

        #Button de confirmation
        button = Button(self.__window,text="Generer",command=self.generertnm)

        #Button Enregistrer
        button1 = Button(self.__window,text="Enregistrer",command=self.save)

        #Essayer a nouveau
        button2 = Button(self.__window,text="Reinitialiser",command=self.reset)

        #Liste recent Order by stade 
        button3 = Button(self.__window,text="Liste le plus dangeureux",command=self.Liste_recent)


        #AddPlace
        label1.place(x=200,y=2)
        label5.place(x=220,y=20)
       
        Label2.place(x=5,y=50)
        option.place(x=60,y=50)
       
        Label3.place(x=5,y=100)
        option2.place(x=110,y=100)

        Label4.place(x=5,y=150)
        self.__date.place(x=100,y=150)

        Label6.place(x=235,y=50)
        self.__T.place(x=270,y=50)

        Label7.place(x=235,y=100)
        self.__N.place(x=270,y=100)

        Label8.place(x=235,y=150)
        self.__M.place(x=270,y=150)

        button.place(x=270,y=175)
        button1.place(x=25,y=175)
        button2.place(x=325,y=175)
        button3.place(x=100,y=175)

        #Frame Window
        self.__frame = Frame(self.__window,bg='#DDE192',width=350,height=200)

        self.__List_Button_tnm = list()
        x=1
        y=1
        indice=0
        for i in range(0,25):
             button = Button(self.__frame,text="   ")
             self.__List_Button_tnm.append(button)
        
        for i in range(0,5):
            for u in range(0,5):
               self.__List_Button_tnm[indice].place(x=x*60,y=y*30) 
               indice+=1
               x+=1
            y+=1
            x=1
                
        
        label_t0 = Label(self.__frame,text="TIS",width=10)
        label_t1 = Label(self.__frame,text="T1",width=10)
        label_t2 = Label(self.__frame,text="T2",width=10)
        label_t3 = Label(self.__frame,text="T3",width=10)
        label_t4 = Label(self.__frame,text="T4",width=10)

        label_n0 = Label(self.__frame,text="N0")    
        label_n1 = Label(self.__frame,text="N1")    
        label_n2 = Label(self.__frame,text="N2")    
        label_n3 = Label(self.__frame,text="N3")    
        label_n4 = Label(self.__frame,text="N4")   

        label1_m0 = Label(self.__frame,text="M0")
        label1_m1 = Label(self.__frame,text="M1")
        
        self.__Button_m1 = Button(self.__frame,text="  ")
        self.__Button_m2 = Button(self.__frame,text="  ")

        
        self.__frame.place(x=25,y=250)
        #Les T
        label_t0.place(x=50,y=1)
        label_t1.place(x=100,y=1)
        label_t2.place(x=150,y=1)
        label_t3.place(x=200,y=1)
        label_t4.place(x=250,y=1)

        #Les N
        label_n0.place(y=30,x=1)
        label_n1.place(y=60,x=1)
        label_n2.place(y=90,x=1)
        label_n3.place(y=120,x=1)
        label_n4.place(y=150,x=1)

        #Les M
        label1_m0.place(y=180,x=1)
        label1_m1.place(y=180,x=70)

        self.__Button_m1.place(x=30,y=180)
        self.__Button_m2.place(x=100,y=180)

        self.__window.mainloop()

    def generertnm(self):
        patient = self.__Patient.get().split('(')
        organe = self.__Organe.get()  
        date = self.__date.get()  
        T = int(self.__T.get())
        N = int(self.__N.get())
        M = int(self.__M.get())
        indice_button = T+(N*5)
        self.__List_Button_tnm[indice_button].configure(text="  x  ")
        if M == 0:
            self.__Button_m1.configure(text="  x  ")
        else:
            self.__Button_m2.configure(text="  x  ")
        stade = Metiers().getStade(T,N,M)
        strq = "Stade : {}".format(stade)
        self.__stade = Label(self.__window,text=strq)
        self.__stade.place(x=260,y=220)


    def save(self):
        idpatient = self.__Patient.get().split('_id:')
        organe = self.__Organe.get()  
        date = self.__date.get()  
        T = int(self.__T.get())
        N = int(self.__N.get())
        M = int(self.__M.get())
        stade = Metiers().getStade(T,N,M)
        count = Connexion().countTable("tnm")+1
        requete = "insert into tnm values ({},'{}','{}',convert(date,'{}'),{},{},{},{})".format(count, idpatient[1] ,organe ,date ,T ,N ,M,stade) 
        Connexion().callreq(requete)

    def reset(self):
        for i in self.__List_Button_tnm:
            i.configure(text="   ")
        self.__Button_m1.configure(text="   ")
        self.__Button_m2.configure(text="   ")
        self.__stade.configure(text="None")

    def Liste_recent(self):
        Liste_recent()
        
class AddPersonne:
    __window1 = None
    __Patient = None
    __sexe = None
    __age = None
    __Organe = None
    def __init__(self):
        # Parametrage affichage
        self.__window1 = Tk()
        self.__window1.title("Cancer TNM")
        self.__window1.geometry("220x220")
        self.__window1.minsize(220,220)
        self.__window1.maxsize(220,220)
        self.__window1.config(background='#CFE3BC')

        #Titre 
        label1 = Label(self.__window1, text="TNM Cancer",font=("ravie",10),background='#CFE3BC' ,fg='white')
        label5 = Label(self.__window1,text="Ajouter Patient(Quittez cette fenetre pour \ntout de suite allez au tnm)",font=("Arial",7),background='#CFE3BC')
        

        #Nom de personne
        label2 = Label(self.__window1, text="Personne")
        self.__Patient = Entry(self.__window1)

        #Sexe
        self.__sexe = StringVar()
        label3 = Label(self.__window1, text="Sexe")
        ListOpt1 = ["M","F"]
        option = OptionMenu(self.__window1,self.__sexe, *ListOpt1)
        
        #age
        label4 = Label(self.__window1,text="age")
        self.__age = Entry(self.__window1)

        #Organe
        self.__Organe = StringVar()
        label6 = Label(self.__window1,text="Organes")
        List_Organe = ["Cerveaux","Foi","Uterus","Prostate"]
        Option = OptionMenu(self.__window1, self.__Organe, *List_Organe)

        #button confirmation
        button1 = Button(self.__window1,text="Enregistrer",command=self.insertPatient) 

        #emplacement
        label1.place(x=65,y=1)
        label5.place(x=1,y=30)
        label2.place(x=10,y=60)
        self.__Patient.place(x=75,y=60)
        label3.place(x=10,y=90)
        option.place(x=75,y=90)
        label4.place(x=10,y=130)
        self.__age.place(x=75,y=130)
        button1.place(x=115,y=190)
        label6.place(x=10,y=160)
        Option.place(x=75,y=160)

        self.__window1.mainloop()
    
    def insertPatient(self):
        patient = self.__Patient.get()
        sexe = self.__sexe.get()
        age = self.__age.get()
        org = self.__Organe.get()
        county = Connexion().countTable("Personne")+1
        counte = Connexion().countTable("Organe")+1
        requete = "insert into Personne values ({},'{}','{}',{})".format(county, patient ,sexe ,age)
        requte_Organe = "insert into Organe values ({},'{}',{})".format(counte,org,county)
        Connexion().callreq(requete)
        Connexion().callreq(requte_Organe)

class Liste_recent:
    __window = None
    def __init__(self):
        self.__window = Tk()
        self.__window.title("Cancer TNM")
        self.__window.geometry("425x500")
        self.__window.minsize(425,500)
        self.__window.maxsize(425,500)
        self.__window.config(background='#CFE3BC')

        label = Label(self.__window,text="Les Top 5 plus recent et dangeureux cas",font=("ravie",10))
        

        Data = Metiers().getListeRecentDanger()
        Liste_data = list()

        for Donnee in Data:
            Liste_data.append("Patient={}; Organe={}; date={}; T={}; N={}; M={}; stade={}".format(Donnee.get_nom(),Donnee.get_organe(),Donnee.get_daty(),Donnee.get_t(),Donnee.get_n(),Donnee.get_m(),Donnee.get_stade()))

        
        Liste = Listbox(self.__window,width=100)

        Liste.insert(END,*Liste_data)

        label.pack()
        Liste.pack()


        self.__window.mainloop()
TestTnm()

