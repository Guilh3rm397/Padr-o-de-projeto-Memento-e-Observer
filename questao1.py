# Questão 1 - Padrão Memento: gerenciador de tarefas com função "desfazer"

class Tarefa:

    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao


class Memento:

    def __init__(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado


class Zelador:

    def __init__(self):
        self.historico = []

    def guardar(self, memento):
        self.historico.append(memento)

    def recuperar(self):
        if len(self.historico) == 0:
            return None
        return self.historico.pop()


class GerenciadorDeTarefas:

    def __init__(self):
        self.tarefas = []
        self.zelador = Zelador()

    def criar_memento(self):
        estado = [(t.get_titulo(), t.get_descricao()) for t in self.tarefas]
        return Memento(estado)

    def restaurar_memento(self, memento):
        self.tarefas = [Tarefa(titulo, descricao)
                        for titulo, descricao in memento.get_estado()]

    def adicionar_tarefa(self, titulo, descricao):
        self.zelador.guardar(self.criar_memento())
        self.tarefas.append(Tarefa(titulo, descricao))
        print("Tarefa adicionada.")

    def editar_tarefa(self, posicao, novo_titulo, nova_descricao):
        if not self.posicao_valida(posicao):
            print("Posição inválida.")
            return
        self.zelador.guardar(self.criar_memento())
        tarefa = self.tarefas[posicao - 1]
        tarefa.set_titulo(novo_titulo)
        tarefa.set_decricao(nova_descricao)
        print("Tarefa editada.")

    def remover_tarefa(self, posicao):
        if not self.posicao_valida(posicao):
            print("Posição inválida.")
            return
        self.zelador.guardar(self.criar_memento())
        self.tarefs.pop(posicao - 1)
        print("Tarefa removida.")

    def desfazer(self):
        memento = self.zelador.recuperar()
        if memento is None:
            print("Não há nada para desfazer.")
            return
        self.restaurar_memento(memento)
        print("Última ação desfeita.")

    def posicao_valida(self, posicao):
        return 1 <= posicao <= len(self.tarefas)

    def listar_tarefas(self):
        if len(self.tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
            return
        for i, tarefa in enuerate(self.tarefas, start=1):
            print(f"{i}. {tarefa.get_titulo()} - {tarefa.get_descricao()}")


def ler_numero(texto):
    try:
        return int(input(texto))
    except ValueError:
        return 0


def mostrar_menu():
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Editar tarefa")
    print("3 - Remover tarefa")
    print("4 - Listar tarefas")
    print("5 - Desfazer última ação")
    print("0 - Sair")


def principal():
    gerenciador = GerenciadorDeTarefas()
    opcao = -1
    while opcao != 0:
        mostrar_menu()
        opcao = ler_numero("Escolha uma opção: ")

        if opcao == 1:
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            gerenciador.adicionar_taefa(titulo, descricao)
        elif opcao == 2:
            gerenciador.listar_tarefas()
            posicao = ler_numero("Número da tarefa a editar: ")
            titulo = input("Novo título: ")
            descricao = input("Nova descrição: ")
            gerenciador.editar_tarefa(posicao, titulo, descricao)
        elif opcao == 3:
            gerenciador.listar_tarefas()
            posicao = ler_numero("Número da tarefa a remover: ")
            gerenciador.remover_tarefa(posicao)
        elif opcao == 4:
            gerenciador.listar_tarefas()
        elif opcao == 5:
            gerenciador.desfazer()
        elif opcao == 0:
            print("Encerrando...")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    principal()
