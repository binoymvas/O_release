# Copyright 2017 Objectif Libre
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging

from django.utils.translation import ugettext_lazy as _
from horizon import forms

from cloudkittydashboard.api import cloudkitty as api

LOG = logging.getLogger(__name__)


class EditPriorityForm(forms.SelfHandlingForm):
    priority = forms.IntegerField(label=_("Priority"), required=True)

    def handle(self, request, data):
        ck_client = api.cloudkittyclient(request)
        return ck_client.modules.update(
            module_id=self.initial["module_id"],
            priority=data["priority"]
        )