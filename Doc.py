import datetime
from time import sleep
class Doc:
    def __init__(self, filepath, filename, content, creator, password):
        self.filepath = filepath  # 파일경로
        self.filename = filename  # 파일이름
        self.content = content  # 파일내용
        self.creator = creator  # 생성자
        self.password = password  # 비밀번호


        now = datetime.datetime.now()
        self.saved_time = now.strftime('%Y-%m-%d %H:%M:%S')  # 생성일시
        # self.mod_time = now.strftime('%Y-%m-%d %H:%M:%S')  # 수정일시

        self.mod_time = ''

    def to_string(self):
        result = f'''----------------------------
                        filepath: {self.filepath}, 
                        filename: {self.filename},
                        content: {self.content},
                        creator: {self.creator},
                        password: {self.password}
                        saved_time: {self.saved_time}
                        mod_time: {self.mod_time}
                        -------------------------------------
                        '''
        return result


    def set_content(self, p):
        self.content = p
        now = datetime.datetime.now()
        self.mod_time = now.strftime('%Y-%m-%d %H:%M:%S')  # 수정일시

    def append_text(self, s):
        self.content = self.content + s
        now = datetime.datetime.now()
        self.mod_time = now.strftime('%Y-%m-%d %H:%M:%S')  # 수정일시




msg = Doc("","","","","")
msg.set_content('1111\n')
print(msg.to_string())
sleep(3)
msg.append_text('2222\n')
print(msg.to_string())