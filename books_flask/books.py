from pymysql import connect


class BOOK(object):
    def __int__(self):  # ��������ͬʱҪִ�еĴ���
        self.conn = connect(
            host='43.248.8.5',
            port=3306,
            user='root',
            passwd='1234',
            databases='demo',
        )
        self.cursor=self.conn.cursor()

    def __del__(self):  # �ͷŶ���ͬʱҪִ�еĴ���
        self.cursor.close()
        self.conn.close()