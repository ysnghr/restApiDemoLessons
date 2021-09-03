from rest_framework import serializers
from haberler.models import Makale, Gazeteci
from datetime import datetime
from django.utils.timesince import timesince
from datetime import date


class MakaleSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()

    class Meta:
        model = Makale
        fields = '__all__'
        read_only_fields = ["id", "yaratilma_tarihi", "guncellenme_tarihi"]
    
    def get_time_since_pub(self, object):
        now = datetime.now()
        pub_date = object.yayinlama_tarihi
        if object.aktif == True:
            time_delta = timesince(pub_date, now)
            return time_delta
        else:
            return 'Aktif Degil!'
    
    def validate_yayimlanma_tarihi(self, tarihdegeri):
        today = date.today()
        if tarihdegeri > today:
            raise serializers.ValidationError("Yayimlanma tarihi ileri bir tarih olamaz!")
        return tarihdegeri



class GazeteciSerializer(serializers.ModelSerializer):

    #makaleler = MakaleSerializer(many=True, read_only=True)

    makaleler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='makale-detay'
    )

    class Meta:
        model = Gazeteci
        fields = '__all__'







### Default Serializer ###
class MakaleDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    metin = serializers.CharField()
    sehir = serializers.CharField()
    yayinlama_tarihi = serializers.DateField()
    aktif = serializers.BooleanField()
    yaratilma_tarihi = serializers.DateTimeField(read_only=True)
    guncellenme_tarihi = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Makale.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.yazar = validated_data.get('yazar', instance.yazar)
        instance.baslik = validated_data.get('baslik', instance.yazar)
        instance.aciklama = validated_data.get('aciklama', instance.yazar)
        instance.metin = validated_data.get('metin', instance.yazar)
        instance.sehir = validated_data.get('sehir', instance.yazar)
        instance.yayinlama_tarihi = validated_data.get('yayinlama_tarihi', instance.yazar)
        instance.aktif = validated_data.get('aktif', instance.yazar)
        instance.save()
        return instance
    
    def validate(self, data):
        if data['baslik'] == data['aciklama']:
            raise serializers.ValidationError('Başlık ve açıklama kısımları aynı olamaz.')
        return data
    
    def validate_baslik(self, value):
        if len(value) < 20:
            raise serializers.ValidationError('Başlık alanının karakter sayısı en az 20 karakter olmalı!')
        return data
