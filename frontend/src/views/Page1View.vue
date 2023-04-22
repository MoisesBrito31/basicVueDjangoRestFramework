<template>
    <div>
      <h3>Pagina 1</h3>
      <p>essa pagina precisa de login</p>
      <b-table 
        striped 
        hover 
        :items="data"
        :fields="fields"
        :busy="esperando"
      >
      <template #cell(actions)="row">
        <b-button size="sm" @click="info(row.item, row.index, $event.target)" class="mr-1">
          Editar
        </b-button>
        <b-button size="sm" @click="alert(row.index)">
          Apagar
        </b-button>
      </template>

      </b-table>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  data(){
    return {
      esperando: false,
      falha: false,
      data:[],
      fields:['id','name','description','action'],
      items:[
        {'idade':32,'nome': 'carlos','sobrenome':'agnes'},
        {'idade':54,'nome': 'joão','sobrenome':'carlos'},
        {'idade':22,'nome': 'joaquins','sobrenome':'freitas'}
      ]
    }
  },
  created(){
    this.getDados();
  },
  computed:{
    ...mapGetters(['getDominio','getToken'])
  },
  methods:{
    async getDados(){
      try{
        this.esperando = true
        const response = await fetch(`${this.getDominio}/api/os/`,{
          headers:{
            'Authorization': `Token ${this.getToken}`
          }
        });
        if(!response.ok){
          throw new Error('Failed to fetch data');
        }
        const data = await response.json()
        this.esperando = false
        this.data = data
        this.falha = false
      }catch(error){
        this.falha = true
        this.esperando = false
        alert(error)
      }
    }
  }
}
</script>
  
 