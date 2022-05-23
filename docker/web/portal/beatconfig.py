from datetime import timedelta


BEAT_SCHEDULE = {
    'test_print': [
        {
            'type': 'test.print',
            'message': {'testing': 'one'},
            'schedule': timedelta(seconds=5),
        },
        # {
        #     'type': 'test.print',
        #     'message': {'testing': 'two'},
        #     # Precisely at 3AM on Monday
        #     'schedule': '0 3 * * 1'
        # },
    ],
    # 'jira_update_tt': [
    #     {
    #         'type': 'jira.get.tt',
    #         'message': {'testing': 'one'},
    #         'schedule': timedelta(seconds=60)
    #     },
    # ],
    # 'tg_ping': [
    #     {
    #         'type': 'index',
    #         'message': {'testing': 'one'},
    #         'schedule': timedelta(seconds=10)
    #     },
    # ],
}
