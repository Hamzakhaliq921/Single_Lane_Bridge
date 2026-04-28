import threading
import time
import random
from bridge_controller import BridgeController
from farmer import farmer_thread

def main():
    north_count = 4
    south_count = 4
    starvation_limit = 3

    controller = BridgeController(starvation_limit)
    threads = []
    farmer_id = 1

    for _ in range(north_count):
        t = threading.Thread(target=farmer_thread, args=(farmer_id, True, controller))
        threads.append(t)
        t.start()
        farmer_id += 1
        time.sleep(random.uniform(0.5, 1.5))

    for _ in range(south_count):
        t = threading.Thread(target=farmer_thread, args=(farmer_id, False, controller))
        threads.append(t)
        t.start()
        farmer_id += 1
        time.sleep(random.uniform(0.5, 1.5))

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()

