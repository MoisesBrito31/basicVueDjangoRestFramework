<template>
  <div>
    <div class="bg-danger">
      <router-link to="/">Home</router-link>
      <router-link to="/page1/">pagina 1</router-link>
      <router-link to="/page2/">pagina 2</router-link>
      <router-link to="/page3/">pagina 3</router-link>
    </div>
    <router-view></router-view>
    
  </div>
</template>

<script>


export default {
  name: 'App-v',
  components: { 
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
