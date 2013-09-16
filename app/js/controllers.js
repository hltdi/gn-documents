'use strict';

/* Controllers */

function MenuCtrl($scope, $location) {
	$scope.menuList = [
	   {id:0, url:'#/search', text:"Inicio", style:""},
	   {id:1, url:'#/upload', text:"Subir un Documento", style:""},
	   {id:2, url:'#/catalog', text:"Catalogo", style:""},
	   ];
	
	var i;
	for(i = 0; i < $scope.menuList.length; i++) {
		if($location.path() === $scope.menuList[i].url.substring(1)) {
			$scope.menuList[i].style = "active";
			break;
		}
	}
	
	$scope.changeActive = function(id) {
		var i;
		for(i = 0; i < $scope.menuList.length; i++) {
			$scope.menuList[i].style = "";
		}
		$scope.menuList[id].style = "active";
	}
}

function SearchCtrl($scope, $http, $location, $routeParams, TotalFiles) {
  $scope.$routeParams = $routeParams;

  $scope.query = $routeParams.query;

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

  $scope.jumpToResults = function() {
    $location.path('/searchresults/' + $scope.query);
  };
  
  $scope.totalDocs = TotalFiles.get();
}

function ByTagCtrl($scope, $http, $location, $routeParams, TotalFiles) {
  $scope.$routeParams = $routeParams;

  $scope.query = $routeParams.query;

  $scope.fetch = function() {
    $scope.code = null;
    $scope.response = null;
    // XXX: should maybe be post?
    // , cache: $templateCache}).
    $http({method: "get", url: "etiqueta/" + $scope.query}).
      success(function(data, status) {
        $scope.results = data;
      }).
      error(function(data, status) {
        alert("search failya");
    });
  };

  $scope.jumpToResults = function() {
    $location.path('/bytag/' + $scope.query);
  };
  
  $scope.totalDocs = TotalFiles.get();
}


function UploadCtrl($scope, $http) {
	$scope.uploadFiles = function() {
		var form = $('form');
		form.attr('action', 'upload');
		form.ajaxSubmit({
			type: 'POST',
	        beforeSubmit: function() {
	            
	        },
	        success: function(response) {
	            alert(response.message);
	        }
		});
	}
}

function CatalogCtrl($scope, $http, AllTags) {
  $scope.allTags = AllTags.get();
}

