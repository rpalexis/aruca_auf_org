(function() {

    $(document).ready(function() {

        $('#publications fieldset').formset({
            prefix: 'publication',
            addText: 'ajouter une publication',
            deleteText: 'supprimer cette publication',
            formCssClass: 'dynamic-form-publications'
        });

        // Publications legacy
        var $edit_publication_link = $('<a class="edit-publication">éditer cette publication</a>');
        var $additional_fields = $('.publication_affichage').next();
        $additional_fields.after($edit_publication_link).hide();
        $edit_publication_link.click(function() { $additional_fields.show(); $(this).hide(); });
		
		/*A+*/
		$('#agrandir').click(function(){
			var currentFontSize = $('#page2 p').css('font-size');
			var currentFontSizeNum = parseFloat(currentFontSize, 10);
			var newFontSize = currentFontSizeNum*1.1;
			$("#page2 p").css('font-size', newFontSize);
		});
		
		/*A-*/
		$('#diminuer').click(function(){
			var currentFontSize = $('#page2 p').css('font-size');
			var currentFontSizeNum = parseFloat(currentFontSize, 10);
			var newFontSize = currentFontSizeNum*0.9;
			$("#page2 p").css('font-size', newFontSize);
		});

    });

})();
