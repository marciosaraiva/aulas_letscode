#!/usr/bin/env python
# coding: utf-8
# %%
def verifica_cpf(cpf):
    cpf = cpf.replace(".","").replace("-","")
    cpf_valido = True

    lista_numeros_cpf = [int(n) for n in cpf]

    soma_nove_digitos = 0
    for index in range(9):
        resultado_do_numero = 0
        for valor in range(1,10):
            resultado_do_numero += valor * lista_numeros_cpf[index]

        soma_nove_digitos+= resultado_do_numero

    soma_nove_digitos*=10

    resto = soma_nove_digitos%11

    if lista_numeros_cpf[9]!=resto:
        cpf_valido = False


    soma_dez_digitos = 0
    for index in range(10):
        resultado_do_numero = 0
        for valor in range(1,10):
            resultado_do_numero += valor * lista_numeros_cpf[index]

        soma_dez_digitos+= resultado_do_numero

    soma_dez_digitos*=10

    resto = soma_dez_digitos%11

    if lista_numeros_cpf[10]!=resto:
        cpf_valido = False


    if cpf_valido:
        return True 
        # 113.451.253-80
    else:
        return False
        # 313.541.102-74


# %%
def quantidade_de_notas(valor):
    print(valor)

    lista_notas = [100,50,20,10,5,2,1] 

    for nota in lista_notas: 
        qtd = valor//nota
        valor = valor%nota
        print("{} nota(s) de R$ {},00".format(qtd, nota))


# %%
def quantidade_de_notas_arquivo(nome, valor):
    texto = str(valor)+"\n"

    lista_notas = [100,50,20,10,5,2,1] 

    for nota in lista_notas: 
        qtd = valor//nota
        valor = valor%nota
        texto+="{} nota(s) de R$ {},00".format(qtd, nota)+"\n"
    
    with open("carteira_"+nome+".txt", "a+") as arquivo:
        arquivo.write(texto)
