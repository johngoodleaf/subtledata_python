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
class NewPayment:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'tip_amount': 'float',
            'tip_type': 'int',
            'testing': 'bool',
            'card_cvv': 'str',
            'card_id': 'int',
            'amount_before_tip': 'float',
            'user_id': 'int'

        }


        #
        self.tip_amount = None # float
        #
        self.tip_type = None # int
        #
        self.testing = None # bool
        #
        self.card_cvv = None # str
        #
        self.card_id = None # int
        #
        self.amount_before_tip = None # float
        #
        self.user_id = None # int
        
