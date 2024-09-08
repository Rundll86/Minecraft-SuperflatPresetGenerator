import zipfile, os

file = zipfile.ZipFile("BlockSheetsAndTextureSheets.zip", "w")
file.write("src/assets/blocks/output.json")
file.write("public/textures")
for root, dirs, files in os.walk("public/textures"):
    for f in files:
        file.write("public/textures/" + f)
