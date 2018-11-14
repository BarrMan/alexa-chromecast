# Alexa Chromecast Skill

Allows Amazon Alexa to control Google Chromecast

> Alexa, tell chromecast to pause

> Alexa, tell chromecast to play

> Alexa, tell chromecast to play MKBHD

> Alexa, tell chromecast to play The Big Lebowski trailer
>
> Alexa, tell chromecast to set the volume to 5

> Alexa, tell chromecast to stop

## How it works

Alexa skills run in the cloud, but this skill needs to be on your local network to control the Chromecast.
This skill implements a hybrid approach: the command is handled by Alexa on AWS, which sends a notification to your local server.

The Lambda component is in `src/lambda`, and the local component is in `src/local`.

![Architecture Overview](docs/diagram.jpg "Architecture Overview")

Both the ChromeCast and the Raspberry Pi (or whatever the local notification handler will run on) **MUST** be on the same network in order for the ChromeCast to be discoverable.

## Dependencies

Installation requires a UNIX environment with:

- BASH
- Python 2.7
- [Pip](https://pip.pypa.io/en/stable/installing/)

## Setup and installation

1. Create an [Amazon Web Services](http://aws.amazon.com/) account
2. Run aws-setup.sh to create a Role, Lambda Function, and SNS Topic. (*It will run `aws configure`, so have an key id and access key ready*)
3. Go to developer.amazon.com and create a Skill mapped to the Lambda function ARN, intentSchemas and sample utterances are in `config/`.
4. Install local dependencies with `sudo pip install -r ./src/local/requirements.txt`
5. Run `./start.sh` to start the listener.
6. Ask Alexa to tell Chromecast to do something.

### Shell example

  `./start.sh`

### Docker

The skill subscriber can be run with docker:

`docker run --network="host" -it -e 'AWS_ACCESS_KEY_ID=...' -e 'AWS_SECRET_ACCESS_KEY=...' -e 'AWS_DEFAULT_REGION=...' -e 'AWS_SNS_TOPIC_ARN=...' lukechannings/alexa-skill-chromecast`

### Environment variables

The skill subscriber (local) uses these environment variables:

- **AWS_SNS_TOPIC_ARN** - AWS SNS Topic ARN (can be found in the `.env` file after running `aws-setup.sh`)
- **CHROMECAST_NAME** - Friendly name of the Chromecast to send commands to. (Defaults to 'Living Room')
- **PORT** - (Optional) Externally accessible port to expose the SNS handler on.

- **AWS_ACCESS_KEY_ID** - AWS User Access Key
- **AWS_SECRET_ACCESS_KEY** - AWS Secret Access Key
- **AWS_DEFAULT_REGION** - AWS Lambda and SNS Region (e.g. eu-west-1)

If you have run `aws configure`, you will not need to set AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, or AWS_DEFAULT_REGION.


## Scripts

### aws-setup.sh

Sets up an AWS environment for the Alexa Skil:

1. Creates an IAM role for Alexa (with permissions for SNS)
2. Creates an SNS topic to communicate over
3. Creates a Lambda function

### build-lambda-bundle.sh

Creates a lambda-bundle.zip, which can be uploaded to an AWS Lambda function.

### aws-update-lambda.sh

Runs build-lambda-bundle and automatically uploads the bundle to AWS Lambda.


## FAQ

### "No Chromecasts found"

When the local service starts it searches for ChromeCasts on the network. If there are no ChromeCasts found, it will exit.

To fix this, you must confirm that the ChromeCast is on and working, make sure you can access it from your phone, and make sure that everything is on the same network.

To debug, a tool to search and list found ChomeCasts is provided at `./search-chromecasts` (make sure to make it executable with `chmod +x ./search-chromecasts`).
