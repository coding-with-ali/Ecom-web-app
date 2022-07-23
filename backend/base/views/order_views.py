from django.shortcuts import render

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response

from base.serializer import ProductSerializer
from base.products import products
from base.models import Product

from rest_framework import status
