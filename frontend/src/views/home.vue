<template>
  <div>
    <div>
    <h1>pagina de boas vindas</h1>
    <p>essa pagina não precisa de acesso</p>
  </div>
    <img alt="Vue logo" src=".././assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>
  
  <script>
  import HelloWorld from '.././components/HelloWorld.vue'
  export default {
    name: 'Home-v',
    components:{
      HelloWorld
    }
  }
  </script>
  
  