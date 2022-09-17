import requests
apiGatewayUrl = "https://g3ycrq1bqh.execute-api.ap-south-1.amazonaws.com/dev/"
s3BucketName = 'montycloudcoding/'


def uploadImageToS3(image):
    invocationString = apiGatewayUrl + s3BucketName + image
    print(invocationString)
    r = requests.put(invocationString)
    print(r)


imageToBeUploaded = 'image.jpeg'
uploadImageToS3(imageToBeUploaded)
