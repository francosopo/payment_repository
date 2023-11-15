import requests

def getToken(url):
    res = requests.get(url)
    print(res)
    return requests.get(url).json()

def sendPayment(url, token):
    return requests.post(url, json={
        "transferCode": "franco.seguel@ug.uchile.cl",
        "amount": 5000
    },
    headers={
        "Authorization": f"Bearer {token}"
    }).json()

url = "http://localhost:5000"
token = getToken(url + "/token")["token"]
payment = sendPayment(url + "/payment", token)
print(payment)


