OK_FORMAT = True

test = {   'name': 'q1_6',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> -5 <= diff_lower_bound <= diff_upper_bound <= 12\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> -1.25 <= diff_lower_bound <= diff_upper_bound <= 11\nTrue', 'hidden': True, 'locked': False},
                                   {   'code': '>>> all([diff_lower_bound == percentile(2.5, sampled_leads), diff_upper_bound == percentile(97.5, sampled_leads)])\nTrue',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
