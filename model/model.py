import numpy as np

from constants import constants


class InputData:
    """
    encapsulation of data fed into the marketing mix model - both the marketing metrics and the sales metrics

    all 2-dimensional arrays have time (day or week number) as the first index and channel as the second index
    all numbers are numpy.uint64, all arrays of numbers are numpy array and numpy ndarray

    all values are true values (i.e. not scaled down for feeding into the MMM)
    """

    @staticmethod
    def _validate(date_strs, time_granularity, media_data, media_costs_per_unit, media_names, extra_features_data,
                  extra_features_names,
                  target_data,
                  target_name):
        num_observations = date_strs.shape[0]

        assert time_granularity in (constants.GRANULARITY_DAILY, constants.GRANULARITY_DAILY), f"{time_granularity}"

        assert 2 == media_data.ndim, f"{media_data.ndim}"
        assert num_observations == media_data.shape[0], f"{num_observations} {media_data.shape[0]}"
        num_channels = media_data.shape[1]
        assert np.float64 == media_data.dtype, f"{np.float64} {media_data.dtype}"

        assert 1 == media_costs_per_unit.ndim, f"{media_costs_per_unit.ndim}"
        assert num_channels == media_costs_per_unit.shape[0], f"{num_channels} {media_costs_per_unit.shape[0]}"
        assert np.float64 == media_costs_per_unit.dtype, f"{np.float64} {media_costs_per_unit.dtype}"

        assert num_channels == len(media_names), f"{num_channels} {len(media_names)}"

        assert 2 == extra_features_data.ndim, f"{extra_features_data.ndim}"
        num_extra_features = extra_features_data.shape[1]
        if num_extra_features:
            assert num_observations == extra_features_data.shape[
                0], f"{num_observations} {extra_features_data.shape[0]}"

        assert num_extra_features == len(extra_features_names), f"{num_extra_features} {len(extra_features_names)}"

        assert 1 == target_data.ndim, f"{target_data.ndim}"
        assert num_observations == target_data.shape[0], f"{num_observations} {target_data.shape[0]}"
        assert np.float64 == target_data.dtype, f"{np.float64} {target_data.dtype}"

        assert target_name

    def __init__(self, date_strs, time_granularity, media_data, media_costs_per_unit, media_names, extra_features_data,
                 extra_features_names,
                 target_data,
                 target_name):
        """
        :param date_strs: array of labels for each time series data point
        :param time_granularity: string constant describing the granularity of the time series data (
                                 constants.GRANULARITY_DAILY, constants.GRANULARITY_WEEKLY, etc.)
        :param media_data: 2-d array of float64 media data values [time,channel]
        :param media_costs_per_unit: 1-d array of float64 average media costs per unit [channel]
        :param media_names: 1-d array of media channel names
        :param extra_features_data: 2-d array of float64 extra feature values [time, channel]
        :param extra_features_names: 1-d array of extra feature names
        :param target_data: 1-d array of float64 target metric values
        :param target_name: name of target metric
        """
        InputData._validate(date_strs=date_strs, time_granularity=time_granularity, media_data=media_data,
                            media_costs_per_unit=media_costs_per_unit, media_names=media_names,
                            extra_features_data=extra_features_data, extra_features_names=extra_features_names,
                            target_data=target_data, target_name=target_name)

        self.date_strs = date_strs
        self.time_granularity = time_granularity
        self.media_data = media_data
        self.media_costs_per_unit = media_costs_per_unit
        self.media_names = media_names
        self.extra_features_data = extra_features_data
        self.extra_features_names = extra_features_names
        self.target_data = target_data
        self.target_name = target_name

    def dump(self):
        """
        Debugging routine
        :return:
        """
        print("Dumping input_data")
        print("\ndate_strs")
        for dstr in self.date_strs:
            print(f"{dstr}")

        print(f"\ntime_granularity={self.time_granularity}")
        print("\nmedia_data")
        for media_observation in self.media_data:
            media_line = ""
            for media_val in media_observation:
                media_line += f"{media_val:,.2f} "
            print(media_line)

        print("\nmedia_costs_per_unit")
        for media_cost in self.media_costs_per_unit:
            print(f"{media_cost:,.2f}")

        print("\nmedia_names")
        for media_name in self.media_names:
            print(f"{media_name}")

        print("\nextra_features_data")
        for extra_feature_observation in self.extra_features_data:
            extra_line = ""
            for extra_feature_val in extra_feature_observation:
                extra_line += f"{extra_feature_val:,.2f} "
            print(f"{extra_line}")

        print("\nextra_features_names")
        for extra_feature_name in self.extra_features_names:
            print(f"{extra_feature_name}")

        print("\ntarget_data")
        for target in self.target_data:
            print(f"{target:,.2f}")

        print(f"\ntarget_name={self.target_name}")
