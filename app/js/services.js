'use strict';

/* Services */

angular.module('totalFilesServices', ['ngResource']).
factory('TotalFiles', function($resource){
	return $resource('/uploaded/totalfiles', {}, {
		query: {method:'GET', isArray:false}
	});
});
