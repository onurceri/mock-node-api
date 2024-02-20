
# node-mock-api

  

## Overview

This api just created to test https://github.com/onurceri/swisscom-coding-challenge repository.

  

To start 3 api instances with the following ports 8001, 8002, 8003:

```shell
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn  main:app  --port  8001  --reload
uvicorn  main:app  --port  8002  --reload
uvicorn  main:app  --port  8003  --reload
```
