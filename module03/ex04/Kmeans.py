import sys
from csvreader import CsvReader
import numpy as np
import os
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d


def calc_dist(a: np.ndarray, b: np.ndarray) -> float:
    """ I use the first index for storing the closest centroid"""
    return abs(a[3] - b[3]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = np.ndarray  # values of the centroids

    def __get_closest_centroid(self, x: np.ndarray, get_index: bool = False) -> np.ndarray | int:
        centroids_dists = [calc_dist(x, centroid) for centroid in self.centroids]
        min_index = centroids_dists.index(min(centroids_dists))
        if get_index:
            return min_index
        return self.centroids[min_index][1:]

    def __assignment_step(self, X: np.ndarray) -> bool:
        """
        :param X: np.ndarray:
        :return True if assignments changed, False otherwise:
        """
        changes = False
        for i, x in enumerate(X):
            centroids_dists = [calc_dist(x, centroid) for centroid in self.centroids]
            min_index = centroids_dists.index(min(centroids_dists))
            if min_index != x[0]:
                changes = True
            x[0] = min_index
        return changes

    def __get_avgs(self, X: np.ndarray, i: int) -> list:
        count = 0
        values = np.array([0., 0., 0., 0.], dtype=float)
        for x in X:
            if x[0] == i:
                count += 1
                values += x
        return values / count

    def __update_step(self, X: np.ndarray):
        for i, centroid in enumerate(self.centroids):
            avgs = self.__get_avgs(X, i)
            self.centroids[i] = avgs

    def display_centroids(self, X: np.ndarray) -> None:
        counts = [0 for _ in range(self.ncentroid)]
        for x in X:
            counts[self.__get_closest_centroid(x, get_index=True)] += 1
        areas_nb = {i: '' for i in range(4)}
        if len(self.centroids) == 4:
            centroids: np.ndarray = self.centroids.copy()
            the_belt_idx = int(centroids[centroids[:, 1].argmax()][0])
            centroids = np.delete(centroids, the_belt_idx, axis=0)
            areas_nb[the_belt_idx] = 'The Belt'
            for venus, earth, mars in [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]:
                if centroids[venus][2] < centroids[earth][2] and centroids[mars][1] > centroids[earth][1]:
                    areas_nb[int(centroids[venus][0])] = 'Venus'
                    areas_nb[int(centroids[earth][0])] = 'Earth'
                    areas_nb[int(centroids[mars][0])] = 'Mars'
                    break

        for i, centroid in enumerate(self.centroids):
            print(f'centroid #{i} is located at {centroid[1:]} with {counts[i]} individuals associated to it.', end='')
            if len(self.centroids) == 4:
                print(' ' + areas_nb[i])

    def get_citizens(self, X: np.ndarray) -> list[np.ndarray]:
        lst = [np.array([[]], dtype=float) for _ in range(self.ncentroid)]
        for x in X:
            n = int(x[0])
            lst[n] = np.append(lst[n], [x])
        lst = [a.reshape(-1, 4) for a in lst]
        return lst

    def fit(self, X: np.ndarray) -> None:
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        rng = np.random.default_rng()
        self.centroids = rng.choice(X, size=self.ncentroid, replace=False, axis=0)
        for _ in range(self.max_iter):
            if not self.__assignment_step(X):
                break
            self.__update_step(X)

    def predict(self, X):
        """
        Predict from which cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        for x in X:
            closest = self.__get_closest_centroid(x)
            print(f'datapoint {x[1:]} belongs to cluster {closest}.')


def get_usage() -> str:
    return f'Usage: python3 {sys.argv[0]} filepath=[path_to.csv] ncentroid=[K] max_iter=[X] where K and X are valid integers.'


def extract_arg(full_arg: str, prefix: str) -> str | None:
    if full_arg[:len(prefix)] != prefix:
        return None
    return full_arg[len(prefix):]


def main() -> None:
    if len(sys.argv) != 4:
        print(get_usage(), file=sys.stderr)
        return
    prefixes = ['filepath=', 'ncentroid=', 'max_iter=']
    file, k, max_iter = tuple(map(extract_arg, sys.argv[1:], prefixes))
    try:
        if not os.path.exists(file):
            raise FileNotFoundError
        k, max_iter = int(k), int(max_iter)
    except (FileNotFoundError, ValueError):
        print(get_usage(), file=sys.stderr)
        return
    print(f'{file=}, {k=}, {max_iter=}')
    with CsvReader(file, header=True, skip_top=1) as f:
        new_data = np.array([arr for arr in f.getdata()], dtype=float)
        header = f.getheader()
        # print(f'{new_data = }')
    kmeans = KmeansClustering(ncentroid=k, max_iter=max_iter)
    kmeans.fit(new_data)
    kmeans.display_centroids(new_data)
    # kmeans.predict(new_data)

    # print(f'{new_data[:,1] = }')
    combinations = [(1, 2), (1, 3), (2, 3)]
    citizens = kmeans.get_citizens(new_data)
    plt.close('all')
    colours = ['ro', 'bo', 'go', 'yo']

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    xline, yline, zline = new_data[:, 1], new_data[:, 2], new_data[:, 3]
    ax.scatter3D(xline, yline, zline, 'gray')
    ax.set_xlabel(header[1])
    ax.set_ylabel(header[2])
    ax.set_zlabel(header[3])
    plt.show()


if __name__ == '__main__':
    main()
