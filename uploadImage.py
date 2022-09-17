import requests
apiGatewayUrl = "APIGATEWAYURL"
s3BucketName = 'montycloudcoding/'


def uploadImageToS3(image):
    invocationString = apiGatewayUrl + s3BucketName + image
    print(invocationString)
    r = requests.put(invocationString)
    print(r)


imageToBeUploaded = 'image.jpeg'
uploadImageToS3(imageToBeUploaded)
