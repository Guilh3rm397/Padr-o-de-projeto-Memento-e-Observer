# Questão 2 - Padrão Observer: venda de ingressos de eventos esportivos

class Observador:

    def atualizar(self, mensagem):
        pass


class Cliente(Observador):
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, mensagem):
        print(f"[Cliente {self.nome}] Notificação: {mensagem}")


class Administrador(Observador):
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, mensagem):
        print(f"[Administrador {self.nome}] Notificação: {mensagem}")


class Desconto:

    def __init__(self, nome, tipo, percentual, quantidade_minima=0):
        self.nome = nome
        self.tipo = tipo                 
        self.percentual = percentual     
        self.quantidade_minima = quantidade_minima


class Ingresso:

    def __init__(self, tipo, preco):
        self.tipo = tipo
        self.preco = preco
        self.desontos = []
        self.observadores = []

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def remover_obserador(self, observador):
        if observador in self.observadores:
            self.observadores.remove(observador)

    def notificar_bservadores(self, mensagem):
        for observador in self.observadores:
            observador.atualizar(mensagem)

    def alterar_preco(self, novo_preco):
        preco_antigo = self.preco
        self.preco = novo_preco
        self.notificar_observadores(
            f"O preço do inresso {self.tipo} mudou de "
            f"R$ {preco_antigo:.2f} para R$ {novo_preco:.2f}.")

    def adicionar_desconto(self, desconto):
        self.descontos.append(desconto)
        self.notificar_observadores(
            f"Novo desconto no ingresso {self.tipo}: "
            f"{desconto.nome} ({desconto.percentual}%).")

    def calcular_preco_final(self, quantidade=1, estudante=False):
        """Preço total aplicando os descontos que valem para a compra."""
        valor_unitario = self.preco
        for desconto in self.descontos:
            if desconto.tipo == "estudante" and estudante:
                valor_unitario -= valor_unitario * desconto.percentual / 100
            elif desconto.tipo == "quantidade" and quantidade >= desconto.quantidade_minima:
                valor_unitario -= valor_unitario * desconto.percentual / 100
        return valor_unitario * quantidade


def demonstrar():
    premium = Ingresso("Cadeira Premium", 200.00)
    arquibancada = Ingresso("Arquibancada", 80.00)
    camarote = Ingresso("Camarote", 500.00)
    ingressos = [premium, arquibancada, camarote]

    maria = Cliente("Maria")
    joao = Cliente("João")
    admin = Administrador("Carlos")

    for ingresso in ingressos:
        ingresso.adicionar_observador(maria)
        ingresso.adicionar_observador(admin)
    arquibancada.adicionar_observador(joao)  

    print("=== 1) Alterando o preço da Arquibancada ===")
    arquibancada.alterar_preco(100.00)

    print("\n=== 2) Alterando o preço do Camarote ===")
    camarote.alterar_preco(550.00)

    print("\n=== 3) Adicionando descontos na Arquibancada ===")
    arquibancada.adicionar_desconto(Desconto("Desconto Estudante", "estudante", 50))
    arquibancada.adicionar_desconto(Desconto("Desconto 4+ ingressos", "quantidade", 10, 4))

    print("\n=== 4) Adicionando desconto na Cadeira Premium ===")
    premium.adicionar_desconto(Desconto("Desconto Estudante", "estudante", 20))

    print("\n=== 5) João deixa de acompanhar a Arquibancada ===")
    arquibancada.remover_observador(joao)
    arquibancada.alterar_preco(90.00)

    print("\n=== Simulação de preços finais (Arquibancada) ===")
    print(f"1 ingresso, não estudante: R$ {arquibancada.calcular_preco_final(1, False):.2f}")
    print(f"1 ingresso, estudante:     R$ {arquibancada.calcular_preco_final(1, True):.2f}")
    print(f"5 ingressos, não estudante: R$ {arquibancada.calcular_preco_final(5, False):.2f}")


if __name__ == "__main__":
    demonstrar()
