class Experimento:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}"

    def mostrar_info(self):
        Proyecto.mostrarxexperimento(FNAF)
    #Redirige a la función del proyecto

class Cientifico:
    instancias = []
    def __init__(self, nombre):
        self.nombre = nombre
        Cientifico.instancias.append(self)
        #Esta lista añade automaticamente a los cientificos al ser creados

    def __str__(self):
        return f"{self.nombre}"

    def mostrar_info(self):
        Proyecto.mostrarxcientifico(FNAF)
    #Redirige a la función del proyecto

    def mostrar_lista(self):
        print("Objetos creados:")
        for obj in Cientifico.instancias:
            print(obj)
    #Imprime los objetos de la lista en el constructor


class Estacion:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}"

    def mostrar_info(self):
        Proyecto.mostrarxestaion(FNAF)
    #Redirige a la función del proyecto

class Proyecto:
    def __init__(self, nombre, Cientifico, Estacion, Experimento):
        self.nombre = nombre
        self.Cientifico = Cientifico
        self.Estacion = Estacion
        self.Experimento = Experimento

    def mostrarxcientifico(self):
        print(f"El Cientifico {self.Cientifico} está trabajando en el experimento: {self.Experimento} en la instalación: {self.Estacion}")
    def mostrarxestaion(self):
        print(f"En la Instalación: {self.Estacion} se investiga el experimento: {self.Experimento} con el científico: {self.Cientifico}")
    def mostrarxexperimento(self):
        print(f"El Experimento: {self.Experimento} está siendo investigado en: {self.Estacion}, por el científico: {self.Cientifico}")


#1. Debes darle una condicional a las listas para que no cuenten un objeto que sea identico a otro
#2. Debes hacer que cada objeto reconozca a que proyecto pertenece sin la necesidad de tú colocarlo
#3. Puedes crear una clase solo para todo el Proyecto Manhattan y que solo te de la lista de todos los proyectos

