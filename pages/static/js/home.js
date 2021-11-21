
var STATE = {
    courts: [],
    current_court: null,
}

const setMarkers = (map) => {
    let url = `/api/courts/get-all-courts`
    let method = 'GET'
    let headers = {
        "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val()
    }
    let body = {}

    $.ajax({
        url: url,
        method: method, 
        headers: headers,
        error: (jqx, status, e) => {
            console.log(status)
            console.log(e)
            console.log(jqx)
        },
        success: (data, status, jqx)=>{
            try {
                STATE.courts = []
                for (let court of data) {
                    STATE.courts.push(court)
                    let _pos = {
                        lat: court.latitude,
                        lng: court.longitude,
                    };
                    let _marker = new google.maps.Marker({
                        position: _pos,
                        map: map,
                        title: court.name,
                    });

                    google.maps.event.addListener(_marker, 'click', function (event) {
                        STATE.current_court = court
                        $('.current-court-panel').empty()
                        let dates_ocupied = ''
                        for (let date of court.dates) {
                            dates_ocupied += `<div class="date-ocupied">${date}</div>`
                        }

                        let today = new Date();
                        $('.current-court-panel').append(`
                        <div class="current-court-name">
                            ${STATE.current_court.name}
                        </div><br>
                        <input type="hidden" id="court-id" value="${court.pk}">
                        <input type="date" id="court" min="${today.getFullYear()}-${today.getMonth() + 1}-${today.getDate()}" value="${today.getFullYear()}-${today.getMonth() + 1}-${today.getDate()}"><br><br>
                        <button class="button is-primary" id="book-button">Book</button><br>
                        <h4 class="my-2">Dates ocupied for this Court</h4>
                        <div class="dates-ocupied">
                        ${dates_ocupied}
                        </div>
                        `)
                        $('#book-button').click(()=> {
                            let date = $('#court').val();
                            if (date) {
                                let url = `/api/courts/book-court/`
                                let method = 'POST'
                                let headers = {
                                    "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val()
                                }
                                let body = {
                                    date: date,
                                    court_id: $('#court-id').val()
                                }

                                $.ajax({
                                    url: url,
                                    method: method, 
                                    data: body,
                                    headers: headers,
                                    error: (jqx, status, e) => {
                                        console.log(status)
                                        console.log(e)
                                        console.log(jqx)
                                    },
                                    success: (data, status, jqx)=>{
                                        try {
                                            alert(data.message);
                                            location.reload();
                                        } catch (error) {
                                            console.log(error)
                                        }
                                    }
                                })
                            }
                        })
                    })
                }
            } catch (error) {
                console.log(error)
            }
        }
    })
}

let map 
function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 24.774265, lng: 46.738586 },
        zoom: 10,
    });

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                };
                map.setCenter(pos);
            },
            () => {
                console.log("Location not found");
            }
        );
    }

    setMarkers(map)
}