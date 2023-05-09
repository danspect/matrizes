import random
import numpy as np

class Matrizes:

    def __init__(self) -> None:
        pass

    def transpor(self, matriz: np.ndarray) -> np.ndarray:
        """
        Retorna uma matriz transposta

        Sendo A = [ 1  4 ]
                  [ 2  5 ]
        
        A matriz transposta A seria At = [ 1  2 ]
                                         [ 4  5 ]

        Note que para uma matriz ser transposta precisamos
        reescreve-la inverter as posições dos índices i e j
        (ambos iguais a 1),ou seja, onde for ij reescrevemos
        ji e os índices m(linhas) e n(colunas):

        [ a(ij)       b(ij + 1)      ... c(in)      ]      [ a'(ji)       b'(ji + 1)      ...  c'(j m)      ]  
        [ d(i + 1 j)  e(i + 1 j + 1) ... f(i + 1 n) ] ---> [ d'(j + 1 i)  e(j + 1 i + 1)  ...  f(j + 1 m)   ]
        [ ...         ...            ...            ]      [ ...          ...             ...               ]
        [ g(m j)      h(m j + 1)     ... k(mn)      ]      [ g(n i)       h(n i + 1)      ...  k(nm)        ]

        note que 
        a' = a
        b' = d
        c' = g
        d' = b
        e' = e
        f' = h
        g' = c
        h' = f
        k' = k

        Assim, sendo uma matriz B = [ b  b' ... bn ]
                                    [ c  c' ... cn ]
                                    [ ...   ...    ]
                                    [ bm    ... mn ]

        Podemos escrever sua forma transposta desta maneira:

        Bt = [  b   ][  c  ][ bm ]
             [  b'  ][  c' ][ ...]
             [ ...  ][ ... ][ ...]
             [  bn  ][ cn  ][ mn ]
        """
        num_linhas = len(matriz)
        num_colunas = len(matriz[0])

        matriz_transposta = np.empty([num_colunas, num_linhas])

        for linha in range(num_linhas):
            for elemento in range(num_colunas):
                matriz_transposta[elemento][linha] = matriz[linha][elemento]

        return matriz_transposta

if __name__ == "__main__":
    matrizes = Matrizes()
    linhas, colunas = random.randint(1, 20), random.randint(1, 20)
    matriz = np.random.randint(1, 20, size=(linhas, colunas))
    print(f"Matriz original: \n{matriz}\n")
    matriz_transposta = matrizes.transpor(matriz)
    print(f"Matriz transposta: \n{matriz_transposta}\n")