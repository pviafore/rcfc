# API Guide

RCFC uses a Rest API to provide buttons to whatever the UI is.


## Endpoints

### GET /buttons

This will return the following JSON information
```
{
    "buttons": [
                <button-1>,
                <button-2>,
                ...
                <button-n>
               ]
}
```

Each button will be its own JSON object, described below
Every button will have the following:

* ID: a string used for uniquely identifying buttons
* Type: A string stating the type (described below)
* Group: A string stating the group that the button belongs to (can be None)
* Button-specific fields

### /groups

This will return the following JSON information
```
{
  "groups": [
             <group-1>,
             <group-2>,
             ...
             <button-n>
            ]
}
```

This will be a unique set of Group references (String) that are currently referenced from buttons.

#### Simple Buttons
A button that you can press, containing some text

Data:
```
{
  "id": <id>,
  "type": "button.simple",
  "group": "Label for the Group"
  "text": <text of button>
}
```

The text is the text displayed on the actual button.

To interact with this button, send a POST request to `/buttons/<id>`

#### Toggle Buttons
A button that can be flipped on/off.

Data:
```
{
    "id": <id>,
    "type": "button.toggle",
    "group": "Label for the Group"
    "state": True/False
    "text": "Label for the Data"
}
```

To interact with this button, send a POST request to `/buttons/<id>` and pass it a json object `{value: true/false}`
