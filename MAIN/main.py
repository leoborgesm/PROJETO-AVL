import time
start_time = time.time()



class NO:
    def __init__(self,info):
        self.info = info
        self.altura = 0
        self.esq = None
        self.dir = None

class AVL:

    def __init__(self):
        self.__raiz = None

    def __altura(self, no):
        if(no == None):
            return -1
        else:
            return no.altura

    def __fatorBalanceamento(self, no):
        return abs(self.__altura(no.esq) - self.__altura(no.dir))    

    def __maior(self, x, y):
        if(x > y):
            return x
        else:
            return y

    def __RotacaoLL(self, A):
        print('RotacaoLL: ',A.info);
        B = A.esq
        A.esq = B.dir
        B.dir = A
        A.altura = self.__maior(self.__altura(A.esq),self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.esq),A.altura) + 1
        #A = B
        return B

    def __RotacaoRR(self, A):
        print('RotacaoRR: ',A.info);
        B = A.dir
        A.dir = B.esq
        B.esq = A
        A.altura = self.__maior(self.__altura(A.esq),self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.dir),A.altura) + 1
        #A = B
        return B

    def __RotacaoLR(self, A):
        A.esq = self.__RotacaoRR(A.esq)
        A = self.__RotacaoLL(A)
        return A
        
    def __RotacaoRL(self, A):
        A.dir = self.__RotacaoLL(A.dir)
        A = self.__RotacaoRR(A)
        return A

    def __insereValor(self,atual,valor):
        if(atual == None): # árvore vazia ou nó folha
            novo = NO(valor)
            return novo
        else:
            if(valor < atual.info):
                atual.esq = self.__insereValor(atual.esq, valor)
                if(self.__fatorBalanceamento(atual) >= 2):
                    if(valor < atual.esq.info):
                        atual = self.__RotacaoLL(atual)
                    else:
                        atual = self.__RotacaoLR(atual)
            else:
                atual.dir = self.__insereValor(atual.dir, valor)
                if(self.__fatorBalanceamento(atual) >= 2):
                    if(valor > atual.dir.info):
                        atual = self.__RotacaoRR(atual)
                    else:
                        atual = self.__RotacaoRL(atual)

            atual.altura = self.__maior(self.__altura(atual.esq),self.__altura(atual.dir)) + 1
            return atual                

    def insere(self, valor):
        if(self.busca(valor)):
            return False #valor já existe na árvore
        else:
            self.__raiz = self.__insereValor(self.__raiz, valor)
            return True

    
    def busca(self, valor):
        if(self.__raiz == None):
            return False

        atual = self.__raiz
        while(atual != None):
            if(valor == atual.info):
                return True
            
            if(valor > atual.info):
                atual = atual.dir
            else:
                atual = atual.esq
        
        return False   

    def __emOrdem(self,raiz):
        if(raiz != None):            
            self.__emOrdem(raiz.esq)
            print(raiz.info, end=' ')
            self.__emOrdem(raiz.dir)

    def emOrdem(self):
        if(self.__raiz != None):
            self.__emOrdem(self.__raiz)     

    
arv = AVL()


# Crie um dicionário para armazenar o índice das palavras e as linhas em que aparecem
indice = {}

with open('documento.txt', 'r') as arqv:
    linha_atual = 0
    for line in arqv:
        linha_atual += 1  # Incrementa o número da linha atual
        palavras = line.split()
        for palavra in palavras:
            palavra = "".join(c for c in palavra if c.isalpha()).lower()
            if palavra:  # Verifica se a palavra não está vazia após a limpeza
                if palavra in indice:
                    # Adicionar a linha atual à lista de linhas da palavra
                    indice[palavra].append(linha_atual)
                else:
                    # Inserir a palavra no índice com a linha atual
                    indice[palavra] = [linha_atual]

# Após o loop, o índice já está construído com as linhas em que as palavras aparecem

# Ordenar o índice alfabeticamente antes de imprimir
indice_ordenado = {k: v for k, v in sorted(indice.items())}

# Imprima o índice das palavras e as linhas em que aparecem em ordem alfabética
print("Índice:")
for palavra, linhas in indice_ordenado.items():
    print(f"{palavra} {', '.join(map(str, linhas))}")

# Imprima o número total de palavras e o número de palavras distintas
total_palavras = sum(len(linhas) for linhas in indice_ordenado.values())
num_palavras_distintas = len(indice_ordenado)
print(f"Número total de palavras: {total_palavras}")
print(f"Número de palavras distintas: {num_palavras_distintas}")

# tempo decorrido

end_time = time.time()
tempo_decorrido = end_time - start_time

# Imprima o tempo decorrido
print(f"Tempo de construção do índice usando árvore AVL: {tempo_decorrido:.3f}s")



with open('arquivo_saida.txt', 'a') as arq_saida:
    arq_saida.write("Indice:\n")
    arq_saida.write("\n")
    
    for palavra, linhas in indice_ordenado.items():
        arq_saida.write(f"{palavra} {', '.join(map(str, linhas))}\n")
    arq_saida.write("\n")   
    
    arq_saida.write(f"Numero total de palavras: {total_palavras}\n")
    arq_saida.write(f"Numero de palavras distintas: {num_palavras_distintas}\n")  
    arq_saida.write(f"Tempo de construcao do indice usando arvore AVL: {tempo_decorrido:.3f}s\n")







