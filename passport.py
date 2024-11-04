import datetime
import time 

class Passport:

    passport_id_counter = 0
# Init methd to initialize the variables and countries dictionary
    def __init__(self, first_name, last_name, dob, country, exp_date):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = datetime.date.fromisoformat(dob)
        self.country = country
        self.exp_date = datetime.date.fromisoformat(exp_date)
        self.passport_id = Passport.passport_id_counter
        Passport.passport_id_counter += 1
        self.countries = {}
#Checking the validity of the Passport    
    def is_valid(self):
        if self.exp_date > datetime.date.fromtimestamp(time.time()):
            return True
        else:
            return False
#Summary of the passport
    def summary(self):
        if self.is_valid == True:
            return (f'This passport belongs to {self.first_name} {self.last_name}, born on {self.dob} in {self.country}. It is valid')
        else:
            return (f'This passport belongs to {self.first_name} {self.last_name}, born on {self.dob} in {self.country}. It is invalid')
#Checking if the data given is matching with the passport    
    def check_data(self, first_name, last_name, dob, country):
        if self.is_valid() == True and first_name == self.first_name and last_name==self.last_name and datetime.date.fromisoformat(dob) ==self.dob and country ==self.country:
            return True
        else:
            return False
#Stamping the passport and updating the countries counter   
    def stamp(self, country):
        if self.is_valid() and country != self.country:
            if country in self.countries:
                self.countries[country] +=1
            else:
                self.countries[country] =1 
#Returning the number of countries visited        
    def countries_visited(self):
        return self.countries
    
    def times_visited(self, country):
        if country in self.countries:
            return (self.countries[country])
        else:
            return (0)
#Squaring the number of visits    
    def sum_square_visits(self):
        return sum(self.countries[country]**2 for country in self.countries)
#Incrementing the passport number    
    def passport_number(self):
        if self.passport_id == 0:
            pass
        return self.passport_id