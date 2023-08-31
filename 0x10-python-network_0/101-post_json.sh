#!/bin/bash
# sends a JSON post request and displays response
curl -s --request POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
