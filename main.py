from Planner import Planner
from Activity import Activity

def input_title() -> str:
    """Prompt user for activity title with validation."""

    while True:
        title = input("Título: ").strip()
        if title:
            return title
        print("El título no puede estar vacío.\n")

def input_hour(label: str) -> float:
   """
    Prompt user for time input with format validation.
    Accepts 24-hour format with decimals (e.g., 14.30 for 14:30).
    """
   
   while True:
        try:
            time_input = input(f"  Hora de {label} (ej: 9.30 para 9:30, 14.45 para 14:45): ")
            hour_value = float(time_input)
            
            if 0 <= hour_value <= 24:
                # Validar que los minutos (decimales) sean válidos
                parts = time_input.split('.')
                if len(parts) == 2:
                    minutes = int(parts[1])
                    if minutes > 59:
                        print("Los minutos deben estar entre 0 y 59.\n")
                        continue
                
                return hour_value
            else:
                print("La hora debe estar entre 0 y 24.\n")
        except ValueError:
            print("Formato inválido. Usa formato hora.minuto (ej: 14.30).\n")

def input_priority() -> int:
    """Prompt user for priority level (1=low, 2=medium, 3=high)."""

    while True:
        try:
            priority = int(input("  Prioridad (1=baja, 2=media, 3=alta): "))
            if priority in [1, 2, 3]:
                return priority
            print("La prioridad debe ser 1, 2 o 3.\n")
        except ValueError:
            print("Formato inválido. Usa un número entero.\n")

def main():
    """Main program flow: collect activities and compute optimal schedule."""

    print("\n" + "="*50)
    print("PLANIFICADOR ÓPTIMO DE ACTIVIDADES")
    print("="*50)
    print("\n📋 INSTRUCCIONES:")
    print("  • Horas en formato 24h con decimales (ej: 14.45 = 14:45)")
    print("  • Prioridad: 1=baja, 2=media, 3=alta")
    print("  • Escribe 'salir' en el título para terminar\n")
    
    activities: list[Activity] = []
    
    while True:
        title = input_title()
        if title.lower() == "salir":
            break
        
        start_hour = input_hour('inicio')
        finish_hour = input_hour('finalización')
        
        if start_hour >= finish_hour:
            print("La hora de inicio debe ser menor a la de fin.\n")
            continue
        
        priority = input_priority()
        
        activity = Activity(title, start_hour, finish_hour, priority)
        activities.append(activity)
        print("✓ Actividad agregada\n")
    
    if activities:
        planner = Planner(activities)
        planner.backtracking()
        planner.print_best_solution()
    else:
        print("No ingresaste actividades.")
    
    

if __name__ == "__main__":
    main()