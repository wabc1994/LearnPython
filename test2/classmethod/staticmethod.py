class Date:
    def __init__(self,month,day,year):
        self.month=month
        self.day=day
        self.year=year
    def display(self):
        return "{0}-{1}-{2}".format(self.month,self.day,self.year)
    @staticmethod
    def millenium(month,day):
        return Date(month,day,2000)
new_year=Date(1,1,2013)    #Create a new Date object
millenium_new_year=Date.millenium(1,1)  #also creates a Date object
new_year.display()
millenium_new_year.display()
#Proof
print(isinstance(new_year,Date))
print(isinstance(millenium_new_year,Date))

