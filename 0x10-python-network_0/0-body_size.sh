#!/bin/bash
# Script to get the size in byte of the body response from request sent
curl -so /dev/null -w '%{size_download}\n' $1
