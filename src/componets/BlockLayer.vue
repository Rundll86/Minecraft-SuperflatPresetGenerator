<template>
    <form>
        <div>
            <BlockSelector :block="block_" />
            <input type="number" name="count" :value="count">
            <button type="button" @click="$el.remove()">删除层</button>
        </div>
    </form>
</template>
<script setup>
import { defineComponent } from "vue";
import BlockSelector from "./BlockSelector.vue";
</script>
<script>
export default defineComponent({
    name: 'BlockLayer',
    props: {
        block: {
            type: String,
            default: 'stone'
        },
        count: {
            type: Number,
            default: 1
        }
    },
    data() {
        return {
            block_: this.block
        }
    }
})
</script>
<style scoped>
div {
    display: flex;
    align-items: center;
    margin: 5px;
}

select,
input {
    margin: 0 5px;
}
</style>