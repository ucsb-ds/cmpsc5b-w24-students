OK_FORMAT = True

test = {   'name': 'q2_4',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> 118 < np.mean(bootstrap_mean_based_estimates) < 126\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.random.seed(123)\n>>> avg = np.mean(sample_estimates(observations, mean_based_estimator, 7500))\n>>> np.isclose(avg, 122.33309803921568)\nTrue',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
