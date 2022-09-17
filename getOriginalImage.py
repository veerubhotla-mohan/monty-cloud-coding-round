import requests
import shutil
apiGatewayUrl = "<URL OF API>"
s3BucketName = '<Name of the S3 bucket containing original images>'

# This scripts fetches the original image uploaded by the user


def getOriginalImage(image):
    invocationString = apiGatewayUrl + s3BucketName + image
    res = requests.get(invocationString, stream=True)
    if res.status_code == 200:
        with open(image, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ', image)
    else:
        print('Image Couldn\'t be retrieved')


imageToBeFetched = input("Enter the name of the image to be fetched\n")
getOriginalImage(imageToBeFetched)
