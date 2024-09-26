<template>
  <div class="track" ref="track">
    <div class="sprite" :style="computedXDirection">
      <img v-if="player === 1" src="/images/car1.png" />
      <img v-else src="/images/car2.png" />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useElementSize } from '@vueuse/core'

const props = defineProps({
  player: {
    type: Number,
    default: 1
  },
  playerName: {
    type: String,
    default: 'Guest'
  },
  progress: {
    type: Number,
    default: 0,
    validator(value) {
      return value >= 0 && value <= 100
    }
  }
})

const track = ref(null)
const { width } = useElementSize(track)

const computedXDirection = computed(() => {
  const position = ((width.value - 98) * props.progress) / 100
  return { transform: `translateX(${position}px)` }
})
</script>

<style scoped lang="css">
.track {
  background-color: #fafafa;
  border-bottom: 1px dashed #000;
}

.sprite img {
  width: 98px;
  display: block;
}
</style>
