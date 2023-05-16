import click
import numpy as np

from outlier.outlier import print_outliers


def test_print_outliers():
    metric_values1 = np.array(
        [1, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5,
         2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 100000000],
        dtype=np.uint64)
    metric_values2 = np.array([1, 2, 3, 4, 5], dtype=np.uint64)
    metric_values3 = np.array(
        [1, 100000000, 200000000, 300000000, 400000000, 500000000, 100000000, 200000000, 300000000, 400000000,
         500000000, 100000000, 200000000, 300000000, 400000000, 500000000, 100000000, 200000000, 300000000, 400000000,
         500000000, 100000000, 200000000, 300000000, 400000000, 500000000, 100000000, 200000000, 300000000, 400000000,
         500000000, 100000000, 200000000, 300000000, 400000000, 500000000, 100000000, 200000000, 300000000, 400000000,
         500000000, 100000000, 200000000, 300000000, 400000000, 500000000, 100000000, 200000000, 300000000, 400000000,
         500000000, 100000000, 200000000, 300000000, 400000000, 500000000, 100000000, 200000000, 300000000, 400000000,
         500000000, 100000000, 200000000, 300000000, 400000000, 500000000, 100000000, 200000000, 300000000, 400000000,
         500000000, 100000000, 200000000, 300000000, 400000000, 500000000, 100000000, 200000000, 300000000, 400000000,
         500000000, 100000000, 200000000, 300000000, 400000000, 500000000], dtype=np.uint64)

    metric_data = {"metric1": metric_values1, "metric2": metric_values2, "metric3": metric_values3}
    print_outliers(metric_data)


@click.command()
@click.option("--routine", required=True, help="routine name")
def run(routine):
    """
    :param routine: routine name
    :return:
    """
    assert "test_print_outliers" == routine
    test_print_outliers()


if __name__ == "__main__":
    run()