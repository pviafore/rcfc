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

    function displayButton(parentGroupId, button) {
      console.log('loading ' + button.text)
        if (button.type === "button.simple") {
            $("#" + parentGroupId).append("<div class='row'><button class='btn-lg btn-info' id='" + getId(button.id) + "'>" + button.text + "</button></div>");
            $("#" + getId(button.id)).click(function () {
                $.post({url: "/buttons/" + button.id});
            });
        }
        if (button.type === "button.toggle") {
            $("#" + parentGroupId).append("<div class='row'>" + button.text + ": <label class='switch'><input type='checkbox' id='" + getId(button.id) + "'><span class='slider round'></span></label></button></div>");
            $("#" + getId(button.id)).click(function () {
                $.post({url: "/buttons/" + button.id, data: JSON.stringify({value: $("#" + getId(button.id)).prop('checked')}), contentType: "application/json"})
            });
            if(button.state) {
                $("#" + getId(button.id)).prop('checked', true);
            }
        }
    }

    function displayGroup(group) {
      name = group || "Unassigned";
      var uniqueID = new Date().getTime();
      $("#group-tabs").append('<button class=\"w3-bar-item w3-button\" onclick=\"openGroup(\'' + uniqueID + '\')\">' + name + '</button>');

      $("#groups").append('<div id="' + uniqueID + '" class="container col-xs-offset-3 col-xs-6 text-center group"></div>')
      console.log('loading group ' + name);
      loadButtons(group, uniqueID)
    }

    function displayGroups(data) {
      data.groups.forEach(displayGroup);
    }

    function displayButtons(groupId, data) {
        data.buttons.forEach(function (button) { displayButton(groupId, button); });
    }

    function displayButtonsInGroup(data, group, groupId) {
      data.buttons = data.buttons.filter(button => {
        return button.group == group
      });
      displayButtons(groupId, data);
    }

    function loadButtons(group, groupId) {
        $.ajax({
            url: "/buttons",
            success: function(data) {
              displayButtonsInGroup(data, group, groupId)
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
