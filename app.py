from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient, results
import openai
import asyncio

app = Flask(__name__)

client = MongoClient('mongodb+srv://sv695177_db_user:1w0OJ89Dl9j8hqI9@task.ovypzkn.mongodb.net/?appName=task')
db = client['intucate_db']
prompts = db['prompts']
history = db['history']


openai.api_key = 'Removed API Key'



@app.route("/ask", methods=["POST"])

def ask():
    try:
        data = request.json
        user_input = data["userInput"]
        
        prompt_doc = prompts.find_one({"_id": "Education_Prompt"})
        if not prompt_doc:
            return jsonify({"error": "Template not found"}), 404
        
        template = prompt_doc["template"]
        
        final_prompt = template.replace("{userInput}", user_input)

        answer = f"This is a simulated AI response for: {user_input}. (OpenAI Quota Exceeded)"

        history.insert_one({
            "user_input": user_input,
            "response": answer
        })
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

async def get_response(question):
    template = prompts.find_one({"_id": "Educational_Prompt"})["template"]
    final_prompt = template.replace("{userInput}", question)

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": final_prompt}]
    )
    return response["choices"][0]["message"]["content"]

@app.route("/ask-batch", methods=["POST"])
async def ask_batch():
    data = request.json
    questions = data["inputs"]

    tasks = [get_response(q) for q in questions]
    responses = await asyncio.gather(*tasks)

    return jsonify({"responses": results})

if __name__ == "__main__":
    app.run(debug=True)