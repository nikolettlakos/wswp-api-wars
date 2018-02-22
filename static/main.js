let $items = $('#datas');
let $residentData = $('#residentData');


$.ajax({
    dataType: "json",
    url: 'https://swapi.co/api/planets/?page=',
    success: function(datas) {
        $.each(datas.results, function(i, data){
         $items.append('<tr><td>' + data.name + '</td>' +
                          '<td>' + commaSeparatedNumbers(data.diameter) + ' km' + '</td>' +
                          '<td>' + data.climate + '</td>' +
                          '<td>' + data.terrain + '</td>' +
                          '<td>' + surfaceKnownOrNot(data.surface_water) + '</td>' +
                          '<td>' + commaSeparatedNumbers(data.population) + ' people' + '</td>' +
                        '<td>' + buttonForResidents(data.residents) + '</td></tr>'
            );
        })
    }
});


$.ajax({
    dataType: "json",
    url: 'https://swapi.co/api/people/?page=',
    success: function(datas) {
        $.each(datas.results, function(i, data){
         $residentData.append(data.name + '<br>' +
             data.height + '<br>' +
             data.mass + '<br>' +
             data.skin_color + '<br>' +
             data.hair_color + '<br>' +
             data.eye_color + '<br>' +
             data.birth_year + '<br>' +
             data.gender + '<br>'
            );
        })
    }
});


function buttonForResidents(residents) {
    if (residents.length === 0) {
        return 'No known residents'
    }
    else {
        return "<button class='btn' data-toggle='modal' data-target='#myModal' data-residents=' + residents + ' >" + residents.length + " resident(s)</button>"
    }
}


function commaSeparatedNumbers(num) {
  return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");  //Found on stackoverflow.
}


function surfaceKnownOrNot(surface_water) {
    if (surface_water === 'unknown') {
        return 'Unknown'
    }
    else {
        return surface_water + '%'
    }
}