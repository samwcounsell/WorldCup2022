from singlematch_engine import singlematch
from multimatch_engine import multimatch
import time

start_s = time.time()

# program body starts
for i in range(100):
    singlematch(0.014, 0.014)

end_s = time.time()

start_m = time.time()

for i in range(100):
    multimatch(0.014, 0.014)

end_m = time.time()

# total time taken
print(f"Runtime of the program is {end_s - start_s}")
print(f"Runtime of the program is {end_m - start_m}")