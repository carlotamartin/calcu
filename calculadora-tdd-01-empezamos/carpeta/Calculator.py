class Calculator:
    def __init__(self):
        self.value = 0

    def suma(self, a, b):
        self.value = a + b
        return (print('SUMA: \n' + str(a) + ' sumado a '+str(b)+ ' es = ' + str(self.value)+ '\n'))

    def resta(self, a, b):
        self.value = a - b
        return (print('RESTA: \n' + str(a) + ' menos '+str(b)+ ' es = ' + str(self.value)+ '\n'))

    def producto(self, a, b):
        self.value = a * b
        return (print('MULTIPLICACIÓN: \n' + str(a) + ' multiplicado por '+str(b)+ ' es = ' + str(self.value)+ '\n'))

    def división(self, a, b):
        self.value = a / b
        return (print('DIVISIÓN: \n' + str(a) + ' dividido entre '+str(b)+ ' es = ' + str(self.value)+ '\n'))

    def potencia(self, a, b):
        self.value = a**b
        return (print('POTENCIA: \n' + str(a) + ' elevado a la '+str(b)+ ' es = ' + str(self.value)+ '\n'))

    def factorial(self, numero):
        fact = 1
        for i in range(1,numero+1):
            fact = fact * i
        self.value = fact
        return (print('FACTORIAL: \n' + ' El factorial de  '+ str(numero) +' es = ' + str(self.value) + '\n'))




