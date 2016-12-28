(function(){

    angular.module('oquefazer.app')
        .controller('ListaController', ['$scope', '$http', '$location', ListaController]);

    function ListaController ($scope, $http, $location) {

        var self = this;

        self.lista = [];

        self.adicionar = function (atividade) {

            var atividade = {
                "titulo": atividade.titulo,
                "descricao": atividade.descricao
            };

            $http.post('/adicionar/', atividade)
                .then(function (response) {
                        self.lista.push(response.data);
                    },
                    function () {
                        alert('Erro ao criar atividade');
                    }
                );

        };

    }

})();
