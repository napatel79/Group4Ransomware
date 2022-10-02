from os import lseek
import requests
import time 

class CheckWallet:
    
    def __init__(self):
        self.btc_address = '34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo'
        
    def getBalance(self):
        api_key = 'xa5WGz7Z2H2VJISn19q0jB45SOt8MBYAw7O77VNiU00'
        url = 'https://www.blockonomics.co/api/balance'
        headers = {'Authorization': 'Bearer ' + api_key}
        r = requests.post(
            url, data=f'{{"addr": "{self.btc_address}"}}', headers=headers)
        if r.status_code == 200:
            json = r.json()
            return json.get('response')[0].get('confirmed', 0)/100000000
        print(r.status_code, r.text)
        return 0

    def waitForDeposit(self):
        balance = self.getBalance()
        newBalance = float(balance)+.025
        run = 1
        while float(balance) < float(newBalance) and run !=0:
            time.sleep(45)
            balance = self.getBalance()
            run -= 1
        print("done waiting")
        return True
