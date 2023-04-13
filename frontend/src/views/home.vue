<template>
  <div>
    <div>
    <h1>pagina de boas vindas</h1>
    <p>essa pagina não precisa de acesso</p>
  </div>
    <img alt="Vue logo" src=".././assets/logo.png">
    <login dominio="http://localhost:8000/"></login>
  </div>
</template>
  
  <script>
  import login from '../components/loginToken.vue'
  export default {
    name: 'Home-v',
    components:{
      login
    }
  }
  </script>
  
  