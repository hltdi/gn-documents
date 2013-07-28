'use strict';

function MenuCtrl($scope) {
	$scope.menuList = [
	   {id:0, url:'#/search', text:"Inicio", style:"active"},
	   {id:1, url:'#/upload', text:"Subir Documentos", style:""},
	   {id:2, url:'#/catalog', text:"Catalogo", style:""},
	   ];
	$scope.changeActive = function(id) {
		var i;
		for(i=0; i < $scope.menuList.length; i++) {
			$scope.menuList[i].style="";
		}
		$scope.menuList[id].style="active";
	}
}

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

function CatalogCtrl($scope, $http) {
	
}