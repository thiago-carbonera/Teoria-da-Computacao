Q = ['q0', 'q1', 'q2','q3','q4']
Sigma = ['a', 'b']
delta = { ('q0','a'): 'q1', ('q0','b'): 'q2', ('q1','a'): 'q0', ('q1','b'): 'q3', ('q2','a'): 'q4', ('q2','b'): 'q3', ('q3','a'): 'q4', 
         ('q3','b'): 'q2', ('q4','a'): 'q4', ('q4','b'): 'q4'}
F = ['q0','q3']



def AFD(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    qA = q0
    for x in cadeia:
        qA = delta[(qA, x)]
    return qA in F