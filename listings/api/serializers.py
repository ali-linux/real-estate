from rest_framework import serializers

from listings.models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'realtor',
            'title',
            'address',
            'city',
            'state',
            'zipcode',
            'discription',
            'price',
            'bedrooms',
            'bathrom',
            'garage',
            'sqft',
            'lot_size',
            'main_image',
            'image_1',
            'image_2',
            'image_3',
            'image_4',
            'image_5',
            'image_6',
            'is_published',
        ]

    def validate(self,data):
        discription = data.get('discription',None)
        if discription == "":
            discription = None
        main_image = data.get('main_image',None)
        if discription is None and main_image is None:
            raise serializers.ValidationError('content or image is required')
        return data 