function run() {
				var image = document.getElementById('background');
				image.onload = function() {
					var engine = new RainyDay({
						image: this
					});
					engine.rain([ [0, 2, 200], [3, 3, 1] ], 100);
				};
				image.crossOrigin = 'anonymous';
            	image.src = 'images/IMG_2717.jpg';
}
onload = run();

$(function() {
    $( "#from" ).datepicker({
      minDate: 1,
      defaultDate: "0d",
      changeMonth: false,
      numberOfMonths: 1,
      dateFormat: "yy-mm-dd",
      onClose: function( selectedDate ) {
        $( "#to" ).datepicker( "option", "minDate", selectedDate );
      }
    });

    $( "#to" ).datepicker({
      defaultDate: "+1w",
      changeMonth: false,
      numberOfMonths: 1,
      dateFormat: "yy-mm-dd",
      onClose: function( selectedDate ) {
        $( "#from" ).datepicker( "option", "maxDate", selectedDate );
      }
    });
});

$(function() {
    $( "#from2" ).datepicker({
      minDate: 1,
      defaultDate: "0d",
      changeMonth: false,
      numberOfMonths: 1,
      dateFormat: "yy-mm-dd",
      onClose: function( selectedDate ) {
        $( "#to2" ).datepicker( "option", "minDate", selectedDate );
      }
    });

    $( "#to2" ).datepicker({
      defaultDate: "+1w",
      changeMonth: false,
      numberOfMonths: 1,
      dateFormat: "yy-mm-dd",
      onClose: function( selectedDate ) {
        $( "#from2" ).datepicker( "option", "maxDate", selectedDate );
      }
    });
});