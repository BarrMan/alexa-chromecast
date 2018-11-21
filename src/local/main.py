#!/usr/bin/env python2.7

"""
Required Environment Variables:

AWS_ACCESS_KEY_ID = "UJiu/Umqq76t7GKYg5j14k2CnlQxzbxODUWabELv" # - AWS User Access Key (IAM)
AWS_SECRET_ACCESS_KEY = "AKIAJT2M4GQLJ5KJWTMQ" # - AWS Secret Access Key (IAM)
AWS_DEFAULT_REGION = "eu-west-1" # - AWS Lambda and SNS Region (e.g. eu-west-1)
AWS_SNS_TOPIC_ARN = "arn:aws:sns:eu-west-1:201661578604:alexa-chromecast" # - AWS SNS Topic ARN (e.g. arn:aws:sns:eu-west-1:236205202378:Alexa-Chromecast) 
PORT = "3306" # - Hardcode external port.
CHROMECAST_NAME = "Bedroom TV" # - name of the Chromecast to send commands to
"""
import os
from SkillSubscriber import Subscriber
from ChromecastSkill import Skill

PORT = os.getenv('PORT', False)

if __name__ == "__main__":
    chromecast_name = os.getenv('CHROMECAST_NAME', 'Bedroom TV')
    print 'chromecast_name=' + chromecast_name
    print 'PORT=' + PORT
    print 'Initializing ChromcastSkill'
    chromecast_skill = Skill(chromecast_name)
    print 'Initializing Chromecast Subscriber'
    Subscriber({'chromecast': chromecast_skill}, PORT)
