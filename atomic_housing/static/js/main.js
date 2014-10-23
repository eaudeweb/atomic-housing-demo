// $(document).ready(function () {
// 	$("[data-popout='click']").on('click', function (e) {
// 		e.preventDefault();
// 		var target = $(this).data('target');
// 		$(this).closest('.popout-container').children(target).addClass('active');
// 		$(this).on('click', function (e) {
// 			event.stopPropagation();		
// 		});
// 	});
// });

// $('html').on('click', function(e) {
// 	$('.popout').removeClass('active');
// });

var openModal = function (elem) {
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
}

var closeModal = function () {
    $('.modal.active').removeClass('active');
    $('body').removeClass('modal-open');
}

$("[data-modal]").on('click', function () {
    var target = $(this).data('modal');
    var listing = $(this).data('listing');
    var url = '/landlord/listings/' + listing + '/photos';

    $.ajax(
        {
            url: url,
            success: function (html) {
                $('#modalcontainer').html(html);
                openModal(target);
            }
        }
    )
});
