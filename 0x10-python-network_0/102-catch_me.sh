#!/bin/bash
# makes request to 0.0.0.0:5000/catch_me to respond with a message "You got me!"
curl -s 0.0.0.0:5000/catch_me | grep -o "You got me!"
