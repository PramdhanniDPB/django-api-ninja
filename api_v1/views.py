from django.shortcuts import render
# Create your views here.
from ninja import NinjaAPI
from api_v1.routes.retrieve_data import router

api = NinjaAPI(title="Retrieve Test API", version=2)

api.add_router('/test-endpoint', router)

