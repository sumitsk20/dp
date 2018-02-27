$('form.ajax-form').on('submit', function() {
	$(this).preventDefault();
	var form = $(this),
	url= form.attr('action'),
	type = form.attr('method'),
	data={};
  $(this).find('[name]').each(function(index,value){
  	var field = $(this),
  	name=field.attr('name'),
  	value=field.val(),
  	data[name]=value;
  });
  $.ajax({
    type: type,
    url: url,
    dataType: 'json',
    data:data,
    contentType: 'application/x-www-form-urlencoded; charset=utf-8',  //Default 
    success: function(response) {
      alert(response.message);
    },
    error : function(xhr,errmsg,err) {
           console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        },
  });
});

$(document).ready(function() {
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    }); 


});