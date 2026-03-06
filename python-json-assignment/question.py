import json

# JSON-formatted API response string
api_response = '''
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''

# Parse JSON string into Python dictionary
data = json.loads(api_response)

# Extract required fields
request_id = data["id"]
status = data["status"]
text_result = data["result"]["text"]
confidence = data["result"]["confidence"]

# Print extracted values
print("Request ID:", request_id)
print("Status:", status)
print("Text:", text_result)
print("Confidence:", confidence)

# Warning if confidence is low
if confidence < 0.9:
    print("Warning: Confidence score is below acceptable threshold.")

# Create a new follow-up result dictionary
follow_up_result = {
    "id": request_id,
    "status": "processed",
    "message": "Result stored successfully"
}

# Convert dictionary to JSON string
json_output = json.dumps(follow_up_result, indent=2)

# Write JSON output to file
with open("response.json", "w") as file:
    file.write(json_output)
