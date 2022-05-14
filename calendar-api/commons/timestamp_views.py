import sys
import traceback

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from commons.Date import Date
from commons.Time import Time
from commons.TimeStamp import TimeStamp


@api_view(['POST'])
def to_string(request):
    data = request.data
    print(data)
    try:
        day, month, year = int(str(data['day']).strip()), int(str(data['month']).strip()), int(str(data['year']).strip())
        hour, minute = int(str(data['hour'])), int(str(data['minute']))
        date = Date(day, month, year)
        time = Time(hour, minute)
        timestamp = TimeStamp(date, time)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'timestamp': f'{timestamp}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def compare(request):
    data = request.data
    print(data)
    try:
        day1, month1, year1 = int(str(data['day1']).strip()), int(str(data['month1']).strip()), int(str(data['year1']).strip())
        day2, month2, year2 = int(str(data['day2']).strip()), int(str(data['month2']).strip()), int(str(data['year2']).strip())
        hour1, minute1 = int(str(data['hour1'])), int(str(data['minute1']))
        hour2, minute2 = int(str(data['hour2'])), int(str(data['minute2']))
        date1 = Date(day1, month1, year1)
        date2 = Date(day2, month2, year2)
        time1 = Time(hour1, minute1)
        time2 = Time(hour2, minute2)

        timestamp1 = TimeStamp(date1, time1)
        timestamp2 = TimeStamp(date2, time2)
    except KeyError:
        return Response({'error': 'Bad request, some required fields are missing.'}, status=status.HTTP_400_BAD_REQUEST)
    except (AttributeError, ValueError):
        return Response({'error': 'Invalid values provided'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        traceback.print_exception(*sys.exc_info())
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    answer = 0 if timestamp1 == timestamp2 else -1 if timestamp1 < timestamp2 else 1
    return Response({'answer': f'{answer}'}, status=status.HTTP_200_OK)

