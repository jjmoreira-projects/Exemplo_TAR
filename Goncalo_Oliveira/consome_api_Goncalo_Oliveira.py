import requests
import xml.etree.ElementTree as ET
resp = requests.get("http://instituto.islagaia.pt/ws/wsrifa.asmx/Rifa")
print(resp)
print()
print(resp.content)
root = ET.fromstring(resp.content)
print(root.text)
