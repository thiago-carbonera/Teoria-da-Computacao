from automata.fa.Moore import Moore

moore = Moore(
    ['q0', 'q1', 'q2', 'q3', 'q4', 'q5'], # estados
    ['0', '1'], # alfabeto
    ['0', '1'], #símbolos de saída
    { # transições
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q3', '1': 'q2'},
        'q3': {'0': 'q0', '1': 'q4'},
        'q4': {'0': 'q0', '1': 'q5'},
        'q5': {'0': 'q3', '1': 'q2'}
    },
    'q0', # estado inicial
    {'q0': '0', 'q1': '0', 'q2': '0', 'q3': '0', 'q4': '0', 'q5': '1'} # saída
)

print("Definição da Máquina de Moore:")
print(moore)

entrada = '11011011011'
print("\nEntrada:", entrada)
print("Saída:  ", moore.get_output_from_string(entrada))
