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

# DO NOT EDIT! This is a generated sample ("Request",  "data_catalog_lookup_entry_sql_resource")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-datacatalog

# sample-metadata
#   title:
#   description: Lookup Entry using SQL resource
#   usage: python3 samples/v1beta1/data_catalog_lookup_entry_sql_resource.py [--sql_name "[SQL Resource Name]"]
import sys

# [START data_catalog_lookup_entry_sql_resource]

from google.cloud import datacatalog_v1beta1
from google.cloud.datacatalog_v1beta1 import enums

def sample_lookup_entry(sql_name):
  """
    Lookup Entry using SQL resource

    Args:
      sql_name The SQL name of the Google Cloud Platform resource the Data Catalog
      entry represents.
      Examples:
      bigquery.table.`projectId`.`datasetId`.`tableId`
      pubsub.topic.`projectId`.`topicId`
    """

  client = datacatalog_v1beta1.DataCatalogClient()

  # sql_name = '[SQL Resource Name]'
  response = client.lookup_entry(sql_resource=sql_name)
  entry = response
  print(u'Entry name: {}'.format(entry.name))
  print(u'Entry type: {}'.format(enums.EntryType(entry.type).name))
  print(u'Linked Resource name: {}'.format(entry.linked_resource))
  print(u'Display name: {}'.format(entry.display_name))
  print(u'Description: {}'.format(entry.description))
# [END data_catalog_lookup_entry_sql_resource]

def main():
  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument('--sql_name', type=str, default='[SQL Resource Name]')
  args = parser.parse_args()

  sample_lookup_entry(args.sql_name)

if __name__ == '__main__':
  main()