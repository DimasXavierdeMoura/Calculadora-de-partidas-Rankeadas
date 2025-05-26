TIPOS_DISPONIVEIS = ["mago", "guerreiro", "monge", "ninja"]
print("Tipos disponíveis de herói:")
for tipo in TIPOS_DISPONIVEIS:
    print(f"- {tipo}")

nome = input("Digite o nome do seu herói: ")
idade = input("Digite a idade do seu herói: ")
tipo = input("Escolha um herói entre as opções acima: ")

class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            print(f"Tipo desconhecido: {self.tipo}. Escolha um tipo válido.")
            novo_tipo = input("Digite um tipo válido (mago, guerreiro, monge, ninja): ")
            self.tipo = novo_tipo
            self.atacar()
            return
        print(f"o {self.tipo} atacou usando {ataque}")
        
heroi = Heroi(nome, idade, tipo)
heroi.atacar()