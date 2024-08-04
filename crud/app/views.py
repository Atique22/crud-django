from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from bson.objectid import ObjectId
from .mongodb import get_collection
from .serializers import ItemSerializer

collection = get_collection('crud')

@api_view(['GET'])
def list_items(request):
    items = list(collection.find())
    for item in items:
        item['_id'] = str(item['_id'])
    return Response(items)

@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        item = serializer.validated_data
        result = collection.insert_one(item)
        item['_id'] = str(result.inserted_id)
        return Response(item, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_item(request, pk):
    item = collection.find_one({'_id': ObjectId(pk)})
    if item:
        item['_id'] = str(item['_id'])
        return Response(item)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_item(request, pk):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        item = serializer.validated_data
        result = collection.update_one({'_id': ObjectId(pk)}, {'$set': item})
        if result.matched_count:
            item['_id'] = pk
            return Response(item)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_item(request, pk):
    result = collection.delete_one({'_id': ObjectId(pk)})
    if result.deleted_count:
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
