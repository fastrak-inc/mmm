import numpy as np
import random

from constants import constants
from plot import plot


def generate_rand_metric_values(num_observations):
    a = []
    for i in range(num_observations):
        a.append(random.randint(1, 1000))

    return np.array(a, dtype=np.uint64)


def test_plot_all_metrics(output_dir):
    num_observations = 10

    metric_names_and_values = {
        "first metric": generate_rand_metric_values(num_observations),
        "second metric": generate_rand_metric_values(num_observations),
        "third metric": generate_rand_metric_values(num_observations)
    }

    metrics_dict = {
        constants.KEY_GRANULARITY: constants.GRANULARITY_DAILY,
        constants.KEY_OBSERVATIONS: num_observations,
        constants.KEY_METRICS: metric_names_and_values
    }
    plot.plot_all_metrics(metrics_dict, output_dir)
