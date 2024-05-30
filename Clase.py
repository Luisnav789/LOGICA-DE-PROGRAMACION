class Opcion():
    def __init__(self,atributo, gana, pierde):
        self.atributo=atributo
        self.gana=gana
        self.pierde=pierde

    def comprobar_Gana(self,rival):
        if rival in self.gana:
            return "Gana"
        else: 
            if rival==self.atributo:
                return "Empate"
            else:
                return "Pierde"