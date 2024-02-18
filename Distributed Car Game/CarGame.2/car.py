import random
class Car:
    def __init__(self,id):
        self.display_width = 1200
        self.display_height = 600
        self.x_coordinate=0
        self.y_coordinate=0
        self.x_coordinate = None
        self.y_coordinate = None
        self.high_score = 0
        self.pending_message=False
        self.id=id
        self.initialize()

    def initialize(self):
        self.x_coordinate = (random.randint(300,self.display_width-300))
        self.y_coordinate = (self.display_height * 0.75)
        self.width = 49
        self.connected=False

    def to_dict(self):
        return {'id': self.id, 'x_coordinate': self.x_coordinate, 'y_coordinate': self.y_coordinate,'high_score': self.high_score}

    @staticmethod
    def retrieve_car(car):
        new_car=Car(car["id"])
        new_car.x_coordinate=car["x_coordinate"]
        new_car.y_coordinate = car["y_coordinate"]
        new_car.high_score = car["high_score"]
        return new_car




