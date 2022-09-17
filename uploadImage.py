import requests
apiGatewayUrl = "<URL OF API GATEWAY>"
s3BucketName = '<Name of the S3 bucket to store original images>'

# This function will invoke the REST API Hosted on API Gateway
# The API Gateway uploades image to S3 bucket
# Event notifications enabled on S3 will trigger an SQS queue
# The SQS queue is a trigger for the lambda function 'generateThumbnail'
# The lambda function will fetch the image from S3 and generates a thumbnail
# The thumbnail is uploaded to another S3 bucket

# All these happen when the user runs this python script.


def uploadImage(image):
    invocationString = apiGatewayUrl + s3BucketName + image
    data = open(image, 'rb').read()
    r = requests.put(invocationString, data=data, headers={
        'content-type': 'application/octatestream'
    })
    print(r)


# Make sure the image is in the same directory as this python script
imageToBeUploaded = input("Enter the name of the image to be uploaded\n")
uploadImage(imageToBeUploaded)
