#!/bin/bash
# takes URL sends request and return size
curl -s "$1" | wc -c
