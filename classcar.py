class car(object):
# same as constructor in our java script class definition    
    def _init_(self,model,color,company_name,speed_limit):
        self.color=color
        self.speed_limit=speed_limit
        self.model=model
        self.company_name=company_name
        
    def start(self):
        print("car started")
    def stop(self):
        print("car stopped")
    def go(self):
        print("Car go!")
    def grear(self,gear_type):
        print("gear changed")    
        
audi= car("A6","red","Audi",80)    

print(audi.start())    
                