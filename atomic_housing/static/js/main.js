var openModal = function(elem, onOpen) {
	$(elem).addClass('active');
	$('body').addClass('modal-open');

  $(elem).on('click', function () {
      event.stopPropagation();
  });
  $('.modal-container').on('click', function () {
      closeModal();
  });
  $(document).keyup(function (e) {
      if (e.keyCode == 27) {
          closeModal();
      }
  });
  if (onOpen) {
    onOpen();
  }
}

var closeModal = function () {
    $('.modal.active').removeClass('active');
    $('body').removeClass('modal-open');
}

$("[data-modal]").on('click', function () {
    var target = $(this).data('modal');
    var onOpen = $(this).data('onopen');
    openModal(target, function () {initialize(onOpen);});
});


var map;
var geocoder;

function initialize(elem) {
	var mapContainer = $(elem);
	var address = mapContainer.data('address');
	var icon = '../img/map-marker.png';

	map = new google.maps.Map(mapContainer[0], {
		zoom: 16,
		scrollwheel: false,
		center: codeAddress(address),
		styles: [{"featureType":"water","elementType":"geometry","stylers":[{"color":"#396ccf"}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#47a5da"}]},{"featureType":"poi","stylers":[{"visibility": "off"}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"color":"#ffd480"}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"visibility":"off"}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#47a5da"}]},{"elementType":"labels.text.fill","stylers":[{"color":"#000000"}]},{"elementType":"labels.text.stroke","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"geometry","stylers":[{"visibility":"off"}]},{"featureType":"administrative","elementType":"geometry","stylers":[{"visibility":"on"},{"color":"#333739"},{"weight":0.8}]},{"featureType":"poi.park","stylers":[{"color":"#47a5da"}]},{"featureType":"road","elementType":"geometry.stroke","stylers":[{"color":"#47a5da"},{"weight":1},{"lightness":-25}]}]
	});

	var marker = new google.maps.Marker({
    position: map.getCenter(),
    icon: icon,
    map: map
  });
}
function codeAddress(address) {
  geocoder = new google.maps.Geocoder();
  geocoder.geocode( { 'address': address}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      map.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location
      });
    } else {
      alert("Geocode was not successful for the following reason: " + status);
    }
  });
}

$(document).ready(function () {
  $("[data-map]").each(function () {
    if ($(this).data('map') == '') {
      initialize(this);
    }
  });
});
