## Variáveis globais.
resultado = []
palavras = []
achados = {}
## Entradas.
n_char, m_borradas, k_comprimento = map(int, input().split())
senha = input()

for i in range(m_borradas):
    palavra = input()
    palavras.append(palavra)
    
p_ordem = int(input())

## Permutações com as letras.
def permutar(d_senha, altura = 0): 
    #No final, adicionar resultado à lista.
    if altura == m_borradas:            
        return resultado.append(d_senha)

    for letra in palavras[altura]:      
        prm_senha = d_senha.replace("#", letra, 1)  #Substitui '#' pela letra
        permutar(prm_senha, altura + 1)
        
        

permutar(senha)

##Ordenação lexicográfica.
resultado_ordenado = sorted(resultado)

print(resultado_ordenado[p_ordem - 1])