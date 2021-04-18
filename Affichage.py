from tkinter import *
from Ipv4 import *

class Gui:
    window = None
    ip_adress = None
    ip_adress_no_class = None
    ip_adress_v6 = None

    classe = None
    masque = None
    adresse_reseau = None
    adresse_diffusion = None

    masque_nc = None
    adresse_reseau_nc = None
    adresse_diff_nc = None
    nb_adresse_dispo = None
    first_adress = None
    last_adress = None

    adresse_reseaux_v6 = None


    def __init__(self):
        self.window = Tk()
        self.window.title("Calcul adresse IP")
        self.window.geometry("425x500")
        self.window.minsize(1000,500)
        self.window.maxsize(1000,500)
        self.window.config(background='#CFE3BC')
        #Titre 
        label1 = Label(self.window,text="IPV4")
        label1.place(x=50,y=2)
        self.ip_adress = Entry(self.window)
        self.ip_adress.place(x=50,y=20)
        button = Button(self.window,text="Generer",command=self.generateIpv4)
        button.place(x=175,y=20)
        self.classe = Label(self.window,text="Classe")
        self.masque = Label(self.window,text="Masque")
        self.adresse_reseau = Label(self.window,text="Adresse reseaux")
        self.adresse_diffusion = Label(self.window,text="Adresse diffusion")
        self.classe.place(x=50,y=50)
        self.masque.place(x=50,y=80)
        self.adresse_reseau.place(x=50,y=110)
        self.adresse_diffusion.place(x=50,y=110)

        label2 = Label(self.window,text="IPV4 Sans Classe")
        label2.place(x=250+70,y=2)
        self.ip_adress_no_class = Entry(self.window)
        self.ip_adress_no_class.place(x=250+70,y=20)
        button1 = Button(self.window,text="Generer",command=self.Ipv4_nc)
        button1.place(x=375+70,y=20)
        self.masque_nc = Label(self.window,text="Masque")
        self.masque_nc.place(x=250+70,y=50)
        self.adresse_reseau_nc = Label(self.window,text="Adresse reseau")
        self.adresse_reseau_nc.place(x=320,y=80)
        self.adresse_diff_nc = Label(self.window,text="Adresse diffusion")
        self.adresse_diff_nc.place(x=320,y=110)
        self.nb_adresse_dispo = Label(self.window,text="Nbe d'adresse disponible")
        self.nb_adresse_dispo.place(x=320,y=140)
        self.first_adress = Label(self.window,text="premiere adressse")
        self.first_adress.place(x=320,y=170)
        self.last_adress = Label(self.window,text="dernier adresse")
        self.last_adress.place(x=320,y=200)



        label3 = Label(self.window,text="IPV6")
        label3.place(x=500+150,y=2)
        self.ip_adress_v6 = Entry(self.window)
        self.ip_adress_v6.place(x=500+150,y=20)
        button3 = Button(self.window,text="Generer",command=self.ipv6_launch)
        button3.place(x=625+150,y=20)
        self.adresse_reseaux_v6 = Label(self.window,text="Adresse reseau")
        self.adresse_reseaux_v6.place(x=650,y=50)
        self.window.mainloop()

    def generateIpv4(self): 
        function = Ipv4(self.ip_adress.get())
        function.generate()
        self.classe["text"] = function.getClasse()
        self.masque["text"] = function.getMasque()
        self.adresse_reseau["text"] = function.getAdresse_reseau()
        self.adresse_diffusion["text"] = function.getAdresse_diffusion()

    def Ipv4_nc(self):
        ipv4_nc = Ipv4_no_class(self.ip_adress_no_class.get())
        self.masque_nc["text"] = ipv4_nc.get_masque()
        self.adresse_reseau_nc["text"] = ipv4_nc.generateAdressReseau()
        self.adresse_diff_nc["text"] = ipv4_nc.generateAdressDiffusion()
        self.nb_adresse_dispo["text"] = ipv4_nc.nbe_adress_dispo()
        self.first_adress["text"] = ipv4_nc.first_adress()
        self.last_adress["text"] = ipv4_nc.last_adress()

    def ipv6_launch(self):
        ipv6 = Ipv6(self.ip_adress_v6.get())
        self.adresse_reseaux_v6["text"] = ipv6.adresse_reseau()

Gui()