<template>
    <div>
        <img :src="'/textures/' + block_ + '.png'">
        <select name="blockid" v-model="block_" :id="isSelector ? 'selector' : 'not-selector'">
            <option v-for="block in blockIDs.filter(block => blocks[block].toLowerCase().includes(nameFilter.toLowerCase()))" :value="block">
                {{ blocks[block] }}
            </option>
        </select>
    </div>
</template>
<script setup>
import blocks from "../assets/blocks/output.json"
const blockIDs = Object.keys(blocks)
</script>
<script>
export default {
    name: 'BlockSelector',
    props: {
        block: {
            type: String,
            default: 'stone'
        },
        isSelector: {
            type: Boolean,
            default: false
        },
        nameFilter: {
            type: String,
            default: ''
        }
    },
    data() {
        return {
            block_: this.block
        }
    },
}
</script>
<style scoped>
div {
    display: inline-flex;
    align-items: center;
    margin: 5px;
}

select,
input {
    margin: 0 5px;
}

img {
    width: 16px;
    height: 16px;
}
</style>