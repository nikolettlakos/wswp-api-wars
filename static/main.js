var $datas = $('#datas');

$.ajax({
    dataType: 'json',
    type: 'GET',
    url: 'https://swapi.co/api/planets/?page=',
    success: function(response) {
        console.log(response['terrain'])
    }
});