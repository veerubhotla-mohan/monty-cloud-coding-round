import requests
apiGatewayUrl = "<URL OF THE API GATEWAY>"
s3BucketName = 'montycloudcoding/'


def uploadImageToS3(image):
    invocationString = apiGatewayUrl + s3BucketName + imageToBeUploaded
    print(invocationString)
    r = requests.put(invocationString)
    print(r)


imageToBeUploaded = 'image.jpeg'
uploadImageToS3(imageToBeUploaded)
