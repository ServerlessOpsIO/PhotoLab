'''Boilerplate function'''
import json
from dataclasses import dataclass

from aws_lambda_powertools.logging import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

from common.util.dataclasses import lambda_dataclass_response


LOGGER = Logger(utc=True)


@dataclass
class Response:
    '''Function response'''

    pass



@LOGGER.inject_lambda_context
@lambda_dataclass_response
def handler(event: Dict[str, Any], context: LambdaContext) -> Response:
    '''Function entry'''
    LOGGER.debug('Event', extra={"message_object": event})


    response = Response(**{})


    LOGGER.debug('Response', extra={"message_object": resp})
    return response

