import threading

class BridgeController:
    def __init__(self, starvation_limit):
        self.north_sem = threading.Semaphore(1)
        self.south_sem = threading.Semaphore(1)
        self.lock = threading.Lock()

        self.direction = None
        self.on_bridge = 0
        self.north_cycle = 0
        self.south_cycle = 0
        self.starvation_limit = starvation_limit

    def enter_north(self, farmer_id):
        self.north_sem.acquire()
        with self.lock:
            if self.on_bridge == 0:
                self.south_sem.acquire()
                self.direction = "NORTH"

            self.on_bridge += 1
            self.north_cycle += 1

            if self.north_cycle < self.starvation_limit:
                self.north_sem.release()
            else:
                self.north_cycle = 0

            print(f"[Farmer {farmer_id}] Entering bridge (NORTH)")

    def exit_north(self, farmer_id):
        with self.lock:
            self.on_bridge -= 1
            print(f"[Farmer {farmer_id}] Exiting bridge (NORTH)")
            if self.on_bridge == 0:
                self.direction = None
                self.south_cycle = 0
                self.south_sem.release()

    def enter_south(self, farmer_id):
        self.south_sem.acquire()
        with self.lock:
            if self.on_bridge == 0:
                self.north_sem.acquire()
                self.direction = "SOUTH"

            self.on_bridge += 1
            self.south_cycle += 1

            if self.south_cycle < self.starvation_limit:
                self.south_sem.release()
            else:
                self.south_cycle = 0

            print(f"[Farmer {farmer_id}] Entering bridge (SOUTH)")

    def exit_south(self, farmer_id):
        with self.lock:
            self.on_bridge -= 1
            print(f"[Farmer {farmer_id}] Exiting bridge (SOUTH)")
            if self.on_bridge == 0:
                self.direction = None
                self.north_cycle = 0
                self.north_sem.release()

