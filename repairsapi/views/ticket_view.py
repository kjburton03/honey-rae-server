"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from repairsapi.models import ServiceTicket


class ServiceTicketView(ViewSet):
    """Honey Rae API customers view"""

    def list(self, request):
        """Handle GET requests to get all customers

        Returns:
            Response -- JSON serialized list of customers
        """

        service_tickets = ServiceTicket.objects.all()
        serialized = ServiceTicketSerializer(service_tickets, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single customer

        Returns:
            Response -- JSON serialized customer record
        """

        service_tickets = ServiceTicket.objects.get(pk=pk)
        serialized = ServiceTicketSerializer(service_tickets, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class ServiceTicketSerializer(serializers.ModelSerializer):
    """JSON serializer for customers"""
    class Meta:
        model = ServiceTicket
        fields = ('id', 'user', 'address')





# """View module for handling requests for customer data"""
# # from django.http import HttpResponseServerError
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import serializers, status
# from repairsapi.models import ServiceTicket


# class ServiceTicketView(ViewSet):
#     """Honey Rae API customers view"""

#     def list(self, request):
#         """Handle GET requests to get all customers

#         Returns:
#             Response -- JSON serialized list of customers
#         """
#         service_tickets = []

#         if request.auth.user.is_staff:
#             service_tickets = ServiceTicket.objects.all()
#         else:
#             service_tickets = ServiceTicket.objects.filter(customer__user=request.auth.user)
        
#         serialized = ServiceTicketSerializer(service_tickets, many=True)
#         return Response(serialized.data, status=status.HTTP_200_OK)

#     def retrieve(self, request, pk=None):
#         """Handle GET requests for single customer

#         Returns:
#             Response -- JSON serialized customer record
#         """

#         ServiceTicket = ServiceTicket.objects.get(pk=pk)
#         serialized = ServiceTicketSerializer(ServiceTicket, context={'request': request})
#         return Response(serialized.data, status=status.HTTP_200_OK)

# class ServiceTicketSerializer(serializers.ModelSerializer):
#     """JSON serializer for servicetickets"""

#     class Meta:
#         model = ServiceTicket
#         fields = ('id', 'customer', 'employee', 'description', 'emergency', 'date_completed')
#         depth = 1
        