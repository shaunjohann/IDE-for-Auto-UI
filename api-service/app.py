import os
from dbk_aicode.base import generate_req_handler
from flask import Flask, request

app = Flask(__name__)


@app.route("/generate", methods = ['POST'])
def generate():
		body = request.json

		project_id = body['projectId']
		blocks = body['blocks']
		method = body['method']

		final_prompt, js_code = generate_req_handler(project_id=project_id, blocks=blocks, method=method)

		return { 'code': js_code.strip('`').strip(), 'prompt': final_prompt }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
