import requests
import codecs,json,hashlib

#cheatplugin_ori = requests.get("https://raw.githubusercontent.com/ottercorp/DalamudAssets/cn/UIRes/cheatplugin.json").json()
meta = requests.get("https://aonyx.ffxiv.wang/Dalamud/Asset/Meta").json()
print(f"Version: {meta['Version']}")
cheatplugin = []
for item in meta["Assets"]:
    if item["FileName"]=="UIRes/cheatplugin.json":
        cheatplugin = requests.get(item["Url"]).json()
        item["FileName"]="UIRes/cheatplugin_ori.json"

print(f"CheatLen: {len(cheatplugin)}")
for plugin in cheatplugin:
    print(plugin["Name"])
    plugin["AssemblyVersion"]="0.0.0.0"

with codecs.open("cheatplugin.json", "w") as f:
    json.dump(cheatplugin, f, indent=4)

with open("cheatplugin.json","rb") as f:
    bs = f.read()
    readable_hash = hashlib.sha1(bs).hexdigest().upper()

fakecheat = {
    "Url": "https://raw.githubusercontent.com/gamous/XIVLauncherEX/main/Asset/cheatplugin.json",
    "FileName": "UIRes/cheatplugin.json",
    "Hash": readable_hash}

meta["Assets"].append(fakecheat)

with codecs.open("meta", "w") as f:
    json.dump(meta, f, indent=4)

