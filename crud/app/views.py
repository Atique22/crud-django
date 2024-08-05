from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from bson.objectid import ObjectId
from .models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def list_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        item = serializer.save()
        return Response(ItemSerializer(item).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_item(request, pk):
    try:
        # Check if pk is a valid ObjectId
        if ObjectId.is_valid(pk):
            item = Item.objects.get(pk=ObjectId(pk))
        else:
            item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    except Item.DoesNotExist:
        return Response({"error": "Item not found"}, status=404)

@api_view(['PUT'])
def update_item(request, pk):
    try:
        # Check if pk is a valid ObjectId
        if ObjectId.is_valid(pk):
            item = Item.objects.get(pk=ObjectId(pk))
        else:
            item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response({"error": "Item not found"}, status=404)
    serializer = ItemSerializer(item ,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        # Check if pk is a valid ObjectId
        if ObjectId.is_valid(pk):
            item = Item.objects.get(pk=ObjectId(pk))
        else:
            item = Item.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Item.DoesNotExist:
        return Response({"error": "Item not found"}, status=404)
