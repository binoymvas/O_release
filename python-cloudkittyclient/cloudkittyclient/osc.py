# Copyright 2014 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from cloudkittyclient import client as ckclient

DEFAULT_API_VERSION = '1'
API_VERSION_OPTION = 'os_rating_api_version'
API_NAME = "rating"
API_VERSIONS = {
    "1": "cloudkittyclient.v1.client.Client",
}


def make_client(instance):
    """Returns a rating service client."""
    version = instance._api_version[API_NAME]
    version = int(version)
    auth_config = instance.get_configuration()['auth']
    return ckclient.get_client(version, **auth_config)


def build_option_parser(parser):
    """Hook to add global options."""
    return parser
