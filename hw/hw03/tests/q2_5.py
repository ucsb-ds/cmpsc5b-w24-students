OK_FORMAT = True

test = {   'name': 'q2_5',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> max(bootstrap_max_estimates) <= 135\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.random.seed(123)\n>>> avg = np.mean(sample_estimates(observations, max, 10000))\n>>> np.isclose(avg, 122.0788)\nTrue',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
