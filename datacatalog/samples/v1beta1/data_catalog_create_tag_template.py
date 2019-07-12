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

# DO NOT EDIT! This is a generated sample ("Request",  "data_catalog_create_tag_template")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-datacatalog

# sample-metadata
#   title:
#   description: Create Tag Template
#   usage: python3 samples/v1beta1/data_catalog_create_tag_template.py [--project_id "[Google Cloud Project ID]"] [--location_id "[Google Cloud Location ID]"]
import sys

# [START data_catalog_create_tag_template]

from google.cloud import datacatalog_v1beta1
from google.cloud.datacatalog_v1beta1 import enums


def sample_create_tag_template(project_id, location_id):
    """
    Create Tag Template

    Args:
      project_id Your Google Cloud project ID.
      location_id Google Cloud region, e.g. us-central1.
    """

    client = datacatalog_v1beta1.DataCatalogClient()

    # project_id = '[Google Cloud Project ID]'
    # location_id = '[Google Cloud Location ID]'
    parent = client.location_path(project_id, location_id)

    # Tag Template ID.
    tag_template_id = "sample_tag_template"
    display_name = "Sample Tag Template"
    display_name_2 = "Source of data asset"
    primitive_type = enums.FieldType.PrimitiveType.STRING
    type_ = {"primitive_type": primitive_type}
    fields_item = {"display_name": display_name_2, "type": type_}
    display_name_3 = "Number of rows in data asset"
    primitive_type_2 = enums.FieldType.PrimitiveType.DOUBLE
    type_2 = {"primitive_type": primitive_type_2}
    fields_item_2 = {"display_name": display_name_3, "type": type_2}
    display_name_4 = "Has PII"
    primitive_type_3 = enums.FieldType.PrimitiveType.BOOL
    type_3 = {"primitive_type": primitive_type_3}
    fields_item_3 = {"display_name": display_name_4, "type": type_3}
    display_name_5 = "PII type"
    display_name_6 = "EMAIL"
    allowed_values_element = {"display_name": display_name_6}
    display_name_7 = "SOCIAL SECURITY NUMBER"
    allowed_values_element_2 = {"display_name": display_name_7}
    display_name_8 = "NONE"
    allowed_values_element_3 = {"display_name": display_name_8}
    allowed_values = [
        allowed_values_element,
        allowed_values_element_2,
        allowed_values_element_3,
    ]
    enum_type = {"allowed_values": allowed_values}
    type_4 = {"enum_type": enum_type}
    fields_item_4 = {"display_name": display_name_5, "type": type_4}
    fields = {
        "source": fields_item,
        "num_rows": fields_item_2,
        "has_pii": fields_item_3,
        "pii_type": fields_item_4,
    }

    # The Tag Template.
    tag_template = {"display_name": display_name, "fields": fields}

    response = client.create_tag_template(parent, tag_template_id, tag_template)
    print(u"Template name: {}".format(response.name))


# [END data_catalog_create_tag_template]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--project_id", type=str, default="[Google Cloud Project ID]")
    parser.add_argument("--location_id", type=str, default="[Google Cloud Location ID]")
    args = parser.parse_args()

    sample_create_tag_template(args.project_id, args.location_id)


if __name__ == "__main__":
    main()
