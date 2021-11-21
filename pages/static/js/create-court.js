var STATE = {
    current_lat: 0,
    current_lng: 0,
    name: "",
}
let map

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 24.774265, lng: 46.738586 },
        zoom: 12,
    });

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                };
                map.setCenter(pos);
                google.maps.event.addDomListener(map, "contextmenu", function(event) {
                    $('.add-court-modal-background').css("display", "flex");
                    STATE.current_lat = event.latLng.lat()
                    STATE.current_lng = event.latLng.lng()
                    // $('.add-court-panel-content').append(`<div>lat: ${event.latLng.lat()}<br>lng: ${event.latLng.lng()}</div>`)
                });
            },
            () => {
                console.log("Location not found");
            }
        );
    }
}

$(document).ready( () => {
    $('#court-name').change(() => {
        if ($('#court-name').val() !== "" && $('#court-name').val().length >= 4) {
            $('.yes-button').get(0).disabled = false;
        } else {
            $('.yes-button').get(0).disabled = true;
        }
    })
    $('.yes-button').click(() => {
        STATE.name = $('#court-name').val();
        console.log(STATE)

        let url = `/api/courts/create-court/`
        let method = 'POST'
        let headers = {
            "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val()
        }
    
        $.ajax({
            url: url,
            method: method, 
            data: STATE,
            headers: headers,
            error: (jqx, status, e) => {
                console.log(status)
                console.log(e)
                console.log(jqx)
            },
            success: (data, status, jqx)=>{
                console.log(data)
                alert(data.message);
                location.reload();
            }
        });
    })

    $('.no-button').click(() => {
        $('.add-court-modal-background').css("display", "none");
        $('#court-name').val("")
    })
})