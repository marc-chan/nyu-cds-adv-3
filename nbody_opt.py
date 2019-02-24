"""
    N-body simulation.
    Optimizations:
        1. All optimizations from nbody 1-4
        2. Run using cython
        
    Results of nbody_opt vs nbody, average of 3 runs:
        Pre-optimized runtime: 84.12s
        Post-optimized runtime: 11.15s
        Relative speedup: 7.55x
"""

def nbody(loops, reference, iterations):
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''
    import pyximport; pyximport.install(language_level=3)
    from nbody_opt_mods import nbody as nbody_cython
    nbody_cython(100, 'sun', 20000)

if __name__ == '__main__':
    nbody(100, 'sun', 20000)
