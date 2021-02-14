# Kid Monitor

There are two parts to this project:

1. Python http server - the "observer"
2. Python OSX client - the "monitor"

# Server

## Running locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

FLASK_APP=observer.py python -m flask run --host=0.0.0.0

open http://localhost:5000
```

## Running using piku

```bash
git remote add piku $PIKU_SERVER:kidmonitor
git push piku master
piku logs # verify all is well (assumes piku-cli installed)
open "http://$(echo $PIKU_SERVER | cut -d@ -f2):5000/"
```

