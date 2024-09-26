<template>
  <main>
    <!-- <button @click="send(JSON.stringify({ message: 'hello world' }))">SEND MESSAGE</button> -->
  </main>
  <TypeRacer :text="gameData.paragraph" />
</template>
<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'
import { useFetch } from '@vueuse/core'
// import { useWebSocket } from '@vueuse/core'
import TypeRacer from '@/components/TypeRacer/TypeRacer.vue'

const route = useRoute()

const id = computed(() => route.params.id)
const { data: gameData } = useFetch(`http://127.0.0.1:8000/api/game/${id.value}`).get().json()

// const { send } = useWebSocket('ws://0.0.0.0:3000/ws/chat/', {
//   autoReconnect: {
//     retries: 3,
//     delay: 1000,
//     onFailed() {
//       alert('Failed to connect WebSocket after 3 retries')
//     }
//   }
// })
</script>
