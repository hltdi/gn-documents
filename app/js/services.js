'use strict';

/* Services */

angular.module('totalFilesServices', ['ngResource']).
factory('TotalFiles', function($resource){
	return $resource('/uploaded/totalfiles', {}, {
		query: {method:'GET', isArray:false}
	});
});

angular.module('allTagsServices', ['ngResource']).
factory('AllTags',
    function($resource){
      var foo = $resource('/uploaded/alltags',
                       {},
                       {query: {method:'GET', isArray:false}});
      console.log(foo);
      return foo;
    });
