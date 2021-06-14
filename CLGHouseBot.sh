#!/usr/bin/env bash

flyway migrate

python /usr/src/app/run_bot.py
