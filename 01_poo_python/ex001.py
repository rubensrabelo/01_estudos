class Cubo:
    '''Classe para calcular o cubo de um número'''
    def __init__(self, valor):
        self.x = valor
        print("Objeto criado!")

    def calcula_cubo(self):
        cubo = self.x * self.x * self.x
        return f'Cubo calculado: {cubo}.'

teste = Cubo(5)

print(teste.calcula_cubo())