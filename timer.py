from timeit import timeit
import os

if __name__ == "__main__":
    reps = 3
    optimized = "nbody_2"

    setup = "from nbody import nbody"
    pretime = timeit("nbody(100, 'sun', 20000)", setup=setup, number=reps)/reps

    setup = "from {} import nbody".format(optimized)
    posttime = timeit("nbody(100, 'sun', 20000)", setup=setup, number=reps)/reps

    print("Results of {} vs nbody, average of {} runs:".format(optimized, reps))
    print("Pre-optimized runtime: {:.2f}s".format(pretime))
    print("Post-optimized runtime: {:.2f}s".format(posttime))
    print("Relative speedup: {:.2f}x".format(pretime/posttime))

    with open("{}_results.txt".format(optimized),"w") as f:
        f.write("Results of {} vs nbody, average of {} runs:".format(optimized, reps))
        f.write("\n")
        f.write("Pre-optimized runtime: {:.2f}s".format(pretime))
        f.write("\n")
        f.write("Post-optimized runtime: {:.2f}s".format(posttime))
        f.write("\n")
        f.write("Relative speedup: {:.2f}x".format(pretime/posttime))
