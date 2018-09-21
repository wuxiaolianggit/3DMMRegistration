from scipy.spatial import cKDTree
import numpy as np
import multiprocessing


def displacementMap(source_points, target_points, max_dist=1.25):
    tree = cKDTree(source_points)  # voglio i punti di source che hanno corrispondenza con i punti del target
    _, indices = tree.query(target_points, distance_upper_bound=max_dist, n_jobs=multiprocessing.cpu_count())
    # indices contiene tutti i punti che distano max_dist dal loro punto più vicino
    #indices_range = source_points.shape[0]
    ##displacement_indices = np.delete(np.arange(0, indices_range), indices)
    displacement_points = np.delete(target_points, indices, axis=0)
    return displacement_points