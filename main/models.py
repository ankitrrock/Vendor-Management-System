from django.db import models
from django.db.models import Avg, Count, Sum

class VendorManager(models.Manager):
    def with_high_delivery_rate(self, threshold):
        return self.filter(on_time_delivery_rate__gte=threshold)

    def top_rated(self, min_quality_rating):
        return self.filter(quality_rating_avg__gte=min_quality_rating)

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    objects = VendorManager()

    def __str__(self):
        return self.name

class PurchaseOrderManager(models.Manager):
    def completed_orders(self):
        return self.filter(status='completed')

    def average_quality_rating(self, vendor):
        return self.filter(vendor=vendor).aggregate(Avg('quality_rating'))['quality_rating__avg']

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, related_name='purchase_orders', on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')])
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    objects = PurchaseOrderManager()

    def __str__(self):
        return self.po_number

class HistoricalPerformanceManager(models.Manager):
    def for_vendor(self, vendor):
        return self.filter(vendor=vendor)

    def average_metrics(self, vendor):
        return self.filter(vendor=vendor).aggregate(
            Avg('on_time_delivery_rate'),
            Avg('quality_rating_avg'),
            Avg('average_response_time'),
            Avg('fulfillment_rate')
        )

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='performance_metrics', on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    objects = HistoricalPerformanceManager()

    def __str__(self):
        return f'{self.vendor.name} - {self.date.strftime("%Y-%m-%d")}'
