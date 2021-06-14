# CLGHouseBot

for CLG House Server



## Quickstart

------------
## Docker Compose (Recommended)

```
$ cat <<-'EOF' > bot.env
TOKEN=<< DISCORD BOT TOKEN >>
GOOGLE_APPLICATION_CREDENTIALS=client_secret.json
EOF
```

`$ docker-compose up --build -d bot`

## Manual (Local Python Environment)

`$ brew install postgresql`

`$ pip install -r requirements.txt`

`$ export TOKEN=<< DISCORD BOT TOKEN >>`

`$ export GOOGLE_APPLICATION_CREDENTIALS=client_secret.json`

`$ python run_bot.py`
