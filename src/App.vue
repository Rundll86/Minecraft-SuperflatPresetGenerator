<script setup>
import AlignItems from "./componets/AlignItems.vue";
import BlockLayer from "./componets/BlockLayer.vue";
import BlockSelector from "./componets/BlockSelector.vue";
import JustifyContent from "./componets/JustifyContent.vue";
</script>
<script>
import { h, render } from "vue";
import TextCenter from "./componets/TextCenter.vue";
import blocks from "./assets/blocks/output.json";
const blockIDs = Object.keys(blocks);
export default {
  methods: {
    addLayer() {
      let vnode = h(BlockLayer, { block: document.getElementById("selector").value });
      console.log(vnode);
      this.$nextTick(() => {
        let temp = document.createElement("div");
        render(vnode, temp);
        document.getElementById("layers").appendChild(temp.firstElementChild);
      });
    },
    updatePreviewImages() {
      const { blockDrawWidth, previewWidth } = this;
      const layersElement = document.querySelectorAll('#layers > *');
      let layers = [];
      this.canvasContext.clearRect(0, 0, this.canvas.width, this.canvas.height);
      layersElement.forEach((layer) => {
        for (let i = 0; i < layer.querySelector("input").value; i++)layers.push(layer.querySelector("select").value);
      });
      layers.reverse();
      this.canvas.width = previewWidth * blockDrawWidth;
      this.canvas.height = layers.length * blockDrawWidth;
      for (let i = 0; i < layers.length; i++) {
        const layer = layers[i];
        const block = layer;
        for (let j = 0; j < previewWidth; j++) {
          this.canvasContext.drawImage(this.blockImages[block], blockDrawWidth * j, blockDrawWidth * i, blockDrawWidth, blockDrawWidth);
        }
      }
    },
    generatePreset() {
      const layers = document.querySelectorAll('#layers > *');
      let preset = [];
      for (let i = 0; i < layers.length; i++) {
        const layer = layers[i];
        preset.push(layer.querySelector("input").value + "*" + layer.querySelector("select").value);
      };
      let result = preset.join(",");
      result += ";plains";
      alert(result);
    },
    mergeLayersOneStep() {
      const layers = document.querySelectorAll('#layers > *');
      let lastMergedType = null;
      let isMergedOne = false;
      for (let i = 0; i < layers.length; i++) {
        if (i + 1 === layers.length) break;
        const layerA = layers[i];
        const layerB = layers[i + 1];
        const blockA = layerA.querySelector("select").value;
        const valueA = parseInt(layerA.querySelector("input").value);
        const blockB = layerB.querySelector("select").value;
        const valueB = parseInt(layerB.querySelector("input").value);
        if (blockA === blockB && lastMergedType !== blockA) {
          lastMergedType = blockA;
          isMergedOne = true;
          layerB.querySelector("input").value = valueA + valueB;
          layerA.remove();
        }
      }
      if (isMergedOne) {
        this.mergeLayersOneStep();
      }
    }
  },
  data() {
    return {
      nameFilter: "",
      previewWidth: 7,
      blockDrawWidth: 16,
      /**
       * @type {HTMLCanvasElement}
       */
      canvas: null,
      /**
       * @type {CanvasRenderingContext2D}
       */
      canvasContext: null,
      blockImages: {}
    };
  },
  mounted() {
    const { previewer } = this.$refs;
    this.canvas = previewer;
    this.canvasContext = this.canvas.getContext("2d");
    blockIDs.forEach(block => {
      const img = new Image();
      img.src = `/textures/${block}.png`;
      this.blockImages[block] = img;
    });
    this.mergeLayersOneStep();
  }
}
</script>
<template>
  <div id="controls">
    <AlignItems>
      <TextCenter>
        <JustifyContent id="panel">
          <button @click="generatePreset">生成预设代码</button>
          <button @click="mergeLayersOneStep">合并同类项</button>
          <button @click="addLayer">添加层</button>
          <BlockSelector isSelector :nameFilter="nameFilter" id="block-selector" />
          <input type="text" v-model="nameFilter" placeholder="搜索方块..." /><br>
          预览世界尺寸：{{ previewWidth }}<input type="range" max="50" min="1" step="1" v-model="previewWidth" />
          预览方块大小：{{ blockDrawWidth }}<input type="range" max="160" min="8" step="1" v-model="blockDrawWidth" />
          <button @click="updatePreviewImages">生成预览</button>
        </JustifyContent>
      </TextCenter>
    </AlignItems>
    <br>
    <div id="layers">
      <BlockLayer block="bedrock" />
      <BlockLayer block="dirt" />
      <BlockLayer block="dirt" />
      <BlockLayer block="grass_block" />
    </div>
  </div>
  <canvas id="preview" ref="previewer"></canvas>
  <!-- <div id="overlay" v-if="Object.keys(blockImages).length !== blockIDs.length">
    <span>正在加载方块贴图，{{ Object.keys(blockImages).length }}/{{ blockIDs.length }}</span>
  </div> -->
</template>
<style>
* {
  margin: 0;
  padding: 0;
  transition: all .1s ease-out;
}

button {
  padding: 3px 6px;
  margin: 5px;
  border: gray 2px solid;
  border-radius: 5px;
  color: black;
}

button:hover {
  background-color: gray;
  color: white;
}

body,
#app {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 10px
}

body {
  height: 100vh;
  overflow: hidden;
}

#app {
  overflow: auto;
  display: block;
}

#layers {
  display: flex;
  flex-direction: column;
}

img.previewer {
  width: 32px;
  height: 32px;
}

#panel {
  flex-direction: column;
  display: inline-flex;
}

#controls {
  position: fixed;
  left: 10px;
  top: 10px;
  background-color: rgba(0, 0, 0, 0.1);
  border: rgba(0, 0, 0, 0.4) 2px solid;
  border-radius: 10px;
  padding: 10px;
  backdrop-filter: blur(5px);
}

input[type="number"] {
  width: 40px;
}

input,
select {
  border: gray 2px solid;
  border-radius: 5px;
  padding: 2px 4px;
  outline: none;
}

input:hover,
select:hover,
input:focus,
select:focus {
  border-color: rgb(54, 54, 54);
}

#overlay {
  position: fixed;
  left: 0;
  top: 0;
  width: 100vw;
  min-height: 100vh;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 10;
  color: white;
  font-size: 2vw;
  font-weight: bold;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>