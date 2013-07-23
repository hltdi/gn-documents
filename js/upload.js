$(document).ready(function(){
	$('form').ajaxForm({
        beforeSubmit: function() {
            
        },
        success: function(response) {
            alert(response.message);
        }
	});
});