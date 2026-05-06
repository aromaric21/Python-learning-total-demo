class DVD:
    def __init__(self, titre, realisateur, annee):
        self.titre = titre 
        self.realisateur = realisateur
        self.annee = annee
     
    def __str__(self):
         return f"{self.titre} ({self.annee}) réalisé par {self.realisateur}"   
        
        