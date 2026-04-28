import threading
import time
import random

def farmer_thread(farmer_id, is_north, controller):
    direction = "NORTH" if is_north else "SOUTH"
    print(f"[Farmer {farmer_id}] Appeared ({direction})")

    if is_north:
        controller.enter_north(farmer_id)
        print(f"[Farmer {farmer_id}] Crossing bridge (NORTH)...")
        time.sleep(random.randint(2, 5))
        controller.exit_north(farmer_id)
    else:
        controller.enter_south(farmer_id)
        print(f"[Farmer {farmer_id}] Crossing bridge (SOUTH)...")
        time.sleep(random.randint(2, 5))
        controller.exit_south(farmer_id)

    print(f"[Farmer {farmer_id}] Finished crossing.")

