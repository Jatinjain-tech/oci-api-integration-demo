import io
import json

def handler(ctx, data: io.BytesIO = None):
    response = {"message": "Hello from Python on OCI!"}
    return json.dumps(response)
