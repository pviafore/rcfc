/*jslint browser: true*/
/*jshint esversion: 6 */
/*global  $, jQuery, console*/
/*global console*/

(function () {
    "use strict";
    "esversion: 6";
;
    function getId(id) {
        return "button" + id;
    }

    function displayButton(button) {
        if (button.type === "button.simple") {
            $("#remote").append("<button class='btn-xl btn-info' id='" + getId(button.id) + "'>" + button.text + "</button>");
            $("#" + getId(button.id)).click(function () {
                $.post({url: "/buttons/" + button.id});
            });
        }
    }

    function displayButtons(data) {
        data.buttons.forEach(displayButton);
    }

    function loadButtons() {
        $.ajax({
            url: "/buttons",
            success: displayButtons,
            dataType: "json"
        });
    }

    $(document).ready(loadButtons);
}());