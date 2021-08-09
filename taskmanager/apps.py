from django.apps import AppConfig
from django.conf import settings
from taskmanager.db.connector import Load_start_up as Load


class TaskmanagerConfig(AppConfig):
    name = "taskmanager"
    verbose_name = "Taskmanager"

    def ready(self):
    	path = str(settings.BASE_DIR) + "/sqlite_startup_com.sql"
    	Load(path)