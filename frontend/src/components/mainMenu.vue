<template> 
    <div>
        <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand href="/">
      <img class="mr-3" src="../assets/logo.jpeg" width="120" height="40">
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-button variant="info" @click="gourl('')" >Home</b-button>
        <b-button variant="info" @click="gourl('page1')" >Pagina 1</b-button>
        <b-button variant="info" @click="gourl('page2')" >Pagina 2</b-button>
        <b-button variant="info" @click="gourl('login')" >Logar</b-button>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto mr-2" v-if="logado">
        <b-nav-item-dropdown right>
          <template #button-content>
            <em>
              Olá {{getName}}
              <b-avatar v-if="getAlertas>0" :badge="getAlertas" badge-variant="warning" :src="getAvatar"></b-avatar>
              <b-avatar v-else :src="getAvatar"></b-avatar>
            </em>
          </template>
          <div>
             <b-button @click="logout" variant="primary">sair</b-button>
          </div>
        </b-nav-item-dropdown>
      </b-navbar-nav>

    </b-collapse>
  </b-navbar>
       
    </div>
</template> 

<script lang="js">
  import { mapGetters } from 'vuex';  
  import Cookies from 'js-cookie' 
  export default {
    name: 'mainMenu',
    computed:{...mapGetters(['logado','getName','getAlertas','getDominio','getAvatar'])},
    methods:{
        gourl(url){
            this.$router.push(`/${url}`);
        },
        async logout(){
            Cookies.remove('token')
            this.gourl('')
        }
    }
  }
</script>