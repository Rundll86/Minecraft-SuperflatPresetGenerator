import threading, time


def progress():
    num = 0
    chars = "-\\|/"
    while processing:
        print(
            f"[ {chars[num]} ] 正在生成贴图表与方块表，请稍后...", end="\r", flush=True
        )
        num = (num + 1) % len(chars)
        time.sleep(0.2)


processing = True
threading.Thread(target=progress).start()
import zipfile, shutil, os, json, msvcrt

output = {}
jarfile = zipfile.ZipFile("jarfile.jar")
filelist = jarfile.filelist
resultlist = []
for file in filelist:
    if file.filename.endswith(".png") and file.filename.startswith(
        "assets/minecraft/textures/block/"
    ):
        resultlist.append(file.filename)
for file in resultlist:
    jarfile.extract(file, "textures")
shutil.copytree(
    "textures/assets/minecraft/textures/block/", "textures/", dirs_exist_ok=True
)
shutil.rmtree("textures/assets")
alias = json.load(open("alias.json", encoding="utf-8"))
for i in alias:
    output[i["id"]] = i["name"]
    shutil.copyfile(f"textures/{i['texture']}.png", f"textures/{i['id']}.png")
shutil.copytree("textures", "../../../public/textures", dirs_exist_ok=True)
langfile: dict = json.load(open("langfile.json", encoding="utf-8"))
for i in resultlist:
    currentID: str = os.path.splitext(os.path.basename(i))[0]
    currentName = langfile.get(f"block.minecraft.{currentID}")
    if currentName:
        output[currentID] = currentName
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
print("\n完成！按下任意键退出")
processing = False
msvcrt.getch()
