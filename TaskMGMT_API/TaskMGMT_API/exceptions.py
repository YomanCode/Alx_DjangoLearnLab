from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            response.data = {
                'error': 'Bad request. Please check your input and try again.'
            }
        elif response.status_code == status.HTTP_401_UNAUTHORIZED:
            response.data = {
                'error': 'Authentication credentials were not provided or are invalid.'
            }
        elif response.status_code == status.HTTP_403_FORBIDDEN:
            response.data = {
                'error': 'You do not have permission to perform this action.'
            }
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            response.data = {
                'error': 'The requested resource was not found.'
            }
        elif response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
            response.data = {
                'error': 'An internal server error occurred. Please try again later.'
            }

    return response