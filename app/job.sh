#!/bin/bash

scriptPath=$(dirname "$(readlink -f "$0")")
source "${scriptPath}/.env.sh"

# the docker-compose variables should be available here
$(which python3) /app/cmcscanner.py