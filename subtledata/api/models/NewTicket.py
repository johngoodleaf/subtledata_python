#!/usr/bin/env python
"""
Copyright 2012 Wordnik, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class NewTicket:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'user_id': 'int',
            'number_of_people_in_party': 'int',
            'custom_ticket_name': 'str',
            'table_id': 'int',
            'revenue_center_id': 'int',
            'device_id': 'int'

        }


        #SubtleData User ID
        self.user_id = None # int
        #Number of people in party
        self.number_of_people_in_party = None # int
        #Custom Ticket Name to be Displayed
        self.custom_ticket_name = None # str
        #Table ID for the new ticket
        self.table_id = None # int
        #Subtledata Revenue Center ID
        self.revenue_center_id = None # int
        #Associated Device ID for user
        self.device_id = None # int
        
