# abrir ficheiro de texto devices.txt
ficheiro = open("devices.txt", "r")

# definir uma lista para guardar em memoria os equipamentos
lista_equipamentos = []

# percorrer todo o ficheiro
for linha in ficheiro:
    #print(linha)
    linha = linha.strip() # retira espaços em branco
    #print(linha)
    lista_equipamentos.append(linha)

ficheiro.close()
print(lista_equipamentos)

#Perguntar Ficheiro

while True:
    nome_equipamento = input("Equipamento a procurar (sair p/terminar): ")

    if nome_equipamento == "sair":
            break # aborta o ciclo

    # mostrar apenas os equipamentos que correspondem
    quant = 0
    for item in lista_equipamentos:
        #if "Router" in item:
        if  nome_equipamento in item:
            quant = quant + 1 
            print(item)

    if quant == 0:
        print("Equipamento Não existe na Lista!")
    else:
        print(f"Quantidade:{quant}")
