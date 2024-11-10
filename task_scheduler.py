import schedule
import time
from threading import Thread


class TaskScheduler:
    """Schedules and manage pdf scraping and exports tasks"""

    def __init__(self, scraping_manager):
        self.scraping_manager = scraping_manager

    def schedule_task(self, interval: int, unit: str):
        """Schedule scraping based on an interval"""

        if unit == 'seconds':
            schedule.every(interval).seconds.do(self.scraping_manager.run_all_scraping)
        elif unit == 'minutes':
            schedule.every(interval).minutes.do(self.scraping_manager.run_all_scraping)

        # run the scheduling loop in a separate thread
        Thread(target=self._run_scheduler).start()

    def _run_scheduler(self):
        """Run the scheduled tasks continuously"""

        while True:
            schedule.run_pending()
            time.sleep(1)
