from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# The APIView is good enough for the purpose as I wanted to keep this exercise
# simple without querying the database or performing complex processing that
#  requires the use of viewsets.
class DataView(APIView):
    """
    This class returns the data dictionary as a JSON response using DRF
    """

    def get(self, request, *args, **kwargs):
        cars_sales_share = [
            {"model": "Volkswagen", "value": 19.1},
            {"model": "Mercedes-Benz", "value": 8.9},
            {"model": "BMW", "value": 8},
            {"model": "Audi", "value": 7.3},
            {"model": "Skoda", "value": 7.2},
            {"model": "SEAT", "value": 5.5},
            {"model": "Opel", "value": 5.3},
            {"model": "Ford", "value": 3.6},
            {"model": "Hyundai", "value": 3.5},
            {"model": "Toyota", "value": 3.2},
            {"model": "Dacia", "value": 2.5},
            {"model": "Kia", "value": 2.5},
            {"model": "Fiat", "value": 2.3},
            {"model": "Peugeot", "value": 2.3},
            {"model": "Volvo", "value": 2.2},
            {"model": "Citroen", "value": 2},
            {"model": "Renault", "value": 1.8},
            {"model": "Mazda", "value": 1.6},
            {"model": "Posche", "value": 1.4},
            {"model": "Tesla", "value": 1.3},
        ]  # Car sales data in Germany between January and September 2024, https://www.statista.com/statistics/1005575/leading-car-brands-market-share-new-registrations-germany/

        return Response(cars_sales_share, status=status.HTTP_200_OK)
