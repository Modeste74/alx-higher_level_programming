#!/bin/bash
# takes a URL sends POST request and displays the body reponse
curl -s --request POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
