from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import io

## Have to install older version azure-cognitiveservices-vision-computervision to use ComputerVisionClient
##  pip install azure.cognitiveservices.vision.computervision

endpoint = "https://vision28.cognitiveservices.azure.com/"
key = "1T7y3swMPX0zw6PMQznxSzz1xOjPqUpw9NzwGvx7TtNwDmxPB443JQQJ99CFACYeBjFXJ3w3AAAFACOGFF4W"

client = ComputerVisionClient(endpoint,CognitiveServicesCredentials(key))

with open("C:\data\Artificial-Intelligence\Images\Microsoft.png", "rb") as image:
    image_data = image.read()   

# bytes does not have have read method, so convert into stream using io.BytesIO
image_stream = io.BytesIO(image_data) 

response = client.analyze_image_in_stream(image=image_stream, visual_features=[VisualFeatureTypes.brands])

for brand in response.brands:
    print(f"Brand: {brand.name}, Confidence: {brand.confidence}")