class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_info(self):
        print(f"Nome: {self.nome}")  # Saída: nome do produto
        print(f"Preço: R$ {self.preco}")  # Saída: preço do produto
        print(f"Quantidade: {self.quantidade}")  # Saída: quantidade do produto

    def mostrar_valor_total_estoque(self):
        valor_total = self.preco * self.quantidade
        print(f"O valor total de estoque deste produto é R$ {round(valor_total, 2)}")




# Exemplo de uso da classe Produto
p1 = Produto("Água", 1.99, 20)
p1.mostrar_info()
p1.mostrar_valor_total_estoque()

p2 = Produto("Refrigerante", 2.50, 10)
p2.mostrar_info()
p2.mostrar_valor_total_estoque()
