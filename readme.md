# Atividade Prática – Memento e Observer

Atividade da disciplina de Engenharia de Software (Universidade de Vassouras), implementada em **Python 3**, com programação orientada a objetos e nomes de classes, métodos e variáveis em português. Não é necessário instalar nenhuma biblioteca externa.

## Arquivos

| Arquivo | Descrição |
|---|---|
| `questao1_memento.py` | Gerenciador de tarefas com função de desfazer (padrão Memento) |
| `questao2_observer.py` | Venda de ingressos com notificações automáticas (padrão Observer) |

## Como executar

```bash
python3 questao1_memento.py
python3 questao2_observer.py
```

No Windows, use `python` no lugar de `python3`.

---

## Questão 1 – Padrão Memento

### Objetivo
Permitir adicionar, editar e remover tarefas, com a opção de **desfazer a última ação** a qualquer momento.

### Classes

| Classe | Papel no padrão | Responsabilidade |
|---|---|---|
| `Tarefa` | – | Guarda `titulo` e `descricao`, com getters e setters |
| `GerenciadorDeTarefas` | Originador | Gerencia a lista de tarefas, cria mementos (`criar_memento`) e restaura estados (`restaurar_memento`) |
| `Memento` | Memento | Guarda uma cópia do estado da lista de tarefas |
| `Zelador` | Zelador (Caretaker) | Mantém o histórico de mementos em uma pilha, sem alterar o conteúdo deles |

### Como funciona
1. Antes de **adicionar, editar ou remover**, o gerenciador cria um memento com o estado atual e o entrega ao `Zelador`.
2. Em seguida, a alteração é feita normalmente.
3. Ao **desfazer**, o gerenciador pede ao `Zelador` o último memento e restaura a lista a partir dele.
4. O desfazer pode ser repetido várias vezes, voltando passo a passo no histórico. Quando a pilha está vazia, o sistema avisa que não há nada para desfazer.

O memento guarda **cópias** dos dados (tuplas de título e descrição), e não referências às tarefas. Assim, editar uma tarefa depois não altera o estado já salvo.

### Menu do programa
```
1 - Adicionar tarefa
2 - Editar tarefa
3 - Remover tarefa
4 - Listar tarefas
5 - Desfazer última ação
0 - Sair
```

---

## Questão 2 – Padrão Observer

### Objetivo
Criar um módulo de venda de ingressos para eventos esportivos (Cadeira Premium, Arquibancada e Camarote) que **notifica automaticamente** clientes e administradores quando o preço de um ingresso muda ou quando um novo desconto é cadastrado.

### Classes

| Classe | Papel no padrão | Responsabilidade |
|---|---|---|
| `Ingresso` | Sujeito (Subject) | Guarda tipo, preço, descontos e a lista de observadores; notifica a cada mudança |
| `Observador` | Interface do Observador | Define o método `atualizar(mensagem)` |
| `Cliente` | Observador concreto | Recebe e exibe as notificações como cliente |
| `Administrador` | Observador concreto | Recebe e exibe as notificações como administrador |
| `Desconto` | – | Representa um desconto de estudante ou por quantidade (com percentual e quantidade mínima) |

### Como funciona
- `adicionar_observador` e `remover_observador` controlam quem acompanha cada ingresso.
- `alterar_preco` muda o preço e chama `notificar_observadores`, informando o preço antigo e o novo.
- `adicionar_desconto` cadastra o desconto e também notifica todos os observadores.
- `calcular_preco_final(quantidade, estudante)` aplica os descontos válidos para a compra:
  - o desconto de **estudante** vale quando o comprador é estudante;
  - o desconto por **quantidade** vale quando a quantidade comprada atinge o mínimo definido.

### Demonstração (função `demonstrar`)
1. Cria os três tipos de ingresso e três interessados: os clientes Maria e João e o administrador Carlos.
2. Altera o preço da Arquibancada (R$ 80,00 → R$ 100,00) e do Camarote (R$ 500,00 → R$ 550,00).
3. Adiciona descontos de estudante (50%) e por quantidade (10% para 4 ou mais ingressos) na Arquibancada, e de estudante (20%) na Cadeira Premium.
4. Remove João da Arquibancada e altera o preço novamente, mostrando que ele deixa de ser notificado.
5. Simula preços finais, por exemplo: 1 ingresso de estudante na Arquibancada sai por R$ 45,00.

---

## Resumo dos padrões

| | Memento | Observer |
|---|---|---|
| **Problema resolvido** | Voltar a um estado anterior sem expor a estrutura interna do objeto | Avisar vários objetos automaticamente quando outro objeto muda |
| **Aplicação** | Desfazer ações no gerenciador de tarefas | Notificar clientes e administradores sobre preços e descontos |
