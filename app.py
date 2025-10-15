from fastapi import FastAPI, Response

app = FastAPI()

KEYS = ["A12fjkmajçop3DSFS"]

@app.get("/keys")
def get_keys_raw():
    content = "\n".join(KEYS)
    return Response(content=content.strip(), media_type="text/plain; charset=utf-8")
