from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import json

endpoint = "https://vision28.cognitiveservices.azure.com/"
key = "1T7y3swMPX0zw6PMQznxSzz1xOjPqUpw9NzwGvx7TtNwDmxPB443JQQJ99CFACYeBjFXJ3w3AAAFACOGFF4W"

client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

with open(r"C:\data\Artificial-Intelligence\Images\Guru Gobind Singh G.png", "rb") as image:
    image_data = image.read()

response = client.analyze(image_data=image_data, visual_features=[VisualFeatures.TAGS, VisualFeatures.CAPTION])

print(json.dumps(response.as_dict(), indent=4))