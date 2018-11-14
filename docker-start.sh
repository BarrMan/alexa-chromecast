#!/usr/bin/env bash -e

source .env

AWS_ACCESS_KEY_ID="$( /usr/bin/awk -F' = ' '$1 == "aws_access_key_id" {print $2}' ~/.aws/credentials )"
AWS_SECRET_ACCESS_KEY="$( /usr/bin/awk -F' = ' '$1 == "aws_secret_access_key" {print $2}' ~/.aws/credentials )"
AWS_DEFAULT_REGION="$( /usr/bin/awk -F' = ' '$1 == "region" {print $2}' ~/.aws/config )"

if [[ $1 == "--build" ]]; then
  docker build -t lukechannings/alexa-skill-chromecast .
fi

docker run --network="host" -it\
 -e "AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID"\
 -e "AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY"\
 -e "AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION"\
 -e "AWS_SNS_TOPIC_ARN=$AWS_SNS_TOPIC_ARN"\
 -e "CHROMECAST_NAME=$CHROMECAST_NAME"\
 lukechannings/alexa-skill-chromecast
