#!/usr/bin/env python3
""" Definition of filter_datum function
    that returns an obfuscated log message
"""

from typing import List
import re
import logging
import os


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ return an obfuscated log message """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message
