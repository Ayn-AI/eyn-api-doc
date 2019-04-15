# -*- coding: utf-8 -*-
#
# Demo Get Enrolments
#   Author: robin@eyn.vision
#   web:    https://eyn.vision
#
#   Requirements:
#       * warrant-lite (pip install warrant-lite)
#
# Eyn API is available at https://api.eyn.ninja. Documentation of the API is available at xxx
# (c) 2019 eyn ltd

from warrant_lite import WarrantLite
import requests
import json
import datetime

def do_authentication(username, password, cognito_pool_id, cognito_client_id):
    wl = WarrantLite(username=username, password=password,
                     pool_id=cognito_pool_id, client_id=cognito_client_id,
                     client_secret=None)
    tokens = wl.authenticate_user()
    return tokens


def get_enrolments(req_auth_headers):
    parameters = {'start_time': 0,
                  'end_time': str(int(datetime.datetime.now().strftime('%s'))*1000),
                  'eyn_api_key': '4f37a768-887f-427c-a784-95a818e60319'}

    response = requests.get('https://api.eyn.ninja/api/v1/dev/enrolments',
                            params=parameters, headers=req_auth_headers)
    body = json.loads(response.content)
    enrolment_ids = body["enrolment_ids"]
    return enrolment_ids


if __name__ == '__main__':
    print('[eyn-api-demo] Demo Get Enrolments')

    # Demo parameters - replace with your eyn credentials
    username = "robin@eyn.vision" #"demo@eyn-api.com"   # replace with your username
    password = "Thisisjusta#t3st" #"Def4ultP4ssw0rd!"   # replace with your password
    cognito_pool_id = "eu-west-2_C949RROW5"             # replace with your cognito pool id
    cognito_client_id = "2t8ltq7ecpfmr1snoah8d22bha"    # replace with your cognito client id
    
    # First, we have to authenticate to AWS Cognito
    tokens = do_authentication(username, password, cognito_pool_id, cognito_client_id)

    req_auth_headers = {'Accept': '*/*',
                        'Content-Type': 'application/json; charset=UTF-8',
                        'Authorization': tokens['AuthenticationResult']['IdToken']}

    # Now, we can query EYN API to get a list of enrolments
    enrolment_ids = get_enrolments(req_auth_headers)

    # Let's print the list of enrolments that we retrieved
    print('[eyn-api-demo] Results of querying /enrolments')
    for enrolment_id in enrolment_ids:
        print('enrolment_id :' + enrolment_id["enrolment_id"])

