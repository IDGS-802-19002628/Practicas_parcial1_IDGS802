import os


class numeros:
    # Declaracion de propiedades
    num1 = 0
    lista1 = []
    lista2 = []
    lista3 = []
    num2 = 0
    i = 0
    res = 0

    # Declaracion de constructor

    def __init__(self, a):
        self.num1 = int(a)
        int(self.i)

    # Declaracion de metodos de clase
    def listaNumeros(self):
        while self.i < self.num1:
            self.i += 1
            self.num2 = input('Ingresa el numero\n')
            self.lista1.append(int(self.num2))
            if int(self.num2) % 2 == 0:
                
                self.lista2.append(int(self.num2))
            else:
                
                self.lista3.append(int(self.num2))

        self.lista1.sort()
        print("La lista ordenada es: {}".format(self.lista1))
        print("La lista de pares es: {}".format(self.lista2))
        print("La lista de impares es: {}".format(self.lista3))


# Declaracion de la función main fuera de la clase


def main():
    # Lineas para limpiar la terminal
    os.system('cls')
    num = input('Ingresa la cantidad de numeros desea registrar\n')
    obj = numeros(num)
    obj.listaNumeros()


if __name__ == "__main__":
    main()
