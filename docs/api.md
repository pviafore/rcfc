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
* Button-specific fields

#### Simple Buttons
A button that you can press, containing some text

Data: 
```
{
  "id": <id>,
  "type": "button.simple",
  "text": <text of button>
}
```

The text is the text displayed on the actuall button.
 
To interact with this button, send a POST request to `/buttons/<id>`