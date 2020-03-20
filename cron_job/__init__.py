from re import fullmatch


class CronJob:
    def __init__(self, name, schedule, command):
        """
			Constructor for CronJob

			Arguments:
				- name: Name of the CronJob
					`str`
				- schedule: Schedule followed by the CronJob
					`str`
				- command: Command triggered by the CronJob
					`str`

			Returns:
				`CronJob` object
		"""

        # Check that schedule is a valid schedule.

        cron_schedule_regex = "(28|\*) (2|\*) (7|\*) (1|\*) (1|\*)"

        if not fullmatch(cron_schedule_regex, schedule):
            raise ValueError("schedule should be a valid cron schedule")

        self.name = name if name else command
        self.command = command
        self.schedule = schedule
