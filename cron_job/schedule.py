from datetime import datetime, timedelta
from croniter import croniter

class Schedule:
    def __init__(self, schedule_str, start_date=datetime.now()):
        """
			Initializes a Schedule Object from a string

			- Arguments
				- schedule_str: Schedule's string representation
					`str`
                - start_date: start date to initialize the iter object
                    `datetime`
			-Returns
				Schedule Object
					`Schedule`

		"""
        self.iter = croniter(schedule_str, start_date)
