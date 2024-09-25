<template>
  <main>
    {{ data }}
    <button @click="send(JSON.stringify({'message': 'hello world'}))">SEND MESSAGE</button>
  </main>
</template>
<script setup>
import { useWebSocket } from '@vueuse/core'

const { data, send } = useWebSocket('ws://0.0.0.0:3000/ws/chat/', {
  autoReconnect: {
    retries: 3,
    delay: 1000,
    onFailed() {
      alert('Failed to connect WebSocket after 3 retries')
    }
  }
})
</script>
