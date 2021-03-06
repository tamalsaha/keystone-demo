#!/usr/bin/python

from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
from pprint import pprint
import os

def main():
	AUTH_URL = os.getenv('OS_AUTH_URL')
	USERNAME = os.getenv('OS_USERNAME')
	USER_DOMAIN_NAME = os.getenv('OS_USER_DOMAIN_NAME')
	PASSWD = os.getenv('OS_PASSWORD')
	PROJECT_ID = os.getenv('OS_PROJECT_ID')
	PROJECT_NAME = os.getenv('OS_PROJECT_NAME')

	pprint('AUTH_URL = ' + AUTH_URL)
	pprint('USERNAME = ' + USERNAME)
	pprint('USER_DOMAIN_NAME = ' + USER_DOMAIN_NAME)
	pprint('PASSWD = ' + PASSWD)
	pprint('PROJECT_ID = ' + PROJECT_ID)
	pprint('PROJECT_NAME = ' + PROJECT_NAME)

	auth = v3.Password(auth_url=AUTH_URL,
		username=USERNAME,
		user_domain_name=USER_DOMAIN_NAME,
		password=PASSWD,
		project_id=PROJECT_ID,
		project_name=PROJECT_NAME)
	sess = session.Session(auth=auth)
	keystone = client.Client(session=sess)
	app_cred = keystone.application_credentials.create(
		name='kubernetes')
	pprint(app_cred.to_dict())

if __name__ == "__main__":
	main()
