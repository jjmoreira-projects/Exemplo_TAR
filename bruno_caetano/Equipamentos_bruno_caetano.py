with open("devices.txt", "r") as arquivo:
    # Guardar todos os equipamentos do ficheiro de texto numa lista
    lista_equipamentos = [linha.strip() for linha in arquivo]

# Perguntar ao utilizador pelo equipamento a procurar
while True:
    nome_equipamento = input("Equipamento a procurar (sair p/terminar): ")

    # Verificar se o utilizador deseja sair
    if nome_equipamento.lower() == "sair":
        break

    # Procurar na lista de equipamentos
    quant = 0
    for equip in lista_equipamentos:
        if nome_equipamento.lower() in equip.lower():
            quant += 1
            print(equip)

    # Apresentar a quantidade
    if quant == 0:
        print("Equipamento Não existe na Lista!")
    else:
        print(f"Quantidade: {quant}")
import requests
import xml.etree.ElementTree as ET
resp = requests.get("http://instituto.islagaia.pt/ws/wsrifa.asmx/Rifa")
print(resp)
print()
print(resp.content)
root = ET.fromstring(resp.content)
print(root.text)
