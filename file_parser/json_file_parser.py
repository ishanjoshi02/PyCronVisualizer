from PyCronVisualizer.file_parser import FileParser
from PyCronVisualizer.cron_job import CronJob
import json


class JsonFileParser(FileParser):
    """docstring for JsonFileParser"""

    def __init__(self):
        super(JsonFileParser, self).__init__()

    def parse(self):
        """
			Initializes the CronTab dictionary.

			Returns:
				- CronTab dictionary
		"""
        try:
            data = json.load(self.file)

            cron_jobs = [CronJob(**i) for i in data]

        except Exception as e:
            raise e
