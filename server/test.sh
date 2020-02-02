#!/bin/sh
PORT=`podman port -l | cut -d':' -f2`
curl -s --negotiate -u : localdev.redhatfsi.com:$PORT/envvars
