from PyCronVisualizer.cron_job import CronJob


class CronJobVisualizer:
    """
		This class is responsible for actually visualizing the Cron Jobs.
	"""

    def __init__(self, cron_jobs):
        """
			Initializes the CronJobVisualizer

			Arguments:
				- cronjobs: CronJob(s) which this visualizer is going to visualize.
					`list` of `CronJob`

		"""
        self.cron_jobs = cron_jobs

    def visualize(self):
        """
			Create the view of the CronJobs.

		"""
        pass
