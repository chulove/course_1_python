class Car:
    car_id = 0

    def __init__(self, speed=0, color="Black", name=None):
        self.speed = speed
        self.color = color
        self.__is_police = False
        self.name = name if name else f"car {Car.car_id}"
        self.move = False
        Car.car_id += 1

    def go(self):
        self.move = True
        print(f'{self.name} has started moving')

    def stop(self):
        self.move = False
        print(f'{self.name} has stopped')

    def turn(self, direction):
        print(f'{self.name} has turned {direction}')

    def show_speed(self):
        if self.move:
            print(f'{self.name} is moving with speed {self.speed} mph')
        else:
            print(f'{self.name} is not moving')


class TownCar(Car):
    def show_speed(self):
        if self.move:
            print(f'{self.name} is moving with speed {self.speed} mph')
            if self.speed > 60:
                print(f'Warning! Exceeding the speed limit')
        else:
            print(f'{self.name} is not moving')


class SportCar(Car):
    def nitro(self):
        self.speed = self.speed * 1.5


class WorkCar(Car):
    def show_speed(self):
        if self.move:
            print(f'{self.name} is moving with speed {self.speed} mph')
            if self.speed > 40:
                print(f'Warning! Exceeding the speed limit')
        else:
            print(f'{self.name} is not moving')


class PoliceCar(Car):
    def __init__(self, speed):
        super(PoliceCar, self).__init__(speed, color="Blue/White")
        self.__is_police = True
        self.name = f"Police car {Car.car_id}"


town_car_1 = TownCar(30, 'White', 'town car 1')
town_car_2 = TownCar(80, 'Grey', 'town car 2')
sport_car = SportCar(200, 'Red')
work_car_1 = TownCar(30, 'Yellow', 'work car 1')
work_car_2 = TownCar(60, 'Blue', 'work car 2')
police_car = PoliceCar(100)

cars = {"town_car_1": TownCar(30, 'White', 'town car 1'),
        "town_car_2": TownCar(80, 'Grey', 'town car 2'),
        "sport_car": SportCar(200, 'Red'),
        "work_car_1": TownCar(30, 'Yellow', 'work car 1'),
        "work_car_2": TownCar(60, 'Blue', 'work car 2'),
        "police_car": PoliceCar(100)}

for k, v in cars.items():
    v.show_speed()
    if v.color in ['Grey', 'Yellow', 'Red']:
        v.go()
        try:
            v.nitro()
        except:
            pass
        v.show_speed()
