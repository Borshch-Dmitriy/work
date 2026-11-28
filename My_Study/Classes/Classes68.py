import time

class AdvancedTimer:
    def __init__(self):
        self.last_run = None
        self.runs = []
        self.min = None
        self.max = None
        self.start_time = None

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        res_time = time.perf_counter() - self.start_time
        self.last_run = res_time
        self.runs.append(res_time)

        if self.min is None or res_time < self.min:
            self.min = res_time

        if self.max is None or res_time > self.max:
            self.max = res_time

        return False
