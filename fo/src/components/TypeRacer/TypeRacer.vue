<template>
  <div class="type-racer">
    <TypeRacerTrack :progress="progress" class="margin-bottom" />
    <TypeRacerTextBox
      :word="word"
      :text="text"
      @next-word="onNextWord"
      @is-wrong="onWrong"
      @is-success="onSucess"
      @on-progress="onProgress"
    />
    <input type="text" v-model="word" :class="currentInputWrong ? 'danger' : ''" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import TypeRacerTextBox from "./TextBox.vue"
import TypeRacerTrack from "./RaceTrack.vue"

defineProps({
  text:{
    type:String,
    default:"Hello world this is type racer game"
  }
})

const word = ref('')
const currentInputWrong = ref(false)
const progress = ref(0)

const onProgress = (val) => {
  progress.value = val
}

const onNextWord = () => {
  word.value = ''
}

const onWrong = () => {
  currentInputWrong.value = true
}

const onSucess = () => {
  currentInputWrong.value = false
}
</script>

<style scoped>
.type-racer {
  max-width: 784px;
  margin: auto;
  text-align: center;
}

input {
  margin-top: 32px;
  font-size: 18px;
  padding: 4px 8px;
  outline: none;
  border-radius: 8px;
}

input.danger {
  color: red;
}

.margin-bottom {
  margin-bottom: 48px;
}
</style>
