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
class Payment:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'payment_id': 'int',
            'card_type': 'str',
            'tip_amount': 'float',
            'total_amount': 'float',
            'expiration_year': 'str',
            'card_nickname': 'str',
            'name_on_tender': 'str',
            'expiration_month': 'str',
            'amount_before_tip': 'float',
            'credit_card_id': 'int',
            'last_4_digits': 'str'

        }


        #SubtleData Payment ID
        self.payment_id = None # int
        #Credit Card Type
        self.card_type = None # str
        #Payment tip amount
        self.tip_amount = None # float
        #Payment Total Amount
        self.total_amount = None # float
        #Card Expiration Year
        self.expiration_year = None # str
        #Credit Card Nickname
        self.card_nickname = None # str
        #Name on the tender
        self.name_on_tender = None # str
        #Card Expiration Month
        self.expiration_month = None # str
        #Payment amount before tip
        self.amount_before_tip = None # float
        #SubtleData Credit Card ID
        self.credit_card_id = None # int
        #Last 4 card digits
        self.last_4_digits = None # str
        
