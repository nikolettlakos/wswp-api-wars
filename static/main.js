var $items = $('#datas');

$.ajax({
    dataType: "json",
    url: 'https://swapi.co/api/planets/?page=',
    success: function(datas) {
        $.each(datas.results, function(i, data){
         $items.append('<tr><td>' + data.name + '</td>' +
                          '<td>' + commaSeperatedNumbers(data.diameter) + ' km' + '</td>' +
                          '<td>' + data.climate + '</td>' +
                          '<td>' + data.terrain + '</td>' +
                          '<td>' + data.surface_water + '%' + '</td>' +
                          '<td>' + data.population + '</td>' +
                        '<td>' + buttonForResidents(data.residents) + '</td></tr>'
            );
        })
    }
});


function buttonForResidents(residents) {
    if (residents.length === 0) {
        return 'No known residents'
    }
    else {
        return "<button class='btn'>Residents</button>"
    }
}

function commaSeperatedNumbers(num) {
  return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");      //Found on stackoverflow.
}
