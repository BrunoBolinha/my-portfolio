import json

ARCHIVE = 'car_list.json'

class Marca:
    def __init__(self, marca):
        self.marca = marca
    
    def to_dict(self):
        return {"__class__": type(self).__name__, "marca": self.marca}

class Motor(Marca):
    def __init__(self, motor):
        self.motor = motor

    def to_dict(self):
        return {"__class__": type(self).__name__, "motor": self.motor}

class Modelo(Marca):
    def __init__(self, marca, modelo, motor):
        self.modelo = modelo
        self.motor = motor
        self.marca = marca

    def to_dict(self):
        return {
            "__class__": type(self).__name__,
            "marca": self.marca.to_dict(),  
            "modelo": self.modelo,
            "motor": self.motor.to_dict()
        }

marcas = [Marca('Volks'), Marca('Chevrolet'), Marca('Fiat')]

motores = [Motor('Motor A'), Motor('Motor B'), Motor('Motor C')]

modelos = [
    Modelo(marcas[1], 'Astra', motores[0]),
    Modelo(marcas[1], 'Onix', motores[1]),
    Modelo(marcas[2], 'Siena', motores[1]),
    Modelo(marcas[2], 'Uno', motores[2]),
    Modelo(marcas[0], 'Voyage', motores[1]),
    Modelo(marcas[0], 'Jetta', motores[0]),
]

db = [modelo.to_dict() for modelo in modelos]

def do_dump():
    with open(ARCHIVE, 'w', encoding='utf8') as archive:
        json.dump(db, archive, ensure_ascii=False, indent=2)

do_dump()

def print_carros():
    with open(ARCHIVE, 'r', encoding='utf8') as archive:
        db = json.load(archive)
        for i in db:
            print(f"Marca: {i['marca']['marca']}, Modelo: {i['modelo']}, Motor: {i['motor']['motor']}")


print_carros()