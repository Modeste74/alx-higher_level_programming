#!/bin/bash
# sends request and displayed only status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
