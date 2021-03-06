#!/usr/bin/python

from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
import pprint
import json
import create_ldap 
from create_ldap import create_instance

credentials = GoogleCredentials.get_application_default()
compute = discovery.build('compute', 'v1', credentials=credentials)

project = 'my-first-project'
zone = 'us-west1-a'

# what kind of machine is being requested and what should it's name be?
# based on the machine type, we can derrive a name

name = 'final-test'

def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items']

newinstance = create_instance(compute, project, zone, name)
instances = list_instances(compute, project, zone)

pprint.pprint(newinstance)
pprint.pprint(instances)
