from django.db import models


class Timestampable(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Syncable(models.Model):
    NOT_SYNCED = 1
    SYNCING = 2
    SYNCED = 3
    ERROR_SYNCING = 4

    SYNC_CHOICES = (
        (NOT_SYNCED, 'Not Synced'),
        (SYNCING, 'Syncing'),
        (SYNCED, 'Synced'),
        (ERROR_SYNCING, 'Error Syncing'),
    )

    SYNC_CODES = {
        NOT_SYNCED: 'not_synced',
        SYNCING: 'syncing',
        SYNCED: 'synced',
        ERROR_SYNCING: 'error',
    }

    sync_status = models.IntegerField(choices=SYNC_CHOICES, default=NOT_SYNCED)

    @property
    def is_syncing(self):
        return self.sync_status == self.SYNCING

    class Meta:
        abstract = True
