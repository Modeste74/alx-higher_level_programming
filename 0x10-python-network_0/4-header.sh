#!/bin/bash
# sends a GET request to the URL
curl -s --request GET -H "X-School-User-Id: 98" "$1"
