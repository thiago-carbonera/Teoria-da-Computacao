Q = ['q0', 'q1', 'q2']
Sigma = ['a', 'b']
delta = { ('q0','a'): 'q1', ('q0','b'): 'q1', ('q1','a'): 'q2', ('q1','b'): 'q2', ('q2','a'): 'q0', ('q2','b'): 'q0'}
F = ['q0']



def AFD(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    qA = q0
    for x in cadeia:
        qA = delta[(qA, x)]
    return qA in F