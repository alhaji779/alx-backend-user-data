#!/usr/bin/env python3
""" regex function to obfuscate mesages
"""
import re


def filter_datum(fields, redaction, message, separator):
    pattern = f"({'|'.join(fields)})=([^ {separator}]*)"
    return re.sub(pattern, f"\\1={redaction}", message)
