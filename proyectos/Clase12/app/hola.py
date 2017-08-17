"""
Este el Modulo para saludar 
a la gente de la UIP

"""
class Hola(object):

    """
    Esta es la clase Hola que permite saludar
    """
    def __init__(self, nombre):

        """
        Este es el metodo contructor de la clase.
        CRea una nueva instancia de :class:   'Hola'
        :param nombre: nombre para el saludo
        :type nombre; str
        
        """

        self.nombre = nombre


    def saludar(self):


        """
        Este es el metodo para saludar a la gente.usa el atributo nombre y lo imprime.
        
        """

        print("Hola, %s "% self.nombre)


    def getNombre(self):

        """
        Este es el metodo para enviar el valor del nombre.
        :return: nombre usado en el saludo

        """
        return self.nombre