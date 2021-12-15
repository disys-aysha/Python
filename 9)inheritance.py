class facebooklist:

 def updated(self):
  self.name=karthi
  self.name1=keerthi
  self.name2=Ravi
 
 def new(self):
    print(self.name)
 
 def __init__(self, fname,sname,tname):
    self.firstname = fname
    self.secondname = sname
    self.thirdname = tname
    
 def time(self):
     print(self.firstname)
    
u=facebooklist("karthi","Anu","james")
u.time()

class updatelist(facebooklist):

    def __init__(self, uname):
     self.updatedname = uname

    def night(self):
        print(self.updatename)


v=updatelist(facebooklist)
v.night()
v.updatedname()
    

    


 
