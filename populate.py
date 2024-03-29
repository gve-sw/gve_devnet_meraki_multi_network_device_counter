""" Copyright (c) 2023 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import config
import meraki
import csv

dashboard = meraki.DashboardAPI(api_key=config.meraki_api_key, print_console=True,output_log=False)

my_networks = dashboard.organizations.getOrganizationNetworks(organizationId=config.org_id)
data = []

for network in my_networks:
    temp = (network["id"],network["name"])
    data.append(temp)

# Write CSV file
with open("networks.csv", "w",newline="") as fp:
    writer = csv.writer(fp, delimiter=",")

    # write header of csv file
    writer.writerow(["org_id", "org_name"])
    writer.writerows(data)