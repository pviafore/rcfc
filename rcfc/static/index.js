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
            $("#remote").append("<div class='row'><button class='btn-lg btn-info' id='" + getId(button.id) + "'>" + button.text + "</button></div>");
            $("#" + getId(button.id)).click(function () {
                $.post({url: "/buttons/" + button.id});
            });
        }
        if (button.type === "button.toggle") {
            $("#remote").append("<div class='row'>" + button.text + ": <label class='switch'><input type='checkbox' id='" + getId(button.id) + "'><span class='slider round'></span></label></button></div>");
            $("#" + getId(button.id)).click(function () {
                $.post({url: "/buttons/" + button.id, data: JSON.stringify({value: $("#" + getId(button.id)).prop('checked')}), contentType: "application/json"})
            });
            if(button.state) {
                $("#" + getId(button.id)).prop('checked', true);
            }
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