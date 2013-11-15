/* Pyoto App
 * Meng Zhuo <mengzhuo1203@gmail.com> 2013
 * */

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
$('.ui.modal').modal();
$('.delete').popup({on:'hover'});
$('.fork').popup({on:'hover'});
$(function (){

    var time = $('input[name="expirate_at"]');
    if (time.val() == ""){
        var one_hour_after = new Date((new Date).getTime()+3600000);
        var time_formated = one_hour_after.getHours() + ":" + one_hour_after.getMinutes()
        time.val(time_formated);
    }

    $('#logout').click(function(){
        $.get('/logout/', function(data){
            if (data == 0){
                console.log('logout');
                location.reload();
            }
        })
    })
    $('#login').click(function(){
        $('#login_modal').modal('show');
    });
    $('#register').click(function(){
        $('#register_modal').modal('show');
    });
    $('#login_modal #submit').click(function(){
        console.log('try to login');
        $.post('/login/', 
                $('#login_modal form').serializeArray(),
                function(data){
                    if (data == 0){
                        console.log('log in');
                        location.reload();
                    }
                }
        )
    })
    $('#register_modal #submit').click(function(){
        console.log('try to register');
        $.post('/register/', 
                $('#register_modal form').serializeArray(),
                function(data){
                    if (data == 0){
                        console.log('log in');
                        location.reload();
                    }
                }
        )
    })
    $('.thumbnail').click(function(){
        console.log(this);
        var tid = $(this).attr('data-target');
        $('#modal-order-'+tid).modal('show');
    });
    $('.add-fee .submit').click(function(){
        var order = $(this).closest('.order').attr('data-order');
        var data = $(this).closest('form').serializeArray();
        data.push({name:'order', value:order});
        $.post('/fee/create/', data, function(d){console.log(d);if (d ==0){location.reload();}})
    })
    $('.order .delete').click(function(){
        var fee_id = $(this).closest('tr').data('fee');
        $.ajax('/fee/'+fee_id, {'type':'DELETE'}).done(function(){
           location.reload(); 
        });
    })
    $('.order .fork').click(function(){
        var fee = $(this).closest('tr');
        $.post('/fee/create/', 
            { 'description': fee.data('description'),
              'price':fee.data('price'),
             'order': $(fee).closest('.order').data('order')},
             function(d){if (d==0){
               location.reload();
             }})
    })
});
