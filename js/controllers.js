'use strict';

/* Controllers */
function SearchCtrl($scope, $http) {
  $http.get('buscar/querygoeshere').success(function(data) {
    $scope.results = data;
  });
}
