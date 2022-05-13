import sys
import traceback

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from commons.Time import Time


@api_view(['POST'])
def to_string(request):
    data = request.data
    print(data)
    try:
        h, m = int(str(data['h']).strip()), int(str(data['m']).strip())
        time = Time(h, m)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'time': f'{time}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def compare(request):
    data = request.data
    print(data)
    try:
        h1, m1 = int(str(data['h1']).strip()), int(str(data['m1']).strip())
        h2, m2 = int(str(data['h2']).strip()), int(str(data['m2']).strip())
        time1 = Time(h1, m1)
        time2 = Time(h2, m2)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    answer = 0 if time1 == time2 else -1 if time1 < time2 else 1
    return Response({'answer': f'{answer}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_minutes(request):
    data = request.data
    print(data)
    try:
        h, m = int(str(data['h']).strip()), int(str(data['m']).strip())
        minutes = int(str(data['minutes']).strip())
        time = Time(h, m)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'answer': f'{time + minutes}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def diff(request):
    data = request.data
    print(data)
    try:
        h1, m1 = int(str(data['h1']).strip()), int(str(data['m1']).strip())
        time = Time(h1, m1)
        if 'minutes' in data:
            other = int(str(data['minutes']).strip())
        else:
            h2, m2 = int(str(data['h2']).strip()), int(str(data['m2']).strip())
            other = Time(h2, m2)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'},
                        status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'answer': f'{time - other}'}, status=status.HTTP_200_OK)
