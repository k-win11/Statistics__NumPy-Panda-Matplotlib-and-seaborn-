class Vechicle:
    
    
    name=''
    color=''
    kind='car'
    value= 100.00
    
    def description(self):
        desc_str='%s is a %s %s worth $%.2f'%(self.name,self.color,self.kind,self.value)
        return desc_str
    
car1=Vechicle()
car1.name='fer'
car1.color='red'
car1.kind='convertible'
car1.value=60000.00
    
car2=Vechicle()
car2.name='jump'
car2.color='blue'
car2.kind='van'
car2.value=10000.00
    
    
print(car1.description())