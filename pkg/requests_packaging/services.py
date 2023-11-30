import core.core as core

if __name__ == "__main__":
    client = core.Client("http://192.168.254.253:5700")
    client.NewClient("","")

    envClient = core.Environments(client)
    envs = envClient.ListEnvironments()
    print(envs)