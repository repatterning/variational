import collections

import numpy as np
import pandas as pd
import tensorflow_probability as tfp

import tensorflow_probability.python.sts.components as tfc

import src.elements.master as mr



class Predicting:

    def __init__(self, arguments: dict):

        self.__arguments = arguments

    def exc(self, master: mr.Master, model: tfc.Sum, v_posterior_samples: collections.OrderedDict):


        # The value of each future observation is unknown, hence np.nan
        data = pd.concat((master.training['measure'], master.testing['measure']), ignore_index=True).values
        data = np.concat((data, np.repeat(np.nan, self.__arguments.get('ahead'))))

        distribution = tfp.sts.one_step_predictive(
            model=model,
            observed_time_series=data,
            parameter_samples=v_posterior_samples)

