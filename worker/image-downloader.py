import os
import requests  # request img from web
import shutil  # save img locally

target = [
    {
        "name": "son-astonished",
        "value": "https://emoji.slack-edge.com/T02R0EL7S9J/son-astonished/3c0aeaba674ef209.png",
    },
    {
        "name": "son-blood-quest",
        "value": "https://emoji.slack-edge.com/T02R0EL7S9J/son-blood-quest/fe160e4d3614ba37.png",
    },
    {
        "name": "son-carrot",
        "value": "https://emoji.slack-edge.com/T02R0EL7S9J/son-carrot/3cc5880e64c7de05.png",
    },
    {
        "name": "son-covid",
        "value": "https://emoji.slack-edge.com/T02R0EL7S9J/son-covid/3a514cb4294644d9.png",
    },
    {
        "name": "son-peng-bbeggom",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_peng_bbeggom%2F5f5684d449e1d7ac.png"
    },
    {
        "name": "son-rabit-bbeggom",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_rabit_bbeggom%2F1541ce5166a8dc13.png"
    },
    {
        "name": "son-hmm",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_hmm%2F29ab6bd3aa90b1a7.png"
    },
    {
        "name": "son-bear-giggle",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_bear_giggle%2F005a4a743d6f9e2d.png"
    },
    {
        "name": "son-rabbit-hard",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_rabbit_hard%2F10eb225e14ccfb35.png"
    },
    {
        "name": "son-rabbit-hehe",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_rabbit_hehe%2F30b86d35251acffd.png"
    },
    {
        "name": "son-rabbit-happy",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_rabbit_happy%2Fca6f1c80304bb7ad.png"
    },
    {
        "name": "son-rabbit-panic",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_rabbit_panic%2F0e75168ae7601520.png"
    },
    {
        "name": "son-rabbit-scared",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_rabbit_scared%2F6f07d0754a346205.png"
    },
    {
        "name": "son-rabbit-hmm",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_rabbit_hmm%2Fe1ceeff864141cc8.png"
    },
    {
        "name": "son-bear-shock",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_bear_shock%2Fd7d1cdb9e55b0e72.png"
    },
    {
        "name": "son-bear-scorn",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_bear_scorn%2F0c287c316cf416d9.png"
    },
    {
        "name": "son-bear-lol",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_bear_lol%2F465d34ce8662ef15.png"
    },
    {
        "name": "son-twitch",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_twitch%2Fce1805ab4362b445.png"
    },
    {
        "name": "son-sneer",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_sneer%2F9cdf82f5f58533c1.png"
    },
    {
        "name": "son-hey",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_hey%2F85ce557c4135e1ae.png"
    },
    {
        "name": "son-twe",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_twe%2Fdf9db6478b1f28dc.png"
    },
    {
        "name": "son-peng-bbeggom",
        "value": "https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT024R44D2%2Fson_peng_bbeggom%2F5f5684d449e1d7ac.png"
    }
]

parentDir = "c:/dev/test/"
if not os.path.isdir(parentDir):
    os.mkdir(parentDir)

str = ""
for ele in target:
    url = ele["value"]
    fileName = ele["name"] + url[url.rfind("."): len(url)]
    str += "url = " + url + "\n"
    str += "fileLocation = " + parentDir + fileName + "\n\n"

with open(parentDir + "preview.txt", "w") as f:
    f.write(str)

for ele in target:
    url = ele["value"]
    fileName = ele["name"] + url[url.rfind("."): len(url)]
    destination = parentDir + fileName
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open(destination, "wb") as f:
            shutil.copyfileobj(res.raw, f)
        print("Image sucessfully Downloaded: ", destination)
    else:
        print("Image Couldn't be retrieved")
