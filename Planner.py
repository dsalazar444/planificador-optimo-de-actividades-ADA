from Activity import Activity

class Planner:
    """Solves the activity scheduling problem using backtracking to maximize priority."""

    activities: list[Activity]
    best_solution: list[Activity] # based in total priority
    best_priority: int
    
    def __init__(self, activities: list[Activity]) -> None:
        """Initialize planner with activities sorted by start time."""
        self.activities = Planner.order_by_start_hour(activities)
        self.best_solution = []
        self.best_priority = 0

    @staticmethod
    def order_by_start_hour(activities: list[Activity]) -> list[Activity]:
        """Sort activities by start hour in ascending order."""

        return sorted(activities, key=lambda x: x.start_hour)

    def backtracking(self, i: int = 0, current_total_priority: int = 0, temporal_solution: list[Activity] | None = None) -> None:
        """
        Recursively explore all possible activity combinations using backtracking.
        Finds the schedule with maximum total priority without time conflicts.
        """

        if temporal_solution is None:
            temporal_solution = []

        # base case. Means that we passed the last activity, so we return
        if i == len(self.activities):
            if current_total_priority > self.best_priority:
                self.best_solution = temporal_solution.copy()
                self.best_priority = current_total_priority
            
            return  
        
        # Decision 1: skip acctivity[i]
        self.backtracking(i+1, current_total_priority, temporal_solution)

        # Decision 2: add activity[i] if it does not violate the constraint
        activity= self.activities[i]
        if not temporal_solution or activity.start_hour >= temporal_solution[-1].finish_hour: # the next activity starts before the last one ends        
            temporal_solution.append(activity) 
            self.backtracking(i+1, current_total_priority + activity.priority, temporal_solution)
            temporal_solution.pop()
    
    def print_best_solution(self) -> None:
        """Display the optimal schedule with total priority and activity details."""

        total_activities = len(self.activities)
        selected_activities = len(self.best_solution)
        discarded_activities = total_activities - selected_activities
    
        print("\n" + "="*50)
        print("MEJOR SOLUCIÓN ENCONTRADA")
        print("="*50)
        print(f"\nEstadísticas:")
        print(f"  • Actividades totales: {total_activities}")
        print(f"  • Actividades seleccionadas: {selected_activities}")
        print(f"  • Actividades descartadas: {discarded_activities}")
        print(f"\nActividades seleccionadas:")
        
        for activity in self.best_solution:
            print(f"  ID: {activity.id}")
            print(f"    Título: {activity.title}")
            print(f"    Horario: {activity.start_hour} - {activity.finish_hour}")
            print(f"    Prioridad: {activity.priority}")
            print()
        
        print("="*50)