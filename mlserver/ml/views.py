# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
import os
import sys
import time
import logging
import traceback

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


sys.path.append('../')

logging.basicConfig(
    format='%(asctime)s %(filename)15s %(funcName)20s %(levelname)s:%(message)s',
    level=logging.INFO)

from .models import *


from ai.NR.Retriever import Retriever
import utils.configurationProvider as cp

@api_view(['POST'])
def service(request):
    try:
        params = request.data
        text = params.get('text', None)
        country = params.get('country', None).lower()
        language = params.get('language', None).lower()
        return Response({'text': 'something'})

    except Exception:
        traceback.print_exc()
        ex_type, ex_value, ex_traceback = sys.exc_info()
        return Response(
            InternalErrorResponse(error_reason=str(ex_type.__name__),
                                  error_description=str(ex_value)).to_dict(),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )



