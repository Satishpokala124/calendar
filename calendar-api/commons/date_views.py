import sys
import traceback

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from commons.Date import Date


@api_view(['POST'])
def to_string(request):
    data = request.data
    print(data)
    try:
        d, m, y = int(str(data['d']).strip()), int(str(data['m']).strip()), int(str(data['y']).strip())
        date = Date(d, m, y)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'date': f'{date}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def compare(request):
    data = request.data
    print(data)
    try:
        d1, d2 = int(str(data['d1']).strip()), int(str(data['d2']).strip())
        m1, m2 = int(str(data['m1']).strip()), int(str(data['m2']).strip())
        y1, y2 = int(str(data['y1']).strip()), int(str(data['y2']).strip())
        date1 = Date(d1, m1, y1)
        date2 = Date(d2, m2, y2)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    answer = 0 if date1 == date2 else 1 if date1 < date2 else -1
    return Response({'answer': f'{answer}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_days(request):
    data = request.data
    print(data)
    try:
        d, m, y = int(str(data['d']).strip()), int(str(data['m']).strip()), int(str(data['y']).strip())
        days = int(str(data['days']).strip())
        date = Date(d, m, y)
        print(date, days)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'date': f'{date + days}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def diff(request):
    data = request.data
    print(data)
    try:
        d1, m1, y1 = int(str(data['d1']).strip()), int(str(data['m1']).strip()), int(str(data['y1']).strip())
        date1 = Date(d1, m1, y1)
        if 'days' in data:
            other = int(str(data['days']).strip())
        else:
            d2, m2, y2 = int(str(data['d2']).strip()), int(str(data['m2']).strip()), int(str(data['y2']).strip())
            other = Date(d2, m2, y2)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'answer': f'{date1 - other}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def is_leap_year(request):
    data = request.data
    print(data)
    try:
        y = int(str(data['y']).strip())
        date = Date(1,1, y)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'is_leap_year': f'{date.is_leap_year()}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def max_days_in_this_month(request):
    data = request.data
    print(data)
    try:
        m, y = int(str(data['m']).strip()), int(str(data['y']).strip())
        date = Date(1, m, y)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'max_days_in_this_month': f'{date.max_days_in_this_month()}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def next_month(request):
    data = request.data
    print(data)
    try:
        m, y = int(str(data['m']).strip()), int(str(data['y']).strip())
        date = Date(1, m, y)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'next_month': f'{date.next_month()}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def previous_month(request):
    data = request.data
    print(data)
    try:
        m, y = int(str(data['m']).strip()), int(str(data['y']).strip())
        date = Date(1, m, y)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'previous_month': f'{date.previous_month()}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def days_from_year_start(request):
    data = request.data
    print(data)
    try:
        d, m, y = int(str(data['d']).strip()), int(str(data['m']).strip()), int(str(data['y']).strip())
        date = Date(d, m, y)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'days_from_year_start': f'{date.days_from_year_start()}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def days_in_this_year(request):
    data = request.data
    print(data)
    try:
        y = int(str(data['y']).strip())
        date = Date(1, 1, y)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'days_in_this_year': f'{date.days_in_this_year()}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def days_remaining_in_this_year(request):
    data = request.data
    print(data)
    try:
        d, m, y = int(str(data['d']).strip()), int(str(data['m']).strip()), int(str(data['y']).strip())
        date = Date(d, m, y)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'days_remaining_in_this_year': f'{date.days_remaining_in_this_year()}'}, status=status.HTTP_200_OK)
