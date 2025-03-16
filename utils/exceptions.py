from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound, PermissionDenied

from exercises.models import Exercise

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PermissionDenied as e:
            return Response({ 'detail': str(e) }, status.HTTP_403_FORBIDDEN)
        except (Exercise.DoesNotExist, NotFound) as e:
            print(e)
            return Response({ 'detail': str(e) }, status.HTTP_404_NOT_FOUND)
        except ValidationError as e: # If the data is not valid, this is the error
            print(e)
            return Response(e.detail, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print('Error name:', e.__class__.__name__)
            return Response({ 'detail': 'An unknown error occurred' }, status.HTTP_500_INTERNAL_SERVER_ERROR)
    return wrapper