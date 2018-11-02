<template>
  <section class="container">
    <p
      v-for="(file, index) in files"
      :key="index">{{ file.basic.name }}</p>
  </section>
</template>

<script>
export default {
  data () {
    return {
      files: []
    }
  },
  async mounted () {
    this.files = await this.$axios.$get('/browse/')
  }
}
</script>

<style>

.container {
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
