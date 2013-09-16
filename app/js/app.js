'use strict';

/* App Module */

angular.module('gndocuments', ['totalFilesServices', 'allTagsServices']).
config(['$locationProvider','$routeProvider',
    function($locationProvider, $routeProvider) {
      $routeProvider.
        when('/search', {templateUrl: 'partials/search.html',   controller: SearchCtrl}).
        when('/searchresults/:query', {templateUrl: 'partials/searchresults.html',   controller: SearchCtrl}).
        when('/bytag/:query', {templateUrl: 'partials/bytag.html',   controller: ByTagCtrl}).
        when('/upload', {templateUrl: 'partials/upload.html', controller: UploadCtrl}).
        when('/catalog', {templateUrl: 'partials/catalog.html', controller: CatalogCtrl}).
        otherwise({redirectTo: '/search'});

      // XXX: when do we need this? ...
      // $locationProvider.html5Mode(true);
}]);
