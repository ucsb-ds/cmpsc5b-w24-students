OK_FORMAT = True

test = {   'name': 'q2_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> print(ak_mn.num_rows == 44)\nTrue\n', 'hidden': False, 'locked': False},
                                   {'code': ">>> print(ak_mn.column('Murder rate in Alaska').item(0) == 10.19999981)\nTrue\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> print(ak_mn.column('Murder rate in Minnesota').item(0) == 1.200000048)\nTrue\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}