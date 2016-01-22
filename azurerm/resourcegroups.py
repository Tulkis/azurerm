#!/usr/bin/env python

"""
Copyright (c) 2016, Guy Bowerman
Description: Core utility functions
License: MIT (see LICENSE.md for details)
"""

# resourcegroups.py - azurerm functions for Resource Groups

from .settings import azure_rm_endpoint, BASEAPI
from .restfns import do_delete, do_get, do_put

def create_resource_group(access_token, subscription_id, rgname, location):
    endpoint = ''.join([azure_rm_endpoint,
						'/subscriptions/', subscription_id,
						'/resourcegroups/', rgname,
						'?api-version=', BASEAPI])
    body = ''.join(['{\n   "location": "', location, '"\n}'])
    return do_put(endpoint, body, access_token)

def delete_resource_group(access_token, subscription_id, rgname):
    endpoint = ''.join([azure_rm_endpoint,
						'/subscriptions/', subscription_id,
						'/resourcegroups/', rgname,
						'?api-version=', BASEAPI])
    return do_delete(endpoint, access_token)
	
# list_resource_groups(access_token, subscription_id)
def list_resource_groups(access_token, subscription_id):
    endpoint = ''.join([azure_rm_endpoint,
                        '/subscriptions/', subscription_id,
						'/resourceGroups/',
						'?api-version=', BASEAPI])
    return do_get(endpoint, access_token)