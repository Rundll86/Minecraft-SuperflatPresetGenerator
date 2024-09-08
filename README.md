# Minecraft超平坦预设生成器
## 启动服务
### 初始化
```bash
git clone https://github.com/Rundll86/Minecraft-SuperflatPresetGenerator.git
cd Minecraft-SuperflatPresetGenerator
npm install
```
### 生成贴图表与方块表
1.将你的Minecraft客户端jar文件复制到 `./src/assets/blocks` 中，将其重命名为 `jarfile.jar`

2.打开 `.minecraft/assets/indexes` 中你的客户端对应版本的json文件，按下 `Ctrl+F` 搜索你想要的翻译语言（例如`简体中文`搜索`zh_cn`），应该会找到一个名为 `minecraft/lang/语言.json` 的字段，复制这个字段下的hash字段的值

3.打开 `.minecraft/assets/objects`，搜索以刚获得的hash值作为名称的文件，将结果复制 `./src/assets/blocks` 中，将其命名为 `langfile.json`

4.运行 `./src/assets/blocks/extractor.py`，将会输出 `output.json` 与 `textures` 目录，将`textures`移动或复制到 `./src/public` 中