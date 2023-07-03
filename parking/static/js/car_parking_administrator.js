$(document).ready(function() {
        $.ajax({
            url: '/parking/spots/list',
            method: 'GET',
            success: function(data) {
                reserved_spots = data['reserved_spots'];
                // Iterate over the returned data and generate table rows
                $.each(data['parking_spots'], function(index, parking_spot) {
                    var row = $('<tr>');
                    row.append($('<td>').text(parking_spot.name));
                    row.append($('<td>').text(parking_spot.latitude));
                    row.append($('<td>').text(parking_spot.longitude));
                    if (reserved_spots.includes(parseInt(parking_spot.id))) {
                        row.append($('<td>').html('<button class="btn btn-secondary" disabled>Reserved</button>'));
                    } else {
                        row.append($('<td>').html('<button class="reserve-button btn btn-primary" id="id_button_reserve_parking_spot" data-id="' + parking_spot.id + '" data-name="' + parking_spot.name + '">Reserve</button>'));
                    }

                    $('#id_table_parking_spots tbody').append(row);
                });
                $('.reserve-button').on('click', function(event) {
                    event.preventDefault();
                    var id = $(this).data('id');
                    var parking_spot_name = $(this).data('name');
                    $('#modal-form #id').val(id);
                    $('#myModal').modal('show');
                    $('#id_parking_spot_name').text(parking_spot_name);
                });

                $('#modal-form').on('submit', function(event) {
                    event.preventDefault();
                    var formData = $(this).serialize();
                    $.ajax({
                        url: '/parking/reserve/spot',
                        method: 'POST',
                        data: formData,
                        success: function(response) {
                            console.log('Success:', response);
                            $('#modal-form')[0].reset();
                            $('#myModal').modal('hide');
                            location.reload();
                        },
                        error: function(xhr, textStatus, errorThrown) {
                            console.log('Error:', errorThrown);
                        }
                    });
                });
                $('#myModal').on('hidden.bs.modal', function() {
                    $('#modal-form')[0].reset();
                    $('#cost').text('');
                    $('#valid_till').text('');
                });
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log('Error:', errorThrown);
            }
        });

        function validateLatitude(latitude) {
            console.log(latitude);
            const latitudeRegex = /^-?([0-8]?\d(?:\.\d{1,6})?|90(?:\.0{1,6})?)$/;

            if (!latitudeRegex.test(latitude)) {
            return false; // Latitude is invalid
            }
            return true; // Latitude is valid
        }
        function validateLongitude(longitude) {
            const longitudeRegex = /^-?((?:1[0-7]|[0-9])?\d(?:\.\d{1,6})?|180(?:\.0{1,6})?)$/;

            if (!longitudeRegex.test(longitude)) {
            return false; // Longitude is invalid
            }
            return true; // Longitude is valid
        }
        function validateDistance(distance) {
            if (distance < 100) {
            return false; // Distance is invalid
            }
            return true; // Distance is valid
        }

        $('#id_search_parking_spot').on('click', function(event) {
            event.preventDefault();
            $('#id_search_spot_modal').modal('show');
        });

        $('#id_search_spot_modal').on('hidden.bs.modal', function() {
            $('#id_search_spot_modal_form')[0].reset();
        });

        $('#id_search_spot_modal_form').on('submit', function(event) {
            event.preventDefault();
            var formData = $(this).serialize();
            var latitude = $('#id_search_spot_modal_form #latitude');
            var longitude = $('#id_search_spot_modal_form #longitude');
            var distance = $('#id_search_spot_modal_form #distance');
            var invalidFlag = false;
            if (!validateLatitude(latitude.val())) {
                latitude.addClass('is-invalid');
                invalidFlag = true;
            } else {
                latitude.removeClass('is-invalid');
            }
            if (!validateLongitude(longitude.val())) {
                longitude.addClass('is-invalid');
                invalidFlag = true;
            } else {
                longitude.removeClass('is-invalid');
            }
            if (!validateDistance(distance.val())) {
                distance.addClass('is-invalid');
                invalidFlag = true;
            } else {
                distance.removeClass('is-invalid');
            }
            if (invalidFlag) {
                return;
            }
            $.ajax({
                url: '/parking/spots/list',
                method: 'POST',
                data: formData,
                success: function(data) {
                    console.log('Success:', data);
                    $('#id_table_parking_spots tbody').empty();
                    reserved_spots = data['reserved_spots'];
                    $.each(data['parking_spots'], function(index, parking_spot) {
                        var row = $('<tr>');
                        row.append($('<td>').text(parking_spot.name));
                        row.append($('<td>').text(parking_spot.latitude));
                        row.append($('<td>').text(parking_spot.longitude));
                        if (reserved_spots.includes(parseInt(parking_spot.id))) {
                            row.append($('<td>').html('<button class="btn btn-secondary" disabled>Reserved</button>'));
                        } else {
                            row.append($('<td>').html('<button class="reserve-button btn btn-primary" id="id_button_reserve_parking_spot" data-id="' + parking_spot.id + '" data-name="' + parking_spot.name + '">Reserve</button>'));
                        }

                        $('#id_table_parking_spots tbody').append(row);
                    });
                    if (data['parking_spots'].length == 0) {
                        $("#id_search_spot_info").text("No Nearby Parking Spots Found.");
                    } else {
                        $("#id_search_spot_info").text("Showing Search Results for Latitude: " + latitude.val() + ", Longitude: " + longitude.val() + ", Distance: " + distance.val() + "m");
                    }
                    $('#id_search_spot_modal_form')[0].reset();
                    $('#id_search_spot_modal').modal('hide');
                },
                error: function(xhr, textStatus, errorThrown) {
                    console.log('Error:', errorThrown);
                }
            });
        });
    });