$(document).ready(function() {
    function date_formatter(date) {
        date = new Date(date);
        var options = {
            day: '2-digit',
            month: 'long',
            year: 'numeric',
            hour: 'numeric',
            minute: '2-digit',
            hour12: true,
            timeZone: 'Asia/Kolkata'
        };
        var formatter = new Intl.DateTimeFormat('en-IN', options);
        var formattedDate = formatter.format(date);
        return formattedDate;
    }
    user_id = $("#global_user").text();
    $.ajax({
        url: '/parking/reserved/spots/list/' + user_id,
        method: 'GET',
        success: function(data) {
            // Iterate over the returned data and generate table rows
            $.each(data['all_reserved_spots'], function(index, reservation) {
                var row = $('<tr>');
                row.append($('<td>').text(reservation.parking_spot.name));
                row.append($('<td>').text(reservation.status));
                row.append($('<td>').text(reservation.hours * 40));
                if (reservation.status == 'Active') {
                    row.append($('<td>').text(date_formatter(reservation.reservation_end_time)));
                } else {
                    row.append($('<td>').text("N/A"));
                }

                $('#id_existing_parking_spots tbody').append(row);
            });
        },
        error: function(xhr, textStatus, errorThrown) {
            console.log('Error:', errorThrown);
        }
    });
});