class Activity:
    """Represents a single activity with time slot and priority."""

    _next_id: int = 1
    id: int
    title: str
    start_hour: float
    finish_hour: float
    priority: int
    
    def __init__(self, title: str, start_hour: float, finish_hour: float , priority: int) -> None:
        """Initialize an activity with auto-incremented ID."""

        self.id = Activity._next_id
        Activity._next_id += 1
        self.title = title
        self.start_hour = start_hour
        self.finish_hour = finish_hour
        self.priority = priority