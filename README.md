# Vendor Management System
 Vendor Management System with Performance Metrics


                                Vendor Management System Documentation
                                        Project Overview
The Vendor Management System (VMS) is a comprehensive solution developed using Django and Django REST Framework. It is designed to manage vendor profiles, track purchase orders, and evaluate vendor performance metrics. This document outlines the core features, the technologies used, and the improvements made to enhance the user experience.

Core Features
1. Vendor Profile Management
    Objective: To create, update, and manage vendor profiles.
    Endpoints:
        POST /api/vendors/: Creates a new vendor.
        GET /api/vendors/: Lists all vendors.
        GET /api/vendors/{vendor_id}/: Retrieves a specific vendor's details.
        PUT /api/vendors/{vendor_id}/: Updates a vendor's details.
        DELETE /api/vendors/{vendor_id}/: Deletes a vendor.
2. Purchase Order Tracking
    Objective: To manage and track purchase orders related to vendors.
    Endpoints:
        POST /api/purchase_orders/: Creates a new purchase order.
        GET /api/purchase_orders/: Lists all purchase orders with an option to filter by vendor.
        GET /api/purchase_orders/{po_id}/: Retrieves details of a specific purchase order.
        PUT /api/purchase_orders/{po_id}/: Updates a purchase order.
        DELETE /api/purchase_orders/{po_id}/: Deletes a purchase order.
3. Vendor Performance Evaluation
    Objective: To evaluate and retrieve performance metrics of vendors.
    Metrics:
        On-Time Delivery Rate
        Quality Rating
        Response Time
        Fulfillment Rate
        Endpoint:
        GET /api/vendors/{vendor_id}/performance/: Retrieves a vendor's performance metrics.
Technologies Used
    Django: A high-level Python web framework used for developing the application's backend.
    Django REST Framework: A powerful toolkit for building Web APIs, used for creating RESTful API endpoints.
    Python: The programming language used for the development of the application.
    Database: PostgreSQL (or any other database supported by Django) for data storage.
    Improvements and Features
    User-Friendly API Responses:

APIs now include a template section in responses, providing field names, types, and descriptions for better clarity on what data is required or returned.

Detailed Error Messages:
    Error responses now include more context, helping users understand what went wrong and how to fix it.
    Performance Metrics:

Added functionality to retrieve and evaluate vendor performance metrics, including delivery rates, quality ratings, response times, and fulfillment rates.

How to Use
    Creating and Managing Vendors: Use the provided API endpoints to create, retrieve, update, and delete vendor profiles.
    Tracking Purchase Orders: Manage purchase orders with endpoints designed to handle creation, retrieval, updates, and deletions.
    Evaluating Performance: Retrieve detailed performance metrics to assess vendor effectiveness.
