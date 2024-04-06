# AFD-Genérico
Trabalho prático da disciplina de Teoria da Computação. Implementação Genérica de um Autômato Finito Determinístico (AFD)

Autor: Gabriel Silva Duarte
Matrícula: 202220171
Disciplina: Teoria da Computação - GCC108

# Autômato Finito Determinístico (AFD)
Este projeto é uma implementação genérica de um Autômato Finito Determinístico (AFD) em Python. Foi desenvolvido como parte do trabalho prático da disciplina Teoria da Computação.

# Descrição:
O programa permite ao usuário definir um AFD inserindo os estados, o alfabeto, as transições, o estado inicial e os estados de aceitação. Em seguida, o usuário pode testar o AFD com várias strings de entrada para ver se elas são aceitas ou rejeitadas.

# Como usar:
Execute o arquivo afd.py.
Quando solicitado, insira os estados do AFD, separados por espaços.
Insira o alfabeto do AFD, separado por espaços.
Insira as transições do AFD. Para cada transição, insira o estado atual, o símbolo recebido e o estado de destino, separados por espaços. Pressione Enter sem digitar nada para finalizar as transições.
Insira o estado inicial do AFD.
Insira os estados de aceitação do AFD, separados por espaços.
Agora você pode testar o AFD. Insira uma string para testar e o programa irá dizer se a string é aceita ou rejeitada. Digite 'sair' para encerrar o programa.

# Funções
A classe AFD possui dois métodos: get_user_input e simulate.

O método get_user_input solicita ao usuário que insira os estados, o alfabeto, as transições, o estado inicial e os estados de aceitação do autômato. Ele valida a entrada do usuário e solicita que ele tente novamente se a entrada for inválida.

O método simulate simula o autômato com uma string de entrada. Ele começa no estado inicial e, para cada símbolo na string de entrada, verifica se há uma transição válida para o estado atual e o símbolo atual. Se houver, ele passa para o próximo estado. Se não houver, retorna False. No final, verifica se o estado atual é um estado de aceitação e retorna True se for, e False caso contrário.

A parte principal do código cria um objeto AFD e chama o método get_user_input para definir o autômato. Em seguida, entra em um loop infinito que pede ao usuário que insira uma string para testar o autômato. Se o usuário inserir "sair", o loop é encerrado. Caso contrário, o autômato é simulado com a string de entrada e o resultado é impresso na tela.
