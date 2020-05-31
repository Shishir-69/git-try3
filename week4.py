#      import sys

#sys.setrecursionlimit(80000)
#print(sys.ge
# trecursionlimit())
"""z = 0
def coventry():
    global z
    z =z+ 1
    print("my college", z)
    coventry()
coventry()"""


class Car():
    def __init__(self, year , model , name):
        self.year = year
        self.model = model
        self.name = name
        self.odometer = 25

    def altogether(self):
        sabai = str(self.year) + ' ' + self.model + ' ' + self.name
        return sabai.title()

    def update_odometer(self, milage):
        if milage >= self.odometer:
            self.odometer = milage
        else:
            print('fuck you')

    def increment_odometer(self, miles):
        self.odometer += miles


    def read_odometer(self):
        print('it has run ' + str(self.odometer) + ' across')




class Battery():
    def __init__(self, battery_power = 7000):
        self.battery_power = battery_power
    def describe_battery(self):
        print("This car has battery power of " + str(self.battery_power))




class Electric_car(Car):
    def __init__(self,year , model , name):
        super().__init__(year,model,name)
        self.battery = Battery(5000)

    def range_battery(self):
        if self.battery.battery_power == 5000:
            range = 3000
        elif self.battery.battery_power == 7000:
            range = 5000
        message = 'This car can run up to ' + str(range)
        message += '-miles'
        print(message)

electric = Electric_car(2017, 'lambo' , 'bitches')
print(electric.altogether())
electric.battery.describe_battery()
electric.range_battery()







