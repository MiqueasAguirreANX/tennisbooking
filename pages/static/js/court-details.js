let map

function initMap() {
    let lat = parseFloat($('#latitude').val())
    let lng = parseFloat($('#longitude').val())
    let name = $('#court-name').val()
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: lat, lng: lng},
        zoom: 15,
    });

    let _pos = {
        lat: lat,
        lng: lng,
    };
    let _marker = new google.maps.Marker({
        position: _pos,
        map: map,
        title: name,
    });
}