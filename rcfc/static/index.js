/*jslint browser: true*/
/*jshint esversion: 6 */
/*global  $, jQuery, console*/
/*global console*/

(function () {
    "use strict";
    "esversion: 6";

    function loadPage() {

    }

    function getId(id) {
        return "button" + id;
    }

    function displayButton(button) {
        if (button.type === "button.simple") {
            displaySimpleButton(button);
        }
        if (button.type === "button.toggle") {
            displayToggleButton(button);
        }
        if (button.type === "input.slider") {
            displayInputSlider(button);
        }
        if (button.type === "input.leftright") {
            displayLeftRightArrows(button);
        }
        if (button.type === "input.colorpicker") {
            displayColorPicker(button);
        }
    }

    function displaySimpleButton(button) {
        $("#groupContainer").append("<div class='row'><button class='btn-lg btn-info' id='" + getId(button.id) + "'>" + button.text + "</button></div>");
        $("#" + getId(button.id)).click(function () {
            $.post({ url: "/buttons/" + button.id });
        });
    }

    function displayToggleButton(button) {
        $("#groupContainer").append("<div class='row'>" + button.text + ": <label class='switch'><input type='checkbox' id='" + getId(button.id) + "'><span class='slider round'></span></label></button></div>");
        $("#" + getId(button.id)).click(function () {
            $.post({ url: "/buttons/" + button.id, data: JSON.stringify({ value: $("#" + getId(button.id)).prop('checked') }), contentType: "application/json" });
        });
        if (button.state) {
            $("#" + getId(button.id)).prop('checked', true);
        }

    }

    function displayLeftRightArrows(arrows) {
        $("#groupContainer").append("<div class='row'>" + arrows.text + "<br /><span id=\"" + 
                                       getId(arrows.id) + "_left\"class=\"glyphicon glyphicon-arrow-left\" /><span id=\"" + 
                                       getId(arrows.id) + "_right\"class=\"glyphicon glyphicon-arrow-right\" /></div>");
        $("#" + getId(arrows.id + "_left")).click(function () {
            $.post({ url: "/buttons/" + arrows.id, data: JSON.stringify({ value: "left"}), contentType: "application/json" });
        });
        $("#" + getId(arrows.id + "_right")).click(function () {
            $.post({ url: "/buttons/" + arrows.id, data: JSON.stringify({ value: "right"}), contentType: "application/json" });
        });
    }

    function displayInputSlider(slider) {
        $("#groupContainer").append("<div class='row'><div class='slidercontainer' >" + 
                                    slider.text + 
                                    "<input id='" + getId(slider.id) + "' type=\"range\" min=\"" + slider.min + "\" max=\"" + slider.max +"\" class=\"input-slider\" value=\"" + slider.state + "\"/></div></div>");
        $("#" + getId(slider.id)).click(function () {
            $.post({ url: "/buttons/" + slider.id, data: JSON.stringify({value: this.value }), contentType: "application/json" });
        });
    }

    function displayColorPicker(colorpicker) {
        $("#groupContainer").append("<div class='row'>" + 
                                    colorpicker.text + 
                                    "<br />Red: <input id='" + getId(colorpicker.id) + "_red' type=\"text\" value=\"" + colorpicker.state[0] + "\"/>" + 
                                    "<br />Blue: <input id='" + getId(colorpicker.id) + "_blue' type=\"text\" value=\"" + colorpicker.state[1] + "\"/>" + 
                                    "<br />Green: <input id='" + getId(colorpicker.id) + "_green' type=\"text\" value=\"" + colorpicker.state[2] + "\"/>" + 
                                    "<br /><input id='" + getId(colorpicker.id) + "' type=\"submit\" value=\"Submit\" >" + 
                                    "</div>");
        $("#" + getId(colorpicker.id)).click(function () {
            const red = $("#" + getId(colorpicker.id) +"_red")[0].value;
            const blue = $("#" + getId(colorpicker.id) +"_blue")[0].value;
            const green = $("#" + getId(colorpicker.id) +"_green")[0].value;
            $.post({ url: "/buttons/" + colorpicker.id, data: JSON.stringify({value: [red, green, blue] }), contentType: "application/json" });
        });
    }

    function displayGroup(group) {
        $("#group-tabs").append('<button class=\"w3-bar-item w3-button\" name="'+ group +'")\">' + group + '</button>');
    }

    function displayGroupTabs(data, groups) {
        if(groups.length !== 0) {
            groups = ["All", ...groups, "Unassigned"];
        }
        groups.forEach(displayGroup);
        $("#group-tabs button").click((event) => displayButtons(data, event.target.name));
        $("#groups").append('<div id="groupContainer" class="container col-xs-offset-3 col-xs-6 text-center group"></div>');
    }


    function displayButtons(data, group) {
        $("#groupContainer").empty();
        data.buttons
            .filter(b => isCorrectGroup(b, group))
            .forEach(b => displayButton(b) );
            
    }

    function isCorrectGroup(button, group) {
        return button.groups.indexOf(group) !== -1 ||
               group === "All" ||
               group === "Unassigned" && button.groups.length === 0;   
    }

    function loadButtons() {
        $.ajax({
            url: "/buttons",
            success: function (data) {
                displayGroupTabs(data, getGroups(data));
                displayButtons(data, "All");
            },
            dataType: "json"
        });
    }

    function getGroups(data) {
        return [].concat
                 .apply([], data.buttons.map((button) => button.groups))
                 .filter((value, index, self) => self.indexOf(value) === index);
    }


    $(document).ready(loadButtons);
}());
