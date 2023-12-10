import requests
request = requests.get('http://instituto.islagaia.pt/ws/wsrifa.asmx/Rifa')
print(request.text)