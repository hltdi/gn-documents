'use strict';

/* App Module */

angular.module('gndocuments', ['totalFilesServices']).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.
    when('/search', {templateUrl: 'partials/search.html',   controller: SearchCtrl}).
    when('/upload', {templateUrl: 'partials/upload.html', controller: UploadCtrl}).
    when('/catalog', {templateUrl: 'partials/catalog.html', controller: CatalogCtrl}).
    otherwise({redirectTo: '/search'});
}]);
