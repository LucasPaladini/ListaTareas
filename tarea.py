
class Tarea:
    def __init__(self, descripcion):
        self.__descripcion = descripcion
        print(self.__descripcion)

    # def marcar_completada(self):
    #     self.completada = True

    def __str__(self):
        return self.__descripcion
