# -*- coding:utf-8 -*-
from django.db import models
from django.db.models import Model
from statuses.models import Status
from users.models import TaskUser


class Task(Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    executor = models.ForeignKey(
        TaskUser,
        on_delete=models.PROTECT,
        related_name="task_executor",
        null=True,
        blank=True,
    )
    creator = models.ForeignKey(
        TaskUser,
        on_delete=models.PROTECT,
        related_name='task_creator',
        null=True,
    )
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
