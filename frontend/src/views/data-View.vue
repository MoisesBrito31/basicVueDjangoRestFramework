<template>
    <div>
      <!-- aqui o modal que vai mostrar erros na tela: -->
      <b-modal v-model="modalVisible" centered ok-only title="Erro" no-stacking>
        <div class="d-flex flex-column align-items-center">
          <b-alert show variant="danger" class="mt-3">
          <b-icon icon="exclamation-circle-fill"></b-icon>
            {{ erroMsg }}
          </b-alert>
        </div>
      </b-modal>

      <b-modal v-model="modalAddVisible" centered ok-only title="CAdastrar">
        <div class="d-flex flex-column align-items-center">
          <dataAdd></dataAdd>
        </div>
      </b-modal>

      <h3>Pagina 1</h3>
      <p>essa pagina precisa de login</p>
      <b-overlay rounded="sm" :show="esperando">
        <dataTable :actions="act" :items="data" :fields="fields"
          @novo="chamaAdd"
          @editar="chamaEdit"
          @apagar = "chamaDel"
        ></dataTable> 
      </b-overlay>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import dataTable from '@/components/data-Table.vue';
import dataAdd from '@/components/data-Add.vue'
export default {
  components:{
    dataTable,
    dataAdd
  },
  data(){    
    return {
      modalVisible:false,
      modalAddVisible:false,
      erroMsg:'',
      act: [1,1,1], //novo,edit,apaga
      esperando: false,
      falha: false,
      data:[], // data precisa ter a key action se não não libera ferramentas
      fields:[
        {key:'id'},
        {key:'name',label:'Cliete',sortable:true},
        {key:'description',label:'Trabalho',sortable:true},
        {key:'action',label:'ação'}
      ]
    }
  },
  created(){
    this.getDadosOS()
  },
  computed:{
    ...mapGetters(['getDominio','getToken'])
  },
  methods:{
    informe(valor){
      alert(valor)
    },
    chamaAdd(){
      this.modalAddVisible = true
    },
    chamaEdit(valor){
      alert(`chamar o data-edit de id: ${valor}`)
    },
    chamaDel(valor){
      alert(`chamar o deletar de id: ${valor}`)
    },
    async getDadosOS(){
      try{
        this.esperando = true
          const response = await fetch(`${this.getDominio}/api/os/`,{
          headers:{
            'Authorization': `Token ${this.getToken}`
          }
        })
        if(response.ok){
          const data = await response.json()
          this.esperando = false
          this.data = data
          this.falha = false
        }else{
          switch(response.status){
            case 401:
              throw new Error('Não Autorizado');
            case 404:
              throw new Error('Não Encontrado');
            default:
              throw new Error('Falha interna no Servidor');
          }
        }
      }catch(error){
        this.modalVisible = true
        this.erroMsg = error
        this.falha = true
        this.esperando = false
      }
    }
  }
}
</script>
  
 