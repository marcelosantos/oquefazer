angular
.module('oquefazer.app', ['ngRoute'])

.service('LoadingInterceptor', ['$q', '$rootScope', '$log', function($q, $rootScope, $log) {

    'use strict';

    return {
        request: function(config) {
            $rootScope.loading = true;
            return config;
        },
        requestError: function(rejection) {
            $rootScope.loading = false;
            $log.error('Request error:', rejection);
            return $q.reject(rejection);
        },
        response: function(response) {
            $rootScope.loading = false;
            return response;
        },
        responseError: function(rejection) {
            $rootScope.loading = false;
            $log.error('Response error:', rejection);
            return $q.reject(rejection);
        }
    };
}])

.config(['$routeProvider',
function config($routeProvider) {

    $routeProvider
    .when('/', {
        templateUrl: '/static/html/lista.html',
        controller: 'ListaController',
        controllerAs: 'vm'
    })
    .otherwise('/');
}
])
.config(['$httpProvider', function ($httpProvider) {
    $httpProvider.interceptors.push('LoadingInterceptor');    
    // Intercept POST requests, convert to standard form encoding
    $httpProvider.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
    $httpProvider.defaults.transformRequest.unshift(function (data, headersGetter) {
        var key, result = [];

        if (typeof data === "string")
        return data;

        for (key in data) {
            if (data.hasOwnProperty(key))
            result.push(encodeURIComponent(key) + "=" + encodeURIComponent(data[key]));
        }
        return result.join("&");
    });
}]).run(run);

run.$inject = ['$http'];

/**
* @name run
* @desc Update xsrf $http headers to align with Django's defaults
*/
function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
};
