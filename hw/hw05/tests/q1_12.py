OK_FORMAT = True

test = {   'name': 'q1_12',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> all([type(career_length_slope) in set([float, np.float32, np.float64]), type(career_length_intercept) in set([float, np.float32, np.float64]), '
                                               'type(salary_slope) in set([float, np.float32, np.float64]), type(salary_intercept) in set([float, np.float32, np.float64])])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all([np.round(career_length_slope, 3) == -0.009,\n'
                                               '...     np.round(career_length_intercept, 3) == 5.454,\n'
                                               '...     np.round(salary_slope, 3) == -16229.882,\n'
                                               '...     np.round(salary_intercept, 3) == 3732861.986])\n'
                                               'False',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
