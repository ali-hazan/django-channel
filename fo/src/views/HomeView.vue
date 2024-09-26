<template>
  <main>
    <div v-if="isFetching">Loading...</div>
    <div v-else>
      <div v-if="gameData.length">
          <div v-for="game in gameData" :key="game.id" class="bg-white rounded-lg py-12 px-16 hover:shadow-sm cursor-pointer">
            <h1>
              {{ game.title }}
            </h1>
            <RouterLink class="bg-red-600 text-white px-3 text-center py-1 w-full block rounded-md mt-4" :to="`/game/${game.id}`">Join</RouterLink>
          </div>
      </div>
      <div v-else>No game available!</div>
    </div>
  </main>
  <TypeRacer />
</template>
<script setup>
import { useFetch } from '@vueuse/core'

const { data: gameData, isFetching } = useFetch('http://127.0.0.1:8000/api/game/').get().json()
</script>
