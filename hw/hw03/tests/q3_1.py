OK_FORMAT = True

test = {   'name': 'q3_1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> type(left_end_1) in set([float, np.float32, np.float64]) and type(right_end_1) in set([float, np.float32, np.float64])\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> left_end_1 == percentile(2.5, bootstrap_mean_based_estimates)\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> right_end_1 == percentile(97.5, bootstrap_mean_based_estimates)\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
