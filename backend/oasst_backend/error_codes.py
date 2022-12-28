# -*- coding: utf-8 -*-
from enum import IntEnum


class OasstErrorCode(IntEnum):
    """
    Error codes of the Open-Assistant backend API.

    Ranges:
         0-1000: general errors
      1000-2000: tasks endpoint
      2000-3000: prompt_repository
    """

    # 0-1000: general errors
    GENERIC_ERROR = 0
    DATABASE_URI_NOT_SET = 1
    API_CLIENT_NOT_AUTHORIZED = 2

    # 1000-2000: tasks endpoint
    TASK_INVALID_REQUEST_TYPE = 1000
    TASK_ACK_FAILED = 1001
    TASK_INVALID_RESPONSE_TYPE = 1002
    TASK_INTERACTION_REQUEST_FAILED = 1003
    TASK_GENERATION_FAILED = 1004

    # 2000-3000: prompt_repository
    INVALID_POST_ID = 2000
    POST_NOT_FOUND = 2001
    RATING_OUT_OF_RANGE = 2002
    INVALID_RANKING_VALUE = 2003
    WORK_PACKAGE_NOT_FOUND = 2004
    WORK_PACKAGE_EXPIRED = 2005
    WORK_PACKAGE_PAYLOAD_TYPE_MISMATCH = 2006
    INVALID_TASK_TYPE = 2007
    USER_NOT_SPECIFIED = 2008
