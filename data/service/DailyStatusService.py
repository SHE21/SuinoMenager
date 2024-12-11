from data.connection.Connection import Connection


class DailyStatusService:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.connection.connect()
