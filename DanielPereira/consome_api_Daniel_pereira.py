# instalar a biblioteca
# pip install requests
import requests
import xml.etree.ElementTree as ET


response = requests.get("http://instituto.islagaia.pt/ws/wscambio.asmx/cambioUSD")
print(response.text)
print()
print(response.content)
root = ET.fromstring(response.content)
print(root.text)

input("Press enter to exit;")