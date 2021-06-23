import requests
import json

url = "https://vision.googleapis.com/v1/images:annotate"

payload = json.dumps({
  "requests": [
    {
      "image": {
        "source": {
          "imageUri": "https://storage.googleapis.com/download/storage/v1/b/odm-sml-bucket/o/dog.jpeg%22?generation=1624440054505494&alt=media"
        }
      },
      "features": [
        {
          "maxResults": 10,
          "type": "OBJECT_LOCALIZATION"
        }
      ]
    }
  ]
})
headers = {
  'Authorization': 'Bearer ya29.c.KqYBAwj1I5iWpwl-1ultn9pxoVo0OG88kPoFNgT5e0xDfdFReYJ7FoHB2_GejKRxRoy7E-bRFFU5_pLxuaE41eg0D_qyBP1Twibb4X6bn1d3K9n3dFgKlKW31DmnaFAQIVQhqqE9iyp4jalTXTbew6BWqCorcXlcZHNunqKcpJq0A2EI-yjgjn0eylJFVqbsi54563A-rdj-N3LrNXH7rztWrLgfnP-p1A',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
