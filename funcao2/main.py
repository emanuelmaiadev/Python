import random

def lancar_dados():
    dado1 = random.randint(1, 6)  
    dado2 = random.randint(1, 6)  
    total = dado1 + dado2         
    return dado1, dado2, total

dado1, dado2, resultado = lancar_dados()
print(f'Tirou: {resultado}')
print(f'O valor do primeiro dado foi {dado1}')
print(f'O valor do segundo dado foi {dado2}')
