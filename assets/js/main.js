;(function(){

			// Menu settings
			$('#menuToggle, .menu-close').on('click', function(){
				$('#menuToggle').toggleClass('active');
				$('body').toggleClass('body-push-toleft');
				$('#theMenu').toggleClass('menu-open');
			});

			$('.menu-wrap').click( function() {
				$('#menuToggle').toggleClass('active');
				$('body').toggleClass('body-push-toleft');
				$('#theMenu').toggleClass('menu-open');
    	});

			$(".item").click(function(event) {
				var clicked = $(this).attr("id");
        var $modal = $("#" + clicked + "-modal.modal");
        var containerId = $(this).parent().parent().attr('id');
        if ($modal.length !== 0) {
		  		$("#" + clicked + "-modal.modal").modal("toggle");
        }
			});

})(jQuery)
