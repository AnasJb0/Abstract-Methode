from abc import ABCMeta, abstractmethod
class Personne(metaclass = ABCMeta):
    _count=0
    def __init__(self,code,nom,prenom,age) :
        self._code=code
        self._nom=nom
        self._prenom=prenom
        self._age=age
        Personne._count+=1
    @property
    def GetCode(self) :
        return self._code
    @property
    def GetNom(self) :
        return self._nom
    @property
    def GetPrenom(self) :
        return self._prenom
    @property
    def GetAge(self) :
        return self._age
    @property
    def GetCount(self) :
        return Personne._count
    def SetCode(self,new_code) :
        self._code=new_code
    def SetNom(self,new_nom) :
        self._code=new_nom
    def Setprenom(self,new_prenom) :
        self._code=new_prenom
    def Setage(self,new_age) :
        self._code=new_age
    @abstractmethod
    def ToString(self) :
        pass
    @abstractmethod
    def Equals(self, p1) :
        pass
class Employe(Personne) :
    _countt=0
    def __init__(self, code, nom, prenom, age,grade):
        super().__init__(code, nom, prenom, age)
        self._grade=grade
        Employe._countt+=1
    @property
    def GetCountt(self) :
        return Employe._countt
    @property
    def GetGrade(self) :
        return self._grade
    def SetGrade(self, new_grade) :
        self._grade=new_grade
    @property
    def ToString(self):
        return  (f" code: {str(self.GetCode)} , nom: {str(self.GetNom)} , prenom: {str(self.GetPrenom)} , age: {str(self.GetAge)}, grade: {str(self.GetGrade)}")
    def Equals(self, emp1) :
        if self._code == emp1._code :
            return True
        else : 
            return False

    
class  Eleve(Personne) :
    _counttt=0
    def __init__(self, code, nom, prenom, age,niveau,moyenne):
        super().__init__(code, nom, prenom, age)
        self._niveau=niveau
        self._moyenne=moyenne
        Eleve._counttt+=1
    @property
    def GetNiveau(self) :
        return self._niveau
    @property
    def GetMoyenne(self) :
        return self._moyenne
    @property
    def GetCounttt(self) :
        return Eleve._counttt
    def SetNiveau(self,new_niveau) :
        self._niveau=new_niveau
    def SetMoyenne(self,new_moyenne) :
        self._moyenne=new_moyenne
    @property
    def ToString(self):
        return  (f" code: {str(self.GetCode)} , nom: {str(self.GetNom)} , prenom: {str(self.GetPrenom)} , age: {str(self.GetAge)}, niveau: {str(self.GetNiveau)} , moyenne: {str(self.GetMoyenne)}")
    def Equals(self, elev1) :
        if self._code == elev1._code :
            return True
        else : 
            return False
        


emp1=Employe("SA93","Amsa","Sara",25,"Chef")
emp2=Employe("SA23","Nara","Wiam",20,"Student")
print(emp1.ToString)
print(emp1.Equals(emp2))
elev1=Eleve("F0da","Json","David",18,"Bac",16)
elev2=Eleve("Sa9D","Mansa","Eva",16,"5 eme",18)
print(elev1.ToString)
print(elev1.Equals(elev2))
        