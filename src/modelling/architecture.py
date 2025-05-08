import tensorflow_probability as tfp

import numpy as np

import src.elements.master as mr


class Architecture:

    def __init__(self, arguments: dict):

        self.__arguments = arguments

    def __design(self, _training: np.ndarray):

        month_of_year_effect = tfp.sts.Seasonal(
            num_seasons=self.__arguments.get('seasons').get('number_of'),
            num_steps_per_season=self.__arguments.get('seasons').get('steps_per'),
            observed_time_series=_training,
            name='month_of_year_effect')

        autoregressive = tfp.sts.Autoregressive(order=1, observed_time_series=_training, name='autoregressive')

        model = tfp.sts.Sum([month_of_year_effect, autoregressive],
                            observed_time_series=_training)

        return model

    def exc(self, master: mr.Master):

        design = self.__design(_training=master.training['measure'].values)
