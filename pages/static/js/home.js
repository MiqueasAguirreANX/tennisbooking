let map;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: -34.397, lng: 150.644 },
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

                step = 0.02
                const pos1 = {
                    lat: position.coords.latitude + step,
                    lng: position.coords.longitude + step,
                };
                const pos2 = {
                    lat: position.coords.latitude + step,
                    lng: position.coords.longitude - step,
                };
                const pos3 = {
                    lat: position.coords.latitude - step,
                    lng: position.coords.longitude + step,
                };
                const pos4 = {
                    lat: position.coords.latitude - step,
                    lng: position.coords.longitude -step,
                };
                const marker1 = new google.maps.Marker({
                    position: pos1,
                    map: map,
                    title: "Marker 1",
                });

                google.maps.event.addListener(marker1, 'click', function (event) {
                    console.log(event)
                    console.log("Marker 1 Clicked")
                })
                const marker2 = new google.maps.Marker({
                    position: pos2,
                    map: map,
                    title: "Marker 2",
                });
                google.maps.event.addListener(marker2, 'click', function (event) {
                    console.log(event)
                    console.log("Marker 2 Clicked")
                })
                const marker3 = new google.maps.Marker({
                    position: pos3,
                    map: map,
                    title: "Marker 3",
                });
                google.maps.event.addListener(marker3, 'click', function (event) {
                    console.log(event)
                    console.log("Marker 3 Clicked")
                })
                const marker4 = new google.maps.Marker({
                    position: pos4,
                    map: map,
                    title: "Marker 4",
                });
                google.maps.event.addListener(marker4, 'click', function (event) {
                    console.log(event)
                    console.log("Marker 4 Clicked")
                })
            },
            () => {
                console.log("Location not found");
            }
        );
    }
}