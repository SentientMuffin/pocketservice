from django.db import models
from PocketService.abstract_models import TimeStampModel
from users import models as user_models


# Create your models here.
class ClientRequest(TimeStampModel):
    date = models.DateField(blank=False)
    start_time = models.DateTimeField(blank=False)

    client = models.ForeignKey(user_models.Client)


class ServiceJob(TimeStampModel):
    requested_start = models.DateTimeField(blank=False)
    actual_start = models.DateTimeField(blank=True)
    actual_end = models.DateTimeField(blank=True)

    client_request = models.ForeignKey(ClientRequest)
    service_worker = models.ForeignKey(user_models.ServiceWorker)


class WorkerCompleteRating(TimeStampModel):
    service_worker = models.OneToOneField(user_models.ServiceWorker)


class ServiceRating(TimeStampModel):
    overall_rating = models.DecimalField(max_digits=2, decimal_places=1)
    quality_rating = models.DecimalField(max_digits=2, decimal_places=1)
    cost_rating = models.DecimalField(max_digits=2, decimal_places=1)
    personality_rating = models.DecimalField(max_digits=2, decimal_places=1)

    service_worker = models.ForeignKey(user_models.ServiceWorker)
    service_job = models.OneToOneField(ServiceJob, on_delete=models.CASCADE, primary_key=True)
    worker_complete_rating = models.ForeignKey(WorkerCompleteRating)