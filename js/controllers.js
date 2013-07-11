'use strict';

/* Controllers */
function SearchCtrl($scope, $http) {

  $scope.fetch = function() {
    $scope.code = null;
    $scope.response = null;
    // XXX: should maybe be post?
    // , cache: $templateCache}).
    $http({method: "get", url: "buscar/" + $scope.query}).
      success(function(data, status) {
        $scope.results = data;
      }).
      error(function(data, status) {
        alert("search failya");
    });
  };
}
