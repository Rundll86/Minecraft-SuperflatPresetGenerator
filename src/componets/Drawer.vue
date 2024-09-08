<template>
    <div class="drawer" :style="{
        maxHeight: showing ? '1000px' : `${showHeight}px`
    }">
        <div class="title" @click="showing = !showing" ref="title">
            <span>{{ showing ? '收起' : '展开' }}</span>
            {{ title }}
        </div>
        <div class="content" :style="{
            transform: showing ? 'scale(1,1)' : 'scale(1,0)',
            opacity: showing ? '1' : '0'
        }">
            <slot></slot>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Drawer',
    props: {
        title: {
            type: String,
            default: ''
        },
        currentState: {
            type: Boolean,
            default: true
        }
    },
    data() {
        return {
            showing: this.currentState,
            showHeight: 0
        }
    },
    mounted() {
        this.showHeight = this.$refs.title.clientHeight;
    }
}
</script>
<style scoped>
.drawer {
    overflow: hidden;
    display: flex;
    flex-direction: column;
    margin: 5px;
    border: gray 2px solid;
    border-radius: 5px;
    padding: 5px;
}

.content {
    display: flex;
    flex-direction: column;
    transform-origin: 50% 0;
}

.title {
    padding: 5px;
    font-size: 14px;
    border-radius: 5px;
}

.title:hover {
    cursor: pointer;
    background-color: rgba(0, 0, 0, 0.2)
}
</style>