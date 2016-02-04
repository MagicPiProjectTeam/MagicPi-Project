class HostInformation:
    env = None;
    interfaces = {};
    netIfaces = None;

    #Constructeur de la classe, on appel loadInformation
    def __init__(self,Environement):
        self.env = Environement;
        self.netIfaces = Environement.getImport("netifaces");
        self.loadInformation();

    # Methode appele a la construction, instancie les parametres de l'interface
    def loadInformation(self):
        for interface_en_cours in self.netIfaces.interfaces() :
            self.interfaces[interface_en_cours] = self.netIfaces.ifaddresses(interface_en_cours);

    # Retourne la liste des interfaces
    def getInterfaces(self):
        return self.interfaces.keys();

    # Retourne les informations de l'interface
    def getInfoForInterface(self,interface):
        return self.interfaces[interface][self.netIfaces.AF_INET];

    #retourne le CIDR
    def getCidrFromIp(self,ip):
        return '/'+str('.'.join([bin(int(x)+256)[3:] for x in ip.split('.')]).count('1'));
