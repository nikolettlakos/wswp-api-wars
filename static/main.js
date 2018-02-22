let $items = $('#datas');
let $residentData = $('#residentData');
let planetResidents = [];


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
                        '<td>' + buttonForResidents(data.residents) + '</td></tr>');
         planetResidents.push(data.residents);
        })
    }
});


console.log(planetResidents);
$.ajax({
    dataType: "json",
    url: 'https://swapi.co/api/people/?page=',
    success: function(datas) {
        $.each(datas.results, function(i, data){
         $residentData.append('<tr><td>' + data.name + '</td>' +
                          '<td>' + data.height + '</td>' +
                          '<td>' + data.mass + '</td>' +
                          '<td>' + data.skin_color + '</td>' +
                          '<td>' + data.hair_color + '</td>' +
                          '<td>' + data.eye_color + '</td>' +
                            '<td>' + data.birth_year + '</td>' +
                        '<td>' + data.gender + '</td></tr>'
            );
        })
    }
});


function buttonForResidents(residents) {
    if (residents.length === 0) {
        return 'No known residents'
    }
    else {
        return "<button class='btn' data-toggle='modal' data-target='#myModal'>" + residents.length + " resident(s)</button>"
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