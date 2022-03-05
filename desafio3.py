import math

def desafio3(string):
    # obtem o valor para manipulação
    texto = string # str("o rato roeu a roupa do rei de roma")

    ## string sem os espaços
    string_de_texto_sem_espaco = texto.replace(' ', '')

    # tamanho total do texto
    tamanho_do_texto = int(len(string_de_texto_sem_espaco))

    # calcula a raiz do tamanho da string
    raiz_tamanho_string = int(math.ceil(math.sqrt(tamanho_do_texto)))

    # anucia o acumulo de raizes de cada loop em execução
    obtemIndex = 0

    # declarão de variaveis
    lista_de_rizes = []
    list_texto = string_de_texto_sem_espaco.split(' ')
    calc, message = 0, ""

    # pecorrendo a lista de string
    for indice, el in enumerate(list_texto[0]):
        obtemIndex += 1
        calc = obtemIndex * raiz_tamanho_string

        # monitora e faz o controle nas colunas do grid
        if calc == raiz_tamanho_string:
            message += "\r" + string_de_texto_sem_espaco[:raiz_tamanho_string]
        else:
            message += f"\n\r{string_de_texto_sem_espaco[(calc - raiz_tamanho_string):calc]}"

    # gerando saida para o valor gerado na grid
    array_matriz = message.strip()
    print(array_matriz)





