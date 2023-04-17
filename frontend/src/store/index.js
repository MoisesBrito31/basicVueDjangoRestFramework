import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    contador: 0
  },
  getters: {	  
    contador(state){
      return state.contador
    }
  },
  mutations: {	
    soma(state){
      state.contador++
    },
    sub(state){
      state.contador--
    }  
  },
  actions: {
  },
  modules: {
  }
})
