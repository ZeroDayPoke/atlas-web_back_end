#!/usr/bin/env python3
"""Logger"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    regex_pattern = '|'.join([f'(?<={field}=)[^{separator}]+'
                              for field in fields])
    return re.sub(regex_pattern, redaction, message)
