OK_FORMAT = True

test = {   'name': 'q2_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> len(example_estimates) == 10000\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> 850 < np.mean(example_estimates) < 1100\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.count_nonzero(np.diff(example_estimates)) >= 1\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.random.seed(123)\n>>> avg = np.mean(sample_estimates(one_sample, mean_based_estimator, 10000))\n>>> np.isclose(avg, 897.954712)\nTrue',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
