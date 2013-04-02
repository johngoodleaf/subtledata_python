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
class DeleteUserStatus:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'user_id': 'int',
            'success': 'bool',
            'card_id': 'str',
            'result': 'str',
            'error': 'str',
            'device_id': 'int'

        }


        #SubtleData User ID
        self.user_id = None # int
        #Call was successful
        self.success = None # bool
        #New Card ID
        self.card_id = None # str
        #Result Status
        self.result = None # str
        #Error
        self.error = None # str
        #SubtleData Device ID
        self.device_id = None # int
        
