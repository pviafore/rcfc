# rcfc - Remote Control For Computers
Welcome to RCFC.  This is a pet project started to help out with some automation around the house.

It provides a way to write Python functions that can be exposed as buttons on a website.  There are plans to make an Android app that would automatically connect to RCFC servers and provide a UI to the user.  For now, we have to deal with a ugly website UI (if you want to spruce it up, feel free to submit a PR)

## Installing (In-Progress)

Just `pip install rcfc` (not available yet)

## There's barely any types of buttons!

So, in typical open source fashion, this is a work in progress.  Buttons will be added as time goes on, such as color-picker buttons, input buttons, toggles and more.  Write an issue if there's something you'd like to see (or submit a PR)  


## Demo
There is a built-in demo if you'd like to see it in action.  Simply execute rcfc_demo on your shell (or make demo if you're in the project) and a demo server will launch on port 7232.
Open up http://localhost:7232 to see buttons that are available.  You can see the source code at [demo source code](rcfc/demo.py)

## Why Bottle, Why not use Flask, Django, Pyramid, etc.?
Bottle had a very small footprint and very few dependencies.  The goal is to get this project up and going as quickly as possible.