# instalar a biblioteca
# pip install requests
import requests
import xml.etree.ElementTree as ET


response = requests.get("http://instituto.islagaia.pt/ws/wsrifa.asmx/Rifa")
print(response.text)
print()
print(response.content)
root = ET.fromstring(response.content)
print(root.text)

input()