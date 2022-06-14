import os
import requests  # request img from web
import shutil  # save img locally

dependsOnUrl = False # True
extension = '.png'
target = [
    # {
    #     "name": "son-astonished",
    #     "value": "https://emoji.slack-edge.com/T02R0EL7S9J/son-astonished/3c0aeaba674ef209.png",
    # }
    # {
    #   "name": "부탁할-때-대학일기1",
    #   "value": "https://item.kakaocdn.net/do/6090dd413202e6645bea7282f80be44e8f324a0b9c48f77dbce3a43bd11ce785"
    # },
    {
      "name": "test",
      "value": "https://dcimg5.dcinside.com/dccon.php?no=62b5df2be09d3ca567b1c5bc12d46b394aa3b1058c6e4d0ca41648b65ced266e7f14c04a1f84cae4cf517a44b1fb5e5084e411f8fc0a805bc754d93996f95fcbea733749c96b"
    }
]

parentDir = "c:/dev/test/"
if not os.path.isdir(parentDir):
    os.mkdir(parentDir)

str = ""
for ele in target:
    url = ele["value"]
    if (dependsOnUrl):
        extension = url[url.rfind("."): len(url)]
    fileName = ele["name"] + extension
    str += "url = " + url + "\n"
    str += "fileLocation = " + parentDir + fileName + "\n\n"

with open(parentDir + "preview.txt", "w") as f:
    f.write(str)

for ele in target:
    url = ele["value"]
    if (dependsOnUrl):
        extension = url[url.rfind("."): len(url)]
    fileName = ele["name"] + extension
    destination = parentDir + fileName
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open(destination, "wb") as f:
            shutil.copyfileobj(res.raw, f)
        print("Image sucessfully Downloaded: ", destination)
    else:
        print("Image Couldn't be retrieved")
