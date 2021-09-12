$(document).ready(function () {

    // jQuery datepicker
    $("#datepicker").datepicker({
    changeMonth: true,
    changeYear: true,
    dateFormat: 'dd-mm-yy',
    minDate : 0
    });

    // https://timepicker.co/# 
    $('#timepicker').timepicker({
    timeFormat: 'hh:mm p',
    minTime: '00:00am',
    maxTime: '11:59pm',
    defaultTime: 'Band Start Time',
    startTime: '10:00',
    });

})
