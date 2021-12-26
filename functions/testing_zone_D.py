import pandas as pd
from testing_zone_A import zone_A
from testing_zone_C import zone_C

for i in range(7):

    df = zone_A()
    df = zone_C()
    df = zone_A()

    print(df)