from rest_framework import serializers


class PieChartSerializer(serializers.Serializer):
    model = serializers.CharField()
    value = serializers.FloatField()
