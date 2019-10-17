import MySQLdb

import laofan.settings as conf


class Database(object):
    def __init__(self):
        self._client = MySQLdb.connect(
            unix_socket=conf.UNIX_SOCKET, db=conf.MYSQL_DBNAME, 
            user=conf.MYSQL_USER, passwd=conf.MYSQL_PASSWORD,
            charset='utf8', use_unicode=True)
        self._cursor = self._client.cursor()

    def execute_query(self, statement, args):
        try:
            self._cursor.execute(statement % args)
            return True
        except Exception as e:
            self._report_error(statement, args)   
            return False
    
    def execute_update(self, statement, args):
        try:
            self._cursor.execute(statement % args)
            return True
        except Exception as e:
            self._report_error(statement, args)            
            return False

    def execute_many(self, statement, args):
        for arg in args:
            if not self.execute_update(statement, arg):
                return False
        return True
    
    def execute_commit(self):
        try:
            self._client.commit()
            return True
        except Exception as e:
            self._report_error(str(e), None)
            return False

    def fetch_queryone(self):
        try:
            return self._cursor.fetchone()[0]
        except Exception as e:
            self._report_error(str(e), None)
            return None

    def _report_error(self, statement, args):
        error_info = "%s\n%s" % (statement, args)
        conf.email.send("数据库异常", error_info)
