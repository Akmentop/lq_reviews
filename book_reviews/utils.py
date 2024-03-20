
MAX_STR_LEN = 100

# id, date, book name, description, photo link, cost, review
REVIEWS_MOCK_DATA = [
    [1, '2023/01/01', 'Learn MySQL ed 1', 'talk about SQL',
     '/images/my_images.png', 68.00,
     'this is a great book!'],
    [2, '2023/01/02', 'Learn MySQL ed 2', 'talk about SQL', '', 69.00,
     'this is a great book!'],
    [3, '2023/01/03', 'Learn MySQL ed 3', 'talk about SQL', '', 80.00,
     'this is a great book!'],
    [4, '2023/01/04', 'Learn MySQL ed 4', 'talk about SQL', '', 81.00,
     'this is a great book!'],
    [5, '2023/01/05', 'Learn MySQL ed 5', 'talk about SQL', '', 82.00,
     'this is a great book!'],
    [6, '2023/01/06', 'Learn MySQL ed 6', 'talk about SQL', '', 83.00,
     'this is a great book!'],
    [7, '2023/01/07', 'Learn MySQL ed 7', 'talk about SQL', '', 84.00,
     'this is a great book!'],
    [8, '2023/01/08', 'Learn MySQL ed8 ', 'talk about SQL', '', 85.00,
     'this is a great book!'],
    [9, '2024/01/01', 'Learn MySQL ed8 ',
     '''Get a comprehensive overview on how to set up and design an effective 
     database with MySQL. This thoroughly updated edition covers MySQL's 
     latest version, including its most important aspects. Whether you're 
     deploying an environment, troubleshooting an issue, or engaging in 
     disaster recovery, this practical guide provides the insights and tools 
     necessary to take full advantage of this powerful RDBMS.

     Authors Vinicius Grippa and Sergey Kuzmichev from Percona show 
     developers and DBAs methods for minimizing costs and maximizing 
     availability and performance. You'll learn how to perform basic 
     and advanced querying, monitoring and troubleshooting, database 
     management and security, backup and recovery, and tuning for improved 
     efficiency. This edition includes new chapters on high availability, 
     load balancing, and using MySQL in the cloud.
     ''',  '', 86.00,
     '''Vinicius M. Grippa is a Senior Support Engineer at Percona and has 
     assisted customers (including Fortune 100 companies) in that capacity 
     for the past three years. He also performs spot checks for other 
     engineers at Percona, to assist in their development and to spread 
     knowledge among his team. In addition to these responsibilities, 
     Vinicius has written and reviewed articles for the Knowledge Base, 
     and has served as a conference program chair for the Percona Live 
     Conference & Expo 2019 and 2020, assisting with the development of 
     each meeting's program and agenda. Prior to his tenure at Percona, 
     Vinicius was a system analyst and DBA for nearly a decade. 
     '''],
]


def get_summary_list() -> list:
    # truncate long desc and review
    return [
        [[i[1], i[2], shorten(i[6])], i[0]] for i in REVIEWS_MOCK_DATA
    ]


def get_review_detail(review_id: int) -> list[str]:
    r = REVIEWS_MOCK_DATA[review_id - 1]
    r[3] = use_br(r[3])
    r[6] = use_br(r[6])
    return r


def use_br(msg: str) -> str:
    return msg.replace('\n', '<br />')


def shorten(msg: str) -> str:
    return use_br(
        msg[:MAX_STR_LEN] + ('...' if len(msg) > MAX_STR_LEN else ''))

