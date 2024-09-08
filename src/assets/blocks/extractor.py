import zipfile, shutil, os, json

output = {}
print("正在计算文件数量...")
jarfile = zipfile.ZipFile("jarfile.jar")
filelist = jarfile.filelist
resultlist = []
for file in filelist:
    if file.filename.endswith(".png") and file.filename.startswith(
        "assets/minecraft/textures/block/"
    ):
        resultlist.append(file.filename)
total = len(resultlist)
print("正在解压...")
for file in resultlist:
    current = resultlist.index(file) + 1
    print(
        f"进度：[{'='*(int(current/total*10))}{'-'*(10-int(current/total*10))}] {current/total*100:.1f}%",
        end="\r",
        flush=True,
    )
    jarfile.extract(file, "textures")
print("")
print("正在整理...")
shutil.copytree(
    "textures/assets/minecraft/textures/block/", "textures/", dirs_exist_ok=True
)
shutil.rmtree("textures/assets")
print("正在加载语言文件...")
langfile: dict = json.load(open("langfile.json", encoding="utf-8"))
print("正在生成方块表...")
for i in resultlist:
    currentID: str = os.path.splitext(os.path.basename(i))[0]
    currentName = langfile.get(f"block.minecraft.{currentID}")
    if currentName:
        output[currentID] = currentName
print("正在输出...")
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
print("完成！")
