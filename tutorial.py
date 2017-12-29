import signal
import time
from math import sqrt

class Killer:
  exit_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit)
    signal.signal(signal.SIGTERM, self.exit)

  def exit(self,signum, frame):
    self.exit_now = True

killer = Killer()
n = int(input())
worker = 0.0
for i in range(0,n):
  worker += sqrt(i)
  if killer.exit_now:
    break

print(int(worker / n))