import math

class Personaje:
    nivel = 1
    experiencia = 0

    def __init__(self, p_nombre):
        self.nombre = p_nombre

    def __lt__(self, other):
        return self.nivel < other.nivel

    def __gt__(self, other):
        return self.nivel > other.nivel

    def __eq__(self, other):
        return self.nivel == other.nivel

    def get_estado(self):
        return self.nombre, self.nivel, self.experiencia

    def set_estado(self, p_experiencia):
        v_nueva_experiencia = p_experiencia + self.experiencia

        if v_nueva_experiencia < 0:
            self.experiencia = 0
            if self.nivel > 1:
                self.experiencia = 100+v_nueva_experiencia
                self.nivel -= 1
        elif (v_nueva_experiencia)/100 >= 1:
            self.nivel += math.floor((v_nueva_experiencia)/100)
            self.experiencia = v_nueva_experiencia%100
        else:
            self.experiencia = v_nueva_experiencia%100

    def get_probabilidad(self, p_personaje):
        if self.__lt__(p_personaje):
            v_probabilidad = 0.33
        elif self.__gt__(p_personaje):
            v_probabilidad = 0.66
        else:
            v_probabilidad = 0.5

        return v_probabilidad
            






