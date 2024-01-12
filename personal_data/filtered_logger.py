#!/usr/bin/env python3
"""Logger"""
import re

def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated"""
    regex_pattern = '|'.join([f'(?<={field}=)[^;]+' for field in fields])
    return re.sub(regex_pattern, redaction, message)
