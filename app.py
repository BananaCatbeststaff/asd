# file: app.py
from fastapi import FastAPI, Response

app = FastAPI()

KEY_VALUE = "A12fjkmajçop3DSFS"

@app.get("/keys")
def get_keys_raw():
    # Retorna texto simples (raw) com encoding UTF-8
    return Response(content=KEY_VALUE, media_type="text/plain; charset=utf-8")


