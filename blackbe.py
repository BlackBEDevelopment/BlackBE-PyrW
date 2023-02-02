from urllib.request import urlopen
import mc
import json

blackbeapi = "https://api.blackbe.work/openapi/v3/check?"


def join(e):
    url = blackbeapi + "name=" + e.name + "&xuid=" + e.xuid
    req = urlopen(url)
    if req.getcode() != 200:
        print("Apierror:errcode=" + str(req.getcode()))
        return False
    j = json.loads(req.read())
    if j["status"] == 2000:
        e.disconnect("BlackBE:正在断开连接")
        print("发现玩家" + e.name + "在BlackBE云端黑名单上，已断开连接！")
        print("详情链接：https://blackbe.work/detail/" + j["data"]["info"][0]["uuid"])
    return False


mc.setListener("onPlayerJoin", join)
