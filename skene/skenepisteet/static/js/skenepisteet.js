modalOptions = {
    maxWidth: "500px",
    initialWidth: "300",
    initialHeight: "300",
    onComplete: initModalForms,
    onOpen: hideMessages,
    close: false
}

pjaxOptions = {
    container: '#content'
}

function hideMessages() {
    $('.messages').slideUp();
}

function initModalForms() {
    /* Make forms in popups to load in new popup - and reload main page with pjax if response is
    JSON with redirect element */
    $(".modal-form").submit(function () {
        $.post(
            $(this).attr('action'),
            $(this).serialize(),
            function (data) {
                if (data.redirect) {
                    $.pjax($.extend({url: data.redirect}, pjaxOptions));
                    $.colorbox.close();
                } else {
                    $.colorbox($.extend({html: data}, modalOptions));
                }
            }
        );

        return false; // prevent normal form submit
    });

}