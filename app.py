from fastapi import FastAPI, Response

app = FastAPI()

KEY_VALUE = "A12fjkmajçop3DSFS"

@app.get("/keys")
def get_keys_raw():
    # Retorna texto puro (sem JSON)
    return Response(content=KEY_VALUE, media_type="text/plain; charset=utf-8")
