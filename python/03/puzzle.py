import sys
import time
from typing import Optional

class PuzzleContext:
    data: str
    def __init__(self, year: int, day: int):
        self._year = year
        self._day = day
        self.data = None
        self._start_times = [None, None]
        self._end_times = [None, None]

    def __enter__(self):
        self.data = self._get_data()
        self._start_times[0] = time.time()
        return self

    def __exit__(self, type, value, traceback):
        duration = sum(t2-t1 for t1, t2 in zip(self._start_times, self._end_times) if t1 and t2)
        print(f"Total running time: {duration} sec")

    @property
    def groups(self):
        return self.data.split("\n\n")

    @property
    def lines(self):
        return self.data.split("\n")

    @property
    def nonempty_lines(self):
        return [l for l in self.lines if l]

    def _get_data(self):
        if self._is_running_on_sample():
            input_path = f"s{sys.argv[1]}.txt"
            with open(input_path, "r") as f:
                return f.read()
        else:
            from aocd import get_data
            return get_data(year=self._year, day=self._day)

    def submit(self, part: int, ans: Optional[str]):
        if part not in [1, 2]:
            raise ValueError(f"Part must be either 1 or 2, was {part}")
        if ans is None:
            print(f"Skipping submission for part {part}")
            return
        self._end_times[part-1] = time.time()
        self._log_answer(ans, part)
        if not self._is_running_on_sample():
            from aocd import submit
            submit(ans, part=["a", "b"][part-1], day=self._day, year=self._year)
        if part == 1:
            self._start_times[part] = time.time()
        
    def _is_running_on_sample(self):
        return len(sys.argv) > 1

    def _log_answer(self, ans: str, part: int):
        if self._start_times[part-1] is None:
            t_start = self._start_times[0]
        else:
            t_start = self._start_times[part-1]
        duration = self._end_times[part-1] - t_start
        
        print(f"Part {part}: {ans} ({duration} sec)")
