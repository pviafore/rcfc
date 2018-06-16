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

    function displayGroup(group) {
      if(group == null) {
        name = "unassigned"
      } else {
        name = group
      }
      let id = name.replace(/ /g, '_');
      $("#group-content").append("<button id='" + id + "'>" + name + "</button>");
      $("#" + id).click(function () {
        clearButtons();
        console.log(group);
        loadButtons(group);
      });
    }

    function clearButtons() {
      $("#remote").empty();
    }

    function displayGroups(data) {
      data.groups.forEach(displayGroup);
    }

    function displayButtons(data) {
        data.buttons.forEach(displayButton);
    }

    function displayButtonsInGroup(data, group) {
      data.buttons = data.buttons.filter(button => {
        return button.group == group
      });
      displayButtons(data);
    }

    function loadButtons(group) {
        $.ajax({
            url: "/buttons",
            success: function(data) {
              console.log(data)
              displayButtonsInGroup(data, group)
            },
            dataType: "json"
        });
    }

    function loadGroups() {
      $.ajax({
        url: "/groups",
        success: displayGroups,
        dataType: "json"
      });
    }

    $(document).ready(loadGroups);
}());
