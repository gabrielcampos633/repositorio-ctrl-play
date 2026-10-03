# class Carro:
#     marca = 'honda'
#     modelo = 'civic'
#     ano = '2024'
#     cor = 'preto'

#     def __init__(self, cor, ano):
#         self.cor = cor
#         self.ano = ano

#     def __str__(self):
#         return f'O carro um eh um {self.marca} e o modelo eh um {self.modelo} '

#     def acelerar(self):
#         print('Acelerando')

#     def ligar(self):
#         print('Ligando o carro')

#     def passar_pro_neutro(self):
#         print('Passando pro neutro')

#     def desligar_carro(self):
#         print('Desligando o carro')

# carro2 = (Carro)
# carro2.modelo = 'city'

# carro1 = Carro('branco', '2022')
# print(carro1.cor)
# print(carro1.ano)


# carro2 = Carro('Vermelho', '2027')
# print(carro2.cor)
# print(carro2.ano)


class Personagem:
    vida = 100
    moedas = 0 
    nivel = 1 
    status = 'plebeu'

    def __init__(self, nome, classe, familia):
        self.nome = nome
        self.classe = classe 
        self.familia = familia

    def dano(self, valor):
        self.vida -= valor    
       
        if self.vida <= 0:
            print('Você tomou {self.valor} de dano e morreu \n Faz o L')

        else:
            print(f'Você tomou {self.valor} de dano')

    # def adicionar_moedas(self, valor)
        self.moedas += valor
        print(f'Moedas: {self.moedas}

    def tirar_moedas(self, valor):
        if (self.moedas - valor <0):
            self.moedas -= valor
        else:
            print(f'Você é pobre')


personagem = Personagem('Jorginho', 'Mago', 'Aketja', 0)
