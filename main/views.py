from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer

# Helper function to get serializer template
def get_serializer_template(serializer_class):
    serializer = serializer_class()
    fields = serializer.fields
    return {
        field_name: {
            'type': field.__class__.__name__,  
            'help_text': field.help_text or 'No description available'
        }
        for field_name, field in fields.items()
    }

# Vendor Views

@api_view(['POST'])
def create_vendor(request):
    serializer = VendorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Vendor created successfully.",
            "data": serializer.data,
            "template": get_serializer_template(VendorSerializer)
        }, status=status.HTTP_201_CREATED)
    return Response({
        "errors": serializer.errors,
        "template": get_serializer_template(VendorSerializer)
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_vendors(request):
    vendors = Vendor.objects.all()
    serializer = VendorSerializer(vendors, many=True)
    return Response({
        "data": serializer.data,
        "template": get_serializer_template(VendorSerializer)
    })

@api_view(['GET'])
def vendor_detail(request, vendor_id):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
        serializer = VendorSerializer(vendor)
        return Response({
            "data": serializer.data,
            "template": get_serializer_template(VendorSerializer)
        })
    except Vendor.DoesNotExist:
        return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_vendor(request, vendor_id):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
        serializer = VendorSerializer(vendor, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Vendor updated successfully.",
                "data": serializer.data
            })
        return Response({
            "errors": serializer.errors,
            "template": get_serializer_template(VendorSerializer)
        }, status=status.HTTP_400_BAD_REQUEST)
    except Vendor.DoesNotExist:
        return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_vendor(request, vendor_id):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
        vendor.delete()
        return Response({"message": "Vendor deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except Vendor.DoesNotExist:
        return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)

# Purchase Order Views

@api_view(['POST'])
def create_purchase_order(request):
    serializer = PurchaseOrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Purchase order created successfully.",
            "data": serializer.data,
            "template": get_serializer_template(PurchaseOrderSerializer)
        }, status=status.HTTP_201_CREATED)
    return Response({
        "errors": serializer.errors,
        "template": get_serializer_template(PurchaseOrderSerializer)
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_purchase_orders(request):
    purchase_orders = PurchaseOrder.objects.all()
    vendor_id = request.query_params.get('vendor_id')
    if vendor_id:
        purchase_orders = purchase_orders.filter(vendor_id=vendor_id)
    serializer = PurchaseOrderSerializer(purchase_orders, many=True)
    return Response({
        "data": serializer.data,
        "template": get_serializer_template(PurchaseOrderSerializer)
    })

@api_view(['GET'])
def purchase_order_detail(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(id=po_id)
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response({
            "data": serializer.data,
            "template": get_serializer_template(PurchaseOrderSerializer)
        })
    except PurchaseOrder.DoesNotExist:
        return Response({"error": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_purchase_order(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(id=po_id)
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Purchase order updated successfully.",
                "data": serializer.data
            })
        return Response({
            "errors": serializer.errors,
            "template": get_serializer_template(PurchaseOrderSerializer)
        }, status=status.HTTP_400_BAD_REQUEST)
    except PurchaseOrder.DoesNotExist:
        return Response({"error": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_purchase_order(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(id=po_id)
        purchase_order.delete()
        return Response({"message": "Purchase order deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except PurchaseOrder.DoesNotExist:
        return Response({"error": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)

# Performance Metrics View

@api_view(['GET'])
def vendor_performance(request, vendor_id):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
        performance = HistoricalPerformance.objects.for_vendor(vendor)
        serializer = HistoricalPerformanceSerializer(performance, many=True)
        return Response({
            "data": serializer.data,
            "template": get_serializer_template(HistoricalPerformanceSerializer)
        })
    except Vendor.DoesNotExist:
        return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
