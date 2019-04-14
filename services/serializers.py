from rest_framework.serializers import ModelSerializer
from .models import *


class ClientRequestSerializer(ModelSerializer):
    class Meta:
        model = ClientRequest
        fields = ('date', 'start_time', 'client_id')


class ServiceJobSerializer(ModelSerializer):
    class Meta:
        model = ServiceJob
        fields = ('requested_start', 'actual_start', 'actual_end', 'client_request_id', 'service_worker_id')


class WorkerCompleteRatingSerializer(ModelSerializer):
    class Meta:
        model = WorkerCompleteRating
        fields = 'service_worker_id'


class ServiceRating(ModelSerializer):
    class Meta:
        models = ServiceRating
        fields = ('overall_rating', 'quality_rating', 'cost_rating', 'personality_rating', 'service_worker_id',
                  'service_job_id', 'worker_complete_rating_id')
