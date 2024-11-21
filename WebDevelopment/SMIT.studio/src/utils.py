import datetime as dt


class UserEventsLog:
    kafka = 99

    def log(
        self,
        user_id: int | None, event_message: str, event_dt: dt.datetime,
    ):
        print(self.kafka)
