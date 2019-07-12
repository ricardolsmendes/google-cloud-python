# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT EDIT! This is a generated sample ("Request",  "data_catalog_delete_tag_template")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-datacatalog

# sample-metadata
#   title:
#   description: Delete Tag Template
#   usage: python3 samples/v1beta1/data_catalog_delete_tag_template.py [--project_id "[Google Cloud Project ID]"] [--location_id "[Google Cloud Location ID]"] [--tag_template_id "[Tag Template ID]"] [--force true]
import sys

# [START data_catalog_delete_tag_template]

from google.cloud import datacatalog_v1beta1


def sample_delete_tag_template(project_id, location_id, tag_template_id, force):
    """
    Delete Tag Template

    Args:
      project_id Your Google Cloud project ID.
      location_id Google Cloud region, e.g. us-central1.
      tag_template_id The Tag Template ID.
      force Confirms the deletion of any possible tags using the template.
    """

    client = datacatalog_v1beta1.DataCatalogClient()

    # project_id = '[Google Cloud Project ID]'
    # location_id = '[Google Cloud Location ID]'
    # tag_template_id = '[Tag Template ID]'
    # force = True
    name = client.tag_template_path(project_id, location_id, tag_template_id)

    client.delete_tag_template(name, force)


# [END data_catalog_delete_tag_template]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--project_id", type=str, default="[Google Cloud Project ID]")
    parser.add_argument("--location_id", type=str, default="[Google Cloud Location ID]")
    parser.add_argument("--tag_template_id", type=str, default="[Tag Template ID]")
    parser.add_argument("--force", type=bool, default=True)
    args = parser.parse_args()

    sample_delete_tag_template(
        args.project_id, args.location_id, args.tag_template_id, args.force
    )


if __name__ == "__main__":
    main()
