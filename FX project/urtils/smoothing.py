import simdkalman
import numpy as np
import pandas as pd

def Smoothing_data(y, symbols) -> dict:
    """
    Smoothes the input time series data using the Kalman filter.

    Parameters:
        y (pd.DataFrame): Time series data.
        symbols (dict): Dictionary containing symbols to be smoothed.

    Returns:
        dict: A dictionary containing smoothed time series for each symbol.
    """
    symbolsmooths = {}

    # Iterate over symbols
    for syms in symbols["all"]:
        smooths = []

        # Iterate over smoothing parameters
        for isf in range(4, 5):
            for ins in range(4, 5):
                smoothing_factor = isf
                n_seasons = ins

                # Define state transition matrix A
                state_transition = np.zeros((n_seasons + 1, n_seasons + 1))
                state_transition[0, 0] = 1
                state_transition[1, 1:-1] = [-1.0] * (n_seasons - 1)
                state_transition[2:, 1:-1] = np.eye(n_seasons - 1)

                # Observation model H
                observation_model = [[1, 1] + [0] * (n_seasons - 1)]

                # Noise models
                level_noise = 0.2 / smoothing_factor
                observation_noise = 0.2
                season_noise = 1e-3

                process_noise_cov = np.diag([level_noise, season_noise] + [0] * (n_seasons - 1)) ** 2
                observation_noise_cov = observation_noise ** 2

                # Kalman filter initialization
                kf = simdkalman.KalmanFilter(
                    state_transition,
                    process_noise_cov,
                    observation_model,
                    observation_noise_cov
                )

                # Compute Kalman filter
                block = y[syms]
                n_train = block.shape[0]
                n_test = 60
                result = kf.compute(block, n_test)
                predictproba = result.smoothed.states.mean[:, 0]

                # Generate labels based on predicted probabilities
                y_label = [1 if predictproba[ivalue] > predictproba[ivalue - 1] else -1 for ivalue in range(1, len(predictproba))]

                smooths.append(y_label)

        symbolsmooths[syms] = smooths

    return symbolsmooths
