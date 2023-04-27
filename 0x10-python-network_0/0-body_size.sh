#!/bin/bash
# Script to get the size  of the body response from request sent
curl -s '$1' | wc -c
