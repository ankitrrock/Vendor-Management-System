from rest_framework import serializers
from .models import Vendor, PurchaseOrder, HistoricalPerformance

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        extra_kwargs = {
            'name': {'help_text': 'The name of the vendor.'},
            'contact_details': {'help_text': 'Contact details for the vendor.'},
            'address': {'help_text': 'Address of the vendor.'},
            'vendor_code': {'help_text': 'Unique code for the vendor.'},
            'on_time_delivery_rate': {'help_text': 'Percentage of orders delivered on time.'},
            'quality_rating_avg': {'help_text': 'Average quality rating given to the vendor.'},
            'average_response_time': {'help_text': 'Average time taken by the vendor to respond.'},
            'fulfillment_rate': {'help_text': 'Percentage of orders fulfilled without issues.'}
        }

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        extra_kwargs = {
            'po_number': {'help_text': 'Unique purchase order number.'},
            'vendor': {'help_text': 'Reference to the vendor.'},
            'order_date': {'help_text': 'Date when the order was placed.'},
            'delivery_date': {'help_text': 'Date when the order is expected to be delivered.'},
            'items': {'help_text': 'List of items in the order.'},
            'quantity': {'help_text': 'Quantity of items ordered.'},
            'status': {'help_text': 'Current status of the order (e.g., pending, completed).'},
            'quality_rating': {'help_text': 'Quality rating of the order.'},
            'issue_date': {'help_text': 'Date when the order was issued.'},
            'acknowledgment_date': {'help_text': 'Date when the order was acknowledged.'}
        }

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'
