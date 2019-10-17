# 邮件配置
SMTP_PORT = 465
SMTP_SERVER = 'smtp.163.com'
SOURCE_ADDR= 'zsimline@163.com'
TARGET_ADDR = 'zsimline@163.com'
SMTP_PASSWORD = 'srline@wyyx.top'

# 起始地址
ITEMS = [
    ('https://www.yyzone.net/vodshow/dianying--time------1---.html',1,1,
    'movie','MovieParse',1,48),
    ('https://www.yyzone.net/vodshow/dianshiju--time------1---.html',1,2,
    'tvseries','TvseriesParse',1,96),
    ('https://www.yyzone.net/vodshow/zongyi--time------1---.html',1,1,
    'variety','VarietyParse',1,24),
    ('https://www.yyzone.net/vodshow/dongman--time------1---.html',1,1,
    'anime','AnimeParse',1,48),
]

# URL文件
FILES = [
    'movie.all.json',
    'tvseries.all.json',
    'variety.all.json',
    'anime.all.json'
]

# 数据库配置
MYSQL_USER = 'root'
MYSQL_PASSWORD = '201920'
MYSQL_DBNAME = 'redtea'
UNIX_SOCKET = '/opt/mysqldts/mysqld.sock'

# 运行时根路径
ROOT_DIR = '/opt/laofan/laofan'

# 日志备份路径
ERRORLOG = '/opt/log/laofan-error.log'
ERRORLOG_BACKUP = '/opt/backup/journal/laofan-error.log'
INFOLOG = '/opt/log/laofan-info.log'
INFOLOG_BACKUP = '/opt/backup/journal/laofan-info.log'
