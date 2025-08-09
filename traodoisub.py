from modules import *

class TraodoisubAPI:
    def __init__(self, tds_cookie=None, tds_token=None):
        self.headers = {
            "cookie": tds_cookie
        }
        self.tds_token = tds_token

    def get_id_facebook_account(self, link: str):
        try:
            response = scraper.post(
                "https://id.traodoisub.com/api.php",
                data={"link": link},
                headers=self.headers,
                timeout=10
            )
            if response.json()["success"] == 200:
                return response.json()["id"]
            else:
                return "error"
        except:
            return "error"
        
    def setup_worker_account(self, account_link: str):
        try:
            facebook_account_id = self.get_id_facebook_account(account_link)
            if facebook_account_id == "error":
                return facebook_account_id
            
            response = scraper.get(
                f"https://traodoisub.com/api/?fields=run&id={facebook_account_id}&access_token={self.tds_token}",
                timeout=10
            )

            if "error" in response.json():
                return response.json()["error"]
            elif "success" in response.json():
                return response.json()['data']['msg']
        except:
            return "error"
        
    def get_task_facebook_fanpage(self, debug=False):
        try:
            response = scraper.post(
                f'https://traodoisub.com/ex/fanpage/load.php',
                headers=self.headers,
                timeout=10
            )
            if debug:
                input(response.text)
            if "error" in response.json():
                return "error"
            elif "coin" in response.json():
                return response.json()['data']
        except:
            return "error"
        
    def get_coin_in_fanpage_task(self, target_facebook_id):
        try:
            response = scraper.post(
                f'https://traodoisub.com/ex/fanpage/nhantien.php',
                headers=self.headers,
                data={"id": target_facebook_id, "type": "fanpage"},
                timeout=10
            )
            if response.text == "2":
                return "success"
            else:
                return "error"
        except:
            return "error"
        
    def get_current_coin(self):
        try:
            response = scraper.get(f'https://traodoisub.com/scr/user.php', headers=self.headers, timeout=10)
            if "xu" in response.json():
                return response.json()['xu']
            else:
                print(response.text)
                return "error"
        except:
            print(response.text)
            return "error"

if __name__ == "__main__":
    tds = TraodoisubAPI(
        tds_token="TDS0nI4IXZ2V2ciojIyVmdlNnIsISM2gjMn5Wak92Y1hGciojIyV2c1Jye",
        tds_cookie="PHPSESSID=67d5d708a4cb0c994d2cc604036ec3d1"
    )

    r = tds.get_current_coin()
    print(r)

    print(tds.setup_worker_account("https://www.facebook.com/hoangphu020"))
    r = tds.get_task_facebook_fanpage()
    print(r)

    input(">>> ")

    r = tds.get_coin_in_fanpage_task(r[0]['id'])
    print(r)
    r = tds.get_current_coin()
    print(r)