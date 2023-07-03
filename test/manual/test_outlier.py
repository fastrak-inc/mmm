import click
import numpy as np

from ...constants import constants
from ...model.model import InputData
from ...outlier.outlier import print_outliers


def test_print_outliers(output_dir):
    media1_values = np.array(
        [1, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5,
         2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 100000000],
        dtype=np.float64)

    media2_values = np.array(
        [5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5,
         2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 2],
        dtype=np.float64)

    media3_values = np.array(
        [1, 200000000, 300000000, 400000000, 500000000, 200000000, 300000000, 400000000, 500000000, 200000000,
         300000000, 400000000, 500000000, 200000000, 300000000, 400000000, 500000000, 200000000, 300000000, 400000000,
         500000000, 200000000, 300000000, 400000000, 500000000, 200000000, 300000000, 400000000, 500000000, 200000000,
         300000000, 400000000, 500000000, 200000000, 300000000, 400000000, 500000000,
         200000000, 300000000, 400000000, 500000000, 200000000, 300000000, 400000000, 500000000, 200000000, 300000000,
         400000000, 500000000, 200000000, 300000000, 400000000, 500000000, 200000000, 300000000, 400000000, 500000000,
         200000000, 300000000, 400000000, 500000000, 200000000, 300000000, 400000000, 500000000, 200000000, 300000000,
         400000000, 500000000, 100000000],
        dtype=np.float64)

    # noinspection PyUnusedLocal
    target_values = np.array([1 for x in media1_values], dtype=np.float64)

    input_data = InputData(
        date_strs=np.full(media1_values.shape[0], "1/1"),
        time_granularity=constants.GRANULARITY_DAILY,
        media_data=np.column_stack((media1_values, media2_values, media3_values)),
        media_costs=np.array([0.5, 0.6, 0.7], dtype=np.float64),
        media_costs_by_row=np.ndarray(shape=(0, 3)),
        media_priors=np.array([0.5, 0.6, 0.7], dtype=np.float64),
        media_names=np.array(["media1", "media2", "media3"]),
        extra_features_data=np.ndarray(shape=(0, 0)),
        extra_features_names=np.array([]),
        target_data=target_values,
        target_is_log_scale=False,
        target_name="Sales"
    )
    input_data.dump(output_dir=output_dir, suffix="brief", verbose=True)
    input_data.dump(output_dir=output_dir, suffix="detailed", verbose=False)

    print_outliers(input_data=input_data, output_dir=output_dir, suffix="test")


@click.command()
@click.option("--routine", required=True, help="routine name")
@click.option("--output_dir", required=False, help="output_dir arg for test_print_outliers")
def run(routine, **kwargs):
    """
    :param routine: routine name
    :return:
    """
    assert "test_print_outliers" == routine
    test_print_outliers(**kwargs)


if __name__ == "__main__":
    run()
