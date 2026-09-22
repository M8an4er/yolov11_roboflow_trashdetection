import os
from inference_sdk import InferenceHTTPClient, InferenceConfiguration

# 1. Connect to your workflow using a hidden environment variable
api_key = os.environ.get("ROBOFLOW_API_KEY")

client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key=api_key
).configure(InferenceConfiguration(
    api_key_transport="header" 
))

# 2. Run your workflow on an image
result = client.run_workflow(
    workspace_name="tybargrind",
    workflow_id="trash-detection-vtrash-detection-ujrn0-qam3l-1-yolo11n-t1-logic",
    images={
        "image": "YOUR_IMAGE.jpg" # Change this to the path of your image file
    },
    use_cache=True 
)

# 3. Print your results
print(result)
