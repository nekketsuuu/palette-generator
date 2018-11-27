import cv2
import numpy as np
import os
from sklearn.cluster import KMeans
import sys

n_clusters = 10
height = 16

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: {} <imgfile>".format(sys.argv[0]))
        sys.exit(1)
    
    filename = sys.argv[1]
    img = cv2.imread(filename)

    colors = img.reshape((img.shape[0] * img.shape[1], 3))
    km = KMeans(n_clusters=n_clusters)
    km.fit(colors)

    centers = km.cluster_centers_.reshape((1, n_clusters, 3)).astype(np.uint8)
    hsv = cv2.cvtColor(centers, cv2.COLOR_BGR2HSV).reshape((n_clusters, 3))
    hsv = hsv[np.argsort(hsv[:, 0])]  # sort by hue

    result = np.zeros((10, 16, 3), dtype=np.uint8)
    for y in range(0, 10):
        for x in range(0, 8):
            v = hsv[y, 2] - 20 * (7 - x)
            if v < 0:
                v = 0
            result[y, x, 0] = hsv[y, 0]
            result[y, x, 1] = hsv[y, 1]
            result[y, x, 2] = v
        for x in range(8, 16):
            v = hsv[y, 2] + 20 * (x - 8)
            if v > 255:
                v = 255
            result[y, x, 0] = hsv[y, 0]
            result[y, x, 1] = hsv[y, 1]
            result[y, x, 2] = v
    result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
    #result = cv2.resize(result, None, fx=10, fy=10, interpolation=cv2.INTER_NEAREST)

    prefix = os.path.splitext(filename)[0]
    resultname = prefix + "_palette.png"

    cv2.imwrite(resultname, result)

