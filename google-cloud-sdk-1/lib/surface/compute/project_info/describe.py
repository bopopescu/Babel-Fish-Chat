# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Command for describing the project."""

from __future__ import absolute_import
from __future__ import unicode_literals
from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.projects import util
from googlecloudsdk.core import properties


class Describe(base.DescribeCommand):
  """Describe the Google Compute Engine project resource."""

  def Run(self, args):
    holder = base_classes.ComputeApiHolder(self.ReleaseTrack())
    client = holder.client

    project_ref = util.ParseProject(properties.VALUES.core.project.GetOrFail())

    return client.MakeRequests([(client.apitools_client.projects, 'Get',
                                 client.messages.ComputeProjectsGetRequest(
                                     project=project_ref.projectId))])[0]


Describe.detailed_help = {
    'brief': 'Describe the Google Compute Engine project resource',
    'DESCRIPTION': """\
        *{command}* displays all data associated with the Google
        Compute Engine project resource. The project resource contains
        data such as global quotas, common instance metadata, and the
        project's creation time.
        """,
}
