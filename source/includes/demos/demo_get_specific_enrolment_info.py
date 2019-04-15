
# -*- coding: utf-8 -*-
#
# Demo Get Specific Enrolment Info
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

def do_authentication(username, password, cognito_pool_id, cognito_client_id):
    wl = WarrantLite(username=username, password=password,
                     pool_id=cognito_pool_id, client_id=cognito_client_id,
                     client_secret=None)
    tokens = wl.authenticate_user()
    return tokens

def get_specific_enrolment_info(req_auth_headers, enrolment_id):
    parameters = {'eyn_api_key': '4f37a768-887f-427c-a784-95a818e60319'}
    # 'https://api.eyn.ninja/api/v1/dev/enrolments',
    response = requests.get('https://api.eyn-api.com/api/v1/dev/enrolments/' + enrolment_id,
                            params=parameters, headers=req_auth_headers)

    enrolment_info = json.loads(response.content)
    return enrolment_info

if __name__ == '__main__':
    print('[eyn-api-demo] Demo Get Specific Enrolment Info.')

    # Demo parameters - replace with your eyn credentials
    username = "demo@eyn-api.com"   # replace with your username
    password = "Def4ultP4ssw0rd!"   # replace with your password
    cognito_pool_id = ""            # replace with your cognito pool id
    cognito_client_id = ""          # replace with your cognito client id
    
    # First, we have to authenticate to AWS Cognito
    tokens = do_authentication(username, password, cognito_pool_id, cognito_client_id)
    
    req_auth_headers = {'Accept': '*/*',
                        'Content-Type': 'application/json; charset=UTF-8',
                        'Authorization': tokens['AuthenticationResult']['IdToken']}

    # Now, we can query EYN API to get specific information about an enrolment
    enrolment_info = get_specific_enrolment_info(req_auth_headers, 'd7bd8751-ea88-4e82-94d8-4940cc07eea8')

    # Let's print the information that we retrieved
    print('[eyn-api-demo] Results of querying /enrolments/d7bd8751-ea88-4e82-94d8-4940cc07eea8:')
    print('other_names: ' + enrolment_info["other_names"])
    print('family_name: ' + enrolment_info["family_name"])
    print('date_of_birth: ' + enrolment_info["date_of_birth"])
    if "link_identity_document_chip_face" in enrolment_info["images"]:
        print('link_identity_document_chip_face: ' + enrolment_info["images"]["link_identity_document_chip_face"])
    if "link_identity_document_image_front" in enrolment_info["images"]:
        print('link_identity_document_image_front: ' + enrolment_info["images"]["link_identity_document_image_front"])
    if "link_identity_document_image_mrz" in enrolment_info["images"]:
        print('link_identity_document_image_mrz: ' + enrolment_info["images"]["link_identity_document_image_mrz"])
    if "link_user_selfie" in enrolment_info["images"]:
        print('link_user_selfie: ' + enrolment_info["images"]["link_user_selfie"])
    print('right_to_work_status: ' + enrolment_info["right_to_work_status"])
    print('mrz_verified: ' + str(enrolment_info["mrz_verified"]))
    print('is_biometric: ' + str(enrolment_info["is_biometric"]))
