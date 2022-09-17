import requests
apiGatewayUrl = "<API GATEWAY URL>"
s3BucketName = "<Name of S3 Bucket>"


def uploadImageToS3(image):
    invocationString = apiGatewayUrl + s3BucketName + image
    print(invocationString)
    r = requests.put(invocationString)
    print(r)


imageToBeUploaded = 'image.jpeg'
uploadImageToS3(imageToBeUploaded)
