import numpy as np
import tensorflow_probability as tfp
import tensorflow_probability.python.experimental.util as tfu
import tf_keras

import src.elements.master as mr


class Architecture:

    def __init__(self, arguments: dict):

        self.__arguments = arguments

    def __model(self, _training: np.ndarray):

        month_of_year_effect = tfp.sts.Seasonal(
            num_seasons=self.__arguments.get('seasons').get('number_of'),
            num_steps_per_season=self.__arguments.get('seasons').get('steps_per'),
            observed_time_series=_training,
            name='month_of_year_effect')

        autoregressive = tfp.sts.Autoregressive(order=1, observed_time_series=_training, name='autoregressive')

        model = tfp.sts.Sum([month_of_year_effect, autoregressive],
                            observed_time_series=_training)

        return model

    def __variational(self, model, _training: np.ndarray):

        posterior = tfp.sts.build_factored_surrogate_posterior(
            model=model)

        # Evidence Lower Bound Loss Curve Data
        elb = tfp.vi.fit_surrogate_posterior(
            target_log_prob_fn=model.joint_distribution(observed_time_series=_training).log_prob,
            surrogate_posterior=posterior,
            optimizer=tf_keras.optimizers.Adam(learning_rate=self.__arguments.get('learning_rate')),
            num_steps=self.__arguments.get('n_variational_steps'),
            jit_compile=True, seed=self.__arguments.get('seed'), name='fit_surrogate_posterior')

        return posterior, elb

    def exc(self, master: mr.Master):

        model = self.__model(_training=master.training['measure'].values)

        v_posterior: tfu.DeferredModule
        v_posterior, v_elb = self.__variational(model=model, _training=master.training['measure'].values)
        v_posterior_samples = v_posterior.sample(self.__arguments.get('n_samples'))
