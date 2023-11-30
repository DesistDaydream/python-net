import requests


class Client(object):
    def __init__(self, baseAPI: str):
        self.BaseAPI: str = baseAPI
        self.Token: str = ""

    def NewClient(self, clientID, clientSecret):
        url = f"{self.BaseAPI}/open/auth/token"
        r = requests.get(url, params={"client_id": clientID, "client_secret": clientSecret})
        if r.status_code == 200:
            self.Token = r.json()["data"]["token"]
            print("登录成功")
        else:
            print(f"登录失败 => {r.json()['message']}")
            exit(0)

    def makeRequest(self, method: str, endpoint: str, params=None, body=None):
        url = f"{self.BaseAPI}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.Token}",
            "Content-Type": "application/json;charset=UTF-8",
        }
        response = requests.request(method, url, params=params, json=body, headers=headers)
        return response

    def makeResponse(self, r: requests.Response, status, name: str):
        if status == 200:
            return r.json()["data"]
        else:
            print(f"{name}环境变量失败 => {r.json()['message']}")
            exit(0)


class Environments(Client):
    def __init__(self, client: Client):
        self.BaseAPI = client.BaseAPI
        self.Token = client.Token

    # 列出全部环境变量
    def ListEnvironments(self):
        endpoint = "/open/envs"
        r = self.makeRequest("GET", endpoint)
        return self.makeResponse(r, r.status_code, "列出")

    # 根据环境变量名获取指定环境变量
    def GetEnvironment(self, env_name: int):
        endpoint = f"/open/envs?searchValue={env_name}"
        r = self.makeRequest("GET", endpoint)
        return self.makeResponse(r, r.status_code, "获取")

    # 根据环境变量 ID 获取环境变量
    def GetEnvironmentByID(self, env_id: int):
        pass