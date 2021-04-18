import math

class Ipv4:
    adresse_ip = ""
    classe = ""
    masque = ""
    adresse_reseaux = ""
    adresse_diffusion = ""

    def __init__(self,ipv4):
        self.adresse_ip = ipv4

    def generate(self):
        adresseSplit = self.adresse_ip.split(".")
        if int(adresseSplit[0]) <= 255 and int(adresseSplit[0]) >= 240:
            self.classe = "E"
            self.masque = "--"
            self.adresse_reseaux = "--"
            self.adresse_diffusion = "--"
        elif int(adresseSplit[0]) <= 239 and int(adresseSplit[0]) >= 224:
            self.classe = "D"
            self.masque = "255.255.255.255"
            self.adresse_reseaux = adresseSplit[0]+"."+adresseSplit[1]+"."+adresseSplit[2]+"."+adresseSplit[3]+".0"
            self.adresse_diffusion = adresseSplit[0]+"."+adresseSplit[1]+"."+adresseSplit[2]+"."+adresseSplit[3]+".255"
        elif int(adresseSplit[0]) <= 223 and int(adresseSplit[0]) >= 192:
            self.classe = "C"
            self.masque = "255.255.255.0"
            self.adresse_reseaux = adresseSplit[0]+"."+adresseSplit[1]+"."+adresseSplit[2]+"0.0"
            self.adresse_diffusion = adresseSplit[0]+"."+adresseSplit[1]+"."+adresseSplit[2]+".255"
        elif int(adresseSplit[0]) <= 191 and int(adresseSplit[0]) >= 128:
            self.classe = "B"
            self.masque = "255.255.0.0"
            self.adresse_reseaux = adresseSplit[0]+"."+adresseSplit[1]+".0.0"
            self.adresse_diffusion = adresseSplit[0]+"."+adresseSplit[1]+".255.255"
        elif int(adresseSplit[0]) <= 126 and int(adresseSplit[0]) >=0:
            self.classe = "A"
            self.masque="255.0.0.0"
            self.adresse_reseaux = adresseSplit[0]+".0.0.0"
            self.adresse_diffusion = adresseSplit[0]+".255.255.255"
        else :
            self.classe =  "Localhost"
            self.masque =  "--"
            self.adresse_reseaux =  "--"
            self.adresse_diffusion =  "--"

    def getClasse(self):
        return self.classe

    def getMasque(self):
        return self.masque

    def getAdresse_reseau(self):
        return self.adresse_reseaux

    def getAdresse_diffusion(self):
        return self.adresse_diffusion


        

class Ipv4_no_class:
    adresse_ip = ""
    chiffre = ""
    masque = ""
    adresse_reseaux = ""
    adresse_diffusion = ""
    adresse_dipso = 0
    first_adresse = ""
    last_adresse = ""

    def __init__(self,ipv4):
        adrr = ipv4.split("/")
        self.adresse_ip = adrr[0]
        self.chiffre = adrr[1]
    
    def generateMasqueBinary(self):
        octes_hex = self.adresse_ip.split(".")
        case = 1
        binar = 1
        result = ""
        for item in octes_hex:
            for i in range(8):
                if case > int(self.chiffre):
                    binar = 0
                result += ""+str(binar)
                case += 1
            if case <= 32 :
                result += "."
        return result
    
    def generateAdressReseau(self):
        octes_hex = self.adresse_ip.split(".")
        case_change = math.ceil(int(self.chiffre)/8)-1
        case = int(self.chiffre) - (case_change*8)
        for indice in range(case_change,len(octes_hex)):
            binary = ""
            for i in range(8):
                if indice == case_change and i == case-1:
                    binary += "1"
                else:
                    binary += "0"
            decimal = int(binary,2)
            octes_hex[indice] = str(decimal)
        result = ""
        for item in octes_hex:
            result += item+"."
        return result[:-1]

    def generateAdressDiffusion(self):
        octes_hex = self.adresse_ip.split(".")
        case_change = math.ceil(int(self.chiffre)/8)-1
        case = int(self.chiffre) - (case_change*8)
        for indice in range(case_change,len(octes_hex)):
            binary = ""
            for i in range(8):
                if i >= case-1 or indice>case_change:
                    binary += "1"
                else:
                    binary += "0"
            decimal = int(binary,2)
            octes_hex[indice] = str(decimal)
        result = ""
        for item in octes_hex:
            result += item+"."
        return result[:-1]

    def convert_adresse_binary(self,adresse):
        adresseSplit = adresse.split(".")
        result = ""
        for item in adresseSplit:
            decimal_octes = int(item,2)
            result += ""+str(decimal_octes)+"."
        return result[:-1]

    def nbe_adress_dispo(self):
        nbe = 32-int(self.chiffre)
        return math.pow(2,nbe)-2
    
    def get_masque(self):
        masque = self.generateMasqueBinary()
        self.masque = self.convert_adresse_binary(masque)
        return self.masque
    
    def first_adress(self):
        adresse_reseaux = self.generateAdressReseau()
        adresseSplit = adresse_reseaux.split(".")
        adresseSplit[3] = str(int(adresseSplit[3])+1)
        result = ""
        for item in adresseSplit:
            result += item+"."
        return result[:-1]

    def last_adress(self):
        adresse_reseaux = self.generateAdressDiffusion()
        adresseSplit = adresse_reseaux.split(".")
        adresseSplit[3] = str(int(adresseSplit[3])-1)
        result = ""
        for item in adresseSplit:
            result += item+"."
        return result[:-1]


class Ipv6:
    address_ip = ""
    chiffre = ""
    def __init__(self,address):
        addr = address.split("/")
        if addr[0][len(addr[0])-1] == ":":
            self.address_ip = addr[0][:-1]
        else:
            self.address_ip = addr[0]
        self.chiffre = addr[1]

    def getIp_octes(self):
        return self.address_ip.split(":")
    
    def check_octes_zero(self,ip_octes):
        for item in ip_octes:
            if len(item) == 0 :
                return True
        return False
    
    def develop_octes_zero(self):
        ip_octes = self.getIp_octes()
        boole = self.check_octes_zero(ip_octes)
        count = 0
        case = -1
        i = 0
        if(boole):
            for item in ip_octes:
                if len(item) != 0:
                    count += 1
                else:
                    case = i
                i += 1
        count = 8 - count 
        result = ""
        for i in range(len(ip_octes)):
            if i == case :
                result += "0000:"*count
            else: 
                result += self.complete_zero(ip_octes[i])+":"
        return result[:-1]

    def complete_zero(self,octes_hex):
        complete = 4 - len(octes_hex) 
        octes_hex = "0"*complete+octes_hex
        return octes_hex

    def adresse_reseau(self):
        octes_hex = self.develop_octes_zero().split(":")
        case_change = math.ceil(int(self.chiffre)/16) - 1
        case = int(self.chiffre) - (case_change*16)
        for indice in range(case_change,len(octes_hex)):
            res = "{0:08b}".format(int(octes_hex[indice], 16))
            osa_zero = 16-len(res)
            binary = "0"*osa_zero+res
            for i in range(16):
                if indice == case_change and i > case:
                    binary[i] = "0"
                elif indice > case_change:
                    binary = "0"
                    break
            hex_decimal = hex(int(binary,2))
            octes_hex[indice] = str(hex_decimal[2:])
        result = ""
        for item in octes_hex:
            result += item+":"
        return result[:-1]


    



