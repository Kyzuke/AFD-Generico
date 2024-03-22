# Autor: Gabriel Silva Duarte
# Matrícula: 202220171
# Disciplina: Teoria da Computação - GCC108
# Trabalho Prático: Implementação Genérica de um Autômato Finito Determinístico (AFD)

# O código começa com a definição de uma classe AFD (Autômato Finito Determinístico). A classe tem os seguintes atributos:
class AFD:
    def __init__(self):
        # states: uma lista de strings que representa os estados do autômato.
        self.states = []
        # alphabet: uma lista de strings que representa o alfabeto do autômato.
        self.alphabet = []
        # transitions: um dicionário que mapeia uma tupla (estado atual, símbolo) para o estado de destino.
        self.transitions = {}
        # initial_state: uma string que representa o estado inicial do autômato.
        self.initial_state = None
        # accept_states: uma lista de strings que representa os estados de aceitação do autômato.
        self.accept_states = []

    # O método get_user_input é responsável por receber a entrada do usuário para definir o autômato. Ele pede ao usuário para digitar os estados,
    # o alfabeto, as transições, o estado inicial e os estados de aceitação. Ele valida as entradas do usuário e pede para que ele tente novamente.
    def get_user_input(self):
        print("Digite os estados separados por espaços:")
        self.states = input().split()

        print("Digite o alfabeto separado por espaços:")
        self.alphabet = input().split()

        print("Digite as transições na sequência de: estadual atual, símbolo e estado de destino. Separados por espaço, não vírgula.")
        print("Para finalizar, pressione Enter sem digitar nada.")

        # O loop while True é usado para que o usuário possa digitar as transições até que ele pressione Enter sem digitar nada.
        while True:
            transition = input()
            if not transition:
                break
            start_state, symbol, next_state = transition.split()
            if start_state not in self.states or next_state not in self.states or symbol not in self.alphabet:
                print("Transição inválida. Por favor, tente novamente.")
                continue
            self.transitions[(start_state, symbol)] = next_state

        print("Digite o estado inicial:")
        self.initial_state = input()
        if self.initial_state not in self.states:
            print("Estado inicial inválido. Por favor, tente novamente.")
            self.get_user_input()
            return

        print("Digite os estados de aceitação separados por espaços:")
        self.accept_states = input().split()
        if not all(state in self.states for state in self.accept_states):
            print("Estado(s) de aceitação inválido(s). Por favor, tente novamente.")
            self.get_user_input()

    # O método simulate é responsável por simular o autômato com uma string de entrada. Ele começa no estado inicial e, para cada símbolo da string
    # de entrada, ele verifica se há uma transição válida para o estado atual e o símbolo atual. Se houver, ele muda para o próximo estado. Se não
    # houver, ele retorna False. No final, ele verifica se o estado atual é um estado de aceitação e retorna True se for, False caso contrário.
    def simulate(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                return False
        return current_state in self.accept_states


# O código principal começa criando um objeto AFD e chamando o método get_user_input para definir o autômato. Em seguida, ele entra em um loop
# infinito que pede ao usuário para digitar uma string para testar o autômato. Se o usuário digitar "sair", o loop é encerrado. Caso contrário, o
# autômato é simulado com a string de entrada e o resultado é impresso na tela.
afd = AFD()
afd.get_user_input()

while True:
    test_string = input("Digite uma string para testar (ou 'sair' para encerrar): ")
    if test_string.lower() == "sair":
        break
    if afd.simulate(test_string):
        print("Aceito")
    else:
        print("Rejeitado")


# Exemplo de execução:
'''Digite os estados separados por espaços:
q0 q1 q2 q3
Digite o alfabeto separado por espaços:
a b 
Digite as transições na sequência de: estadual atual, símbolo e estado de destino. Separados por espaço, não vírgula.
Para finalizar, pressione Enter sem digitar nada.
q0 a q1
q1 a q0
q0 b q2
q2 b q0
q2 a q3
q3 a q2
q1 b q3 
q3 b q1

Digite o estado inicial:
q0
Digite os estados de aceitação separados por espaços:
q0
Digite uma string para testar (ou 'sair' para encerrar): aabb
Aceito
Digite uma string para testar (ou 'sair' para encerrar): aaabb
Rejeitado
Digite uma string para testar (ou 'sair' para encerrar): ab
Rejeitado
Digite uma string para testar (ou 'sair' para encerrar): abab
Aceito
Digite uma string para testar (ou 'sair' para encerrar): aaabbb
Rejeitado
Digite uma string para testar (ou 'sair' para encerrar): baab
Aceito
Digite uma string para testar (ou 'sair' para encerrar): sair'''