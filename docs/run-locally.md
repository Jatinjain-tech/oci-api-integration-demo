# Run Functions Locally

## Python
1. Create a virtual environment:
python -m venv venv
source venv/bin/activate
pip install flask

2. Run this small wrapper:
```python
from flask import Flask, jsonify
import func, json
app = Flask(__name__)
@app.route('/python/hello')
def hello():
    return jsonify(json.loads(func.handler(None)))
app.run(port=5001)

	3.	Open http://localhost:5001/python/hello
