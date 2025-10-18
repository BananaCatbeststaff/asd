from fastapi import FastAPI, Response

app = FastAPI()

KEYS = ["5yh67y6457y4674y675"]

@app.get("/keys")
def get_keys_raw():
    content = "\n".join(KEYS)
    return Response(content=content.strip(), media_type="text/plain; charset=utf-8")
