#!/usr/bin/env python3
"""Basic authentication module for the API.
"""
import re
import base64
from typing import Tuple


class BasicAuth(Auth):
    """ basic auth Class
    """

