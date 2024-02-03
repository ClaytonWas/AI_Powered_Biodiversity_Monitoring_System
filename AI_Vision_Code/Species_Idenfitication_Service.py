from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch
from msrest.authentication import ApiKeyCredentials 
import numpy as np


ENDPOINT = "<endpoint>"

# Replace with a valid key
training_key = "<key>"
credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
publish_iteration_name = "classifyMushroomModel"

trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

# Create a new project
print ("Creating project...")
project = trainer.create_project("Mushroom Classification")

print("Project created!")


