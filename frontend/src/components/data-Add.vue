<template>
    <div>
        <div class="card-header mb-3">
            <h4> Cadastro de OS</h4>
        </div>
        <b-form>
            <b-form-group label="Cliente:" :state="clienteOK"  invalid-feedback="Não pode ser Vazio">
            <b-input-group>
                <b-form-input :state="clienteOK" 
                    type="text" placeholder="Fabricante" v-model="obj.name" trim >
                </b-form-input>
            </b-input-group>
        </b-form-group>
        <b-form-group label="Serviço:" :state="serviceOK"  invalid-feedback="Não pode ser Vazio">
            <b-input-group>
                <b-form-input :state="serviceOK" 
                    type="text" placeholder="Serviço" v-model="obj.descpition" trim >
                </b-form-input>
            </b-input-group>
        </b-form-group>

        <b-form-group class="mt-3 pt-3 bg-danger" >
            <b-button @click="putDadosOS" v-bind:class="{disabled:!podeCadastrar}"  block variant="primary">
                <span v-show="espera">
                <b-spinner type="grow" variant="light"></b-spinner>
                <b-spinner type="grow" variant="light"></b-spinner>
                <b-spinner type="grow" variant="light"></b-spinner>
               </span>
               <span v-show="!espera">Cadastrar</span>
            </b-button>
        </b-form-group>
        </b-form>
    </div>
</template>

<script lang="js">
export default {
  name: 'data-Add',
  data(){
    return{
        modalVisible:false,
        erroMsg : '',
        espera:false,
        falha: false,
        obj:{'name':'','descpition':''}
    }
  },computed:{
    clienteOK(){
        if(this.obj.name.length>0){return true}
        else{return false}
    },
    serviceOK(){
        if(this.obj.descpition.length>0){return true}
        else{return false}
    },
    podeCadastrar(){
        if (this.clienteOK && this.serviceOK){ return true}
        else{ return false}
    }
  },methods:{
    dataFormat(){
            //const form = document.getElementById('img')
            //const file = form.files[0]
            const formdata = new FormData()
            //if(file!==undefined){formdata.append('img',file,file.name)}
            //if(this.obj.id!==undefined){formdata.append('id',this.obj.id)}
            formdata.append('name',this.obj.name)
            formdata.append('descpition',this.obj.descpition)
            return formdata
    },
    async putDadosOS(){
        this.espera=true
        try{
        this.esperando = true
          const response = await fetch(`${this.getDominio}/api/os/`,{
            method:"PUT",
            headers:{
            'Authorization': `Token ${this.getToken}`
          },body:this.dataFormat()
        })
        if(response.ok){
          this.espera = false
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
        this.espera = false
      }
       
    }

  }

}
</script>