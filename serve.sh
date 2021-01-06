#!/usr/bin/env bash

set -Eeuo pipefail

pipenv run python3 websockets_midi/app.py
