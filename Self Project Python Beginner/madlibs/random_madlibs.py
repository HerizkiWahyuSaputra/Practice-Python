from sample_madlibs import Aboutfuture, Aboutindustry, AboutTech
import random 

if __name__ == "__main__":
    n = random.choice ([Aboutfuture, Aboutindustry, AboutTech])
    n.madlib()