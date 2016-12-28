(function(){

    angular.module('oquefazer.app')
        .controller('ListaController', ['$scope', '$http', '$location', ListaController]);

    function ListaController ($scope, $http, $location) {

        var self = this;

        self.form_cadastro = true;
        self.form_edicao = false;

        self.listagem = [];
        self.atividade = {};
        self.atividade.status = false;

        self.adicionar = adicionar;
        self.listar = listar;
        self.visualizar = visualizar;
        self.editar = editar;

        listar();

        //Função para adicionar atividade
        function adicionar(atividade) {

            self.atividade = {
                "titulo": atividade.titulo,
                "descricao": atividade.descricao,
                "status": atividade.status
            };

            $http.post('/adicionar/', atividade)
                .then(function (response) {
                        self.listagem = response.data;
                    },
                    function () {
                        var ERRO = "<p>Erro ao criar atividade</p>";
                        $(".formulario-de-cadastro").prepend(ERRO);
                        console.log(ERRO);
                    }
                );

        };

        //Função para listar atividades
        function listar() {

            $http.get('/listar/')
                .then(function (response) {
                        console.log(response);
                        self.listagem = response.data;
                    },
                    function () {
                        var ERRO = "<p>Erro ao listar atividades</p>";
                        $(".nao-existem-atividades .white-text").append(ERRO);
                        console.log(ERRO);
                    }
                );

        };

        //Função para visualizar atividade
        function visualizar(atividade){

            self.form_cadastro = false;
            self.form_edicao = true;

            self.atividadeEdicao = atividade;

        }

        //Função para editar atividade
        function editar(atividade) {

            self.atividade = {
                "id_atividade": atividade.id_atividade,
                "titulo": atividade.titulo,
                "descricao": atividade.descricao,
                "status": atividade.status
            };

            $http.post('/editar/', atividade)
                .then(function (response) {
                        self.listagem = response.data;
                    },
                    function () {
                        var ERRO = "<p>Erro ao editar atividade</p>";
                        $(".formulario-de-cadastro").prepend(ERRO);
                        console.log(ERRO);
                    }
                );

        };


    }

})();
