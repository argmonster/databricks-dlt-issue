import dlt
from utils.foo import bar

@dlt.table
def support_example():
    return spark.read.table("engineering_tim.bronze.eligibility_standard")

