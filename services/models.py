from django.db import models
from PocketService.abstract_models import TimeStampModel
from users import models as user_models


# Create your models here.
class ClientRequest(TimeStampModel):
    date = models.DateField(blank=False)
    start_time = models.DateTimeField(blank=False)

    # Belongs to Client
    client = models.ForeignKey(user_models.Client, on_delete=models.CASCADE)


class ServiceJob(TimeStampModel):
    requested_start = models.DateTimeField(blank=False)
    actual_start = models.DateTimeField(blank=True)
    actual_end = models.DateTimeField(blank=True)

    # Belongs to ClientRequest
    client_request = models.ForeignKey(ClientRequest, on_delete=models.CASCADE)
    # Belongs to ServiceWorker
    service_worker = models.ForeignKey(user_models.ServiceWorker, on_delete=models.CASCADE)


class WorkerCompleteRating(TimeStampModel):

    # Has and belongs to ServiceWorker
    service_worker = models.OneToOneField(user_models.ServiceWorker, on_delete=models.CASCADE)


class ServiceRating(TimeStampModel):
    overall_rating = models.DecimalField(max_digits=2, decimal_places=1)
    quality_rating = models.DecimalField(max_digits=2, decimal_places=1)
    cost_rating = models.DecimalField(max_digits=2, decimal_places=1)
    personality_rating = models.DecimalField(max_digits=2, decimal_places=1)

    # Belongs to ServiceWorker
    service_worker = models.ForeignKey(user_models.ServiceWorker, on_delete=models.CASCADE)
    # Has and Belongs to ServiceJob
    service_job = models.OneToOneField(ServiceJob, on_delete=models.CASCADE, primary_key=True)
    # Belongs to WorkerCompleteRating
    worker_complete_rating = models.ForeignKey(WorkerCompleteRating, on_delete=models.CASCADE)