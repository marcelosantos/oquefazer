(function(){

    angular.module('oquefazer.app')
        .controller('ListaController', ['$scope', '$http', '$location', ListaController]);

    function ListaController ($scope, $http, $location) {

        var self = this;

        self.form_cadastro = true;
        self.form_edicao = false;

        self.listagem = [];
        self.listagem_pendentes = [];
        self.listagem_finalizados = [];
        self.atividade = {};
        self.atividade.status = false;

        self.adicionar = adicionar;
        self.listar = listar;
        self.visualizar = visualizar;
        self.editar = editar;
        self.limpar = limpar;

        listar();

        //Atualiza listagem
        function atualizarListagem(atividades){

            self.listagem_pendentes = [];
            self.listagem_finalizados = [];

            for (var i = 0; i < atividades.length; i++){
                console.log(atividades[i]);
                if(atividades[i].status == 'false'){
                    self.listagem_pendentes.push(atividades[i]);
                }else{
                    self.listagem_finalizados.push(atividades[i]);
                }

            }

        }

        //Função para adicionar atividade
        function adicionar(atividade) {

            self.atividade = {
                "titulo": atividade.titulo,
                "descricao": atividade.descricao,
                "status": atividade.status
            };

            $http.post('/adicionar/', atividade)
                .then(sucessoAdicao,erroAdicao);

        };

        function sucessoAdicao (response) {
            self.listagem = response.data;
            atualizarListagem(self.listagem);
            Materialize.toast('Atividade cadastrada com sucesso!', 4000);
            self.atividade = {};
            self.atividade.status = false;
        }

        function erroAdicao() {
            var ERRO = "Erro ao criar atividade";
            Materialize.toast(ERRO, 6000);
        }

        //Função para listar atividades
        function listar() {

            $http.get('/listar/')
                .then(sucessoListagem,erroListagem);

        };

        function sucessoListagem (response) {
            self.listagem = response.data;
            atualizarListagem(self.listagem);
        }

        function erroListagem() {
            var ERRO = "Erro ao listar atividades";
            Materialize.toast(ERRO, 6000);
        }

        //Função para visualizar atividade
        function visualizar(atividade){

            self.form_cadastro = false;
            self.form_edicao = true;

            $(".formulario-de-edicao #titulo").focus();

            self.atividadeEdicao = atividade;

        }

        //Função para editar atividade
        function editar() {

            $http.post('/editar/', self.atividadeEdicao)
                .then(sucessoEdicao,erroEdicao);

        };

        function sucessoEdicao(response) {

            self.listagem = response.data;
            atualizarListagem(self.listagem);
            self.form_cadastro = true;
            self.form_edicao = false;
            self.atividadeEdicao = {};
            Materialize.toast('Atividade atualizada com sucesso!', 4000);

        }

        function erroEdicao() {
            var ERRO = "Erro ao editar atividade";
            Materialize.toast(ERRO, 6000);
        }

        //Função para remover todas as atividades cadastradas
        function limpar() {

            $http.post('/limpar/')
                .then(sucessoLimpeza,erroLimpeza);

        };

        function sucessoLimpeza(response) {

            self.listagem = response.data;
            atualizarListagem(self.listagem);
            Materialize.toast('Atividades removidas com sucesso!', 4000);

        }

        function erroLimpeza() {
            var ERRO = "Erro ao remover atividades";
            Materialize.toast(ERRO, 6000);
        }


    }

})();
