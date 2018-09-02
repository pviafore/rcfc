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
* Groups: A list of strings stating the groups that the button belongs to (can be empty)
* Button-specific fields


#### Simple Buttons
A button that you can press, containing some text

Data:
```
{
  "id": <id>,
  "type": "button.simple",
  "groups": "List of groups"
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
    "groups": "List of groups"
    "state": True/False
    "text": "Label for the toggle"
}
```
To interact with this button, send a POST request to `/buttons/<id>` and pass it a json object `{value: true/false}`

### Slider Inputs
A slider with a range
Data:
```
{
    "id": <id>,
    "type": "input.slider",
    "groups": "List of groups",
    "state": current slider value,
    "min": minimum of slider,
    "max": maximum of slider,
    "text": "Label for the slider"
}
```

To interact with this button, send a POST request to `/buttons/<id>` and pass it a json object `{value: <value of slider>}`

### Left/Right Arrow Inputs
Arrows that can be left or right
Data:
```
{
    "id": <id>,
    "type": "input.leftright",
    "groups": "List of groups",
    "text": "Label for the arrows"
}
```

To interact with this button, send a POST request to `/buttons/<id>` and pass it a json object `{value: left/right>}`

### Colorpicker Inputs
Allows for RGB values to be set
Data:
```
{
    "id": <id>,
    "type": "input.colorpicker",
    "groups": "List of groups",
    "state": Current color
    "text": "Label for the colorpicker"
}
```

To interact with this button, send a POST request to `/buttons/<id>` and pass it a json object `{value: [red, green, blue]}`, where red,green, and blue are values from 0 to 255.