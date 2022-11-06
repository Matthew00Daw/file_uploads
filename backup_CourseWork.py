import os.path
import sys
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload
from PyQt5 import QtWidgets
import UploadFiles


class UploadApp(QtWidgets.QMainWindow, UploadFiles.Ui_UploadFiles):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.FindFolderBtn.clicked.connect(self.BrowseFolder)
        self.CreateGoogleFolder.clicked.connect(self.CreateFolder)
        self.AuthorizationBtn.clicked.connect(self.Authorization)
        self.UploadFilesBtn.clicked.connect(self.GetUploadFiles)
        self.GetTimer.clicked.connect(self.GetTimerUpload)

    def GetTimerUpload(self):
        YY = self.getYears.value()
        MM = self.getMonth.value()
        DD = self.getDays.value()
        timer = (format(YY) + ' год. ' + format(MM) + ' месяц. ' + format(DD) + ' день')
        self.listWidget.addItem('Файлы будут выгружаться каждый:' + timer)

    def BrowseFolder(self):
        Directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        DirectoryName = os.path.basename(Directory)

        text = open('Directories.txt', 'a')
        Stext = open('FolderNames.txt', 'a')
        if Directory:
            self.listWidget.addItem(Directory)
            text.write(Directory + '/' + '\n')
            Stext.write(DirectoryName + '\n')

        text.close()
        Stext.close()

    def CreateFolder(self):
        if os.path.exists('token.json'):
            MyDrive = GoogleUpload()
            self.GetChildDir()
            FoldersName = open('FolderNames.txt', 'r')
            ChildFoldersName = open('ChildFoldersName.txt', 'r')
            Lines1 = FoldersName.readlines()
            if os.path.exists('FoldersID.txt'):
                FoldersID = open('FoldersID.txt', 'a')
            else:
                FoldersID = open('FoldersID.txt', 'w')
            if os.path.exists('ChildFoldersID.txt'):
                ChildFoldersID = open("ChildFoldersID.txt", 'a')
            else:
                ChildFoldersID = open('ChildFoldersID.txt', 'w')

            for line1 in Lines1:
                Res = MyDrive.CreateDriveFolder(line1)
                FoldersID.write(Res.get('id') + '\n')
            Lines2 = ChildFoldersName.readlines()
            for line2 in Lines2:
                Res = MyDrive.CreateDriveFolder(line2)
                ChildFoldersID.write(Res.get('id') + '\n')

            self.listWidget.addItem('Папки в облаке созданы.')
            FoldersName.close()
            FoldersID.close()
            ChildFoldersName.close()
            ChildFoldersID.close()
        else:
            self.listWidget.addItem('Необходимо авторизоваться!')

    def Authorization(self):
        GoogleUpload.__init__(self)
        if os.path.exists('token.json'):
            self.listWidget.addItem('Вы уже авторизованы')
        else:
            self.listWidget.addItem('Авторизация пройдена')

    def GetChildDir(self):
        file_1 = open('Directories.txt', 'r')
        file_2 = open('FoldersID.txt', 'r')
        CHN = open('ChildFoldersName.txt', 'a')
        CHD = open('ChildFoldersDir.txt', 'a')

        PATH = []
        ID = []

        with open('Directories.txt') as f:
            lines = 0
            for line in f:
                lines += 1

        while True:
            path = file_1.readline()
            path_file_1 = path.strip()
            PATH.append(path_file_1)

            if not path:
                break
        for i in PATH:
            if i == '':
                PATH.remove(i)

        while True:
            path_2 = file_2.readline()
            path_file_2 = path_2.strip()
            ID.append(path_file_2)

            if not path_file_2:
                break
        for j in ID:
            if j == '':
                ID.remove(j)

        for i in range(0, lines):

            dir = os.listdir(PATH[i])
            count = len(dir)
            print(PATH[i])

            # Главные директории
            for j in range(0, count):
                print(dir[j])
                CHN.write(dir[j] + '\n')
                # Дочерние папки

                print(os.listdir(PATH[i] + dir[j] + '/'))
                CHD.write(PATH[i] + dir[j] + '/' + '\n')
                # Файлы в дочерних папках

                print('\n')
        CHD.close()
        CHN.close()

        file_1.close()
        file_2.close()

    def GetMovingFolder(self):
        Move = GoogleUpload()
        Dir = open('Directories.txt', 'r')
        Parent = open('FoldersID.txt', 'r')
        Child = open('ChildFoldersID.txt', 'r')

        ParentID = []
        ChildID = []
        DIR = []

        with open('Directories.txt') as f:
            Dlines = 0
            for line in f:
                Dlines += 1
        with open('FoldersID.txt') as f:
            Plines = 0
            for line in f:
                Plines += 1
        with open('ChildFoldersID.txt') as f:
            Clines = 0
            for line in f:
                Clines += 1

        while True:
            dir = Dir.readline()
            dirStr = dir.strip()
            DIR.append(dirStr)

            if not dirStr:
                break
        for i in DIR:
            if i == '':
                DIR.remove(i)

        while True:
            pid = Parent.readline()
            pidStr = pid.strip()
            ParentID.append(pidStr)

            if not pidStr:
                break
        for i in ParentID:
            if i == '':
                ParentID.remove(i)

        while True:
            cid = Child.readline()
            cidStr = cid.strip()
            ChildID.append(cidStr)

            if not cidStr:
                break
        for j in ChildID:
            if j == '':
                ChildID.remove(j)
        for i in range(0, Dlines):
            dirs = os.listdir(DIR[i])
            count = len(dirs)
            for j in range(0, count):
                Move.MovingFolder(ParentID[i], ChildID[j])
        Parent.close()
        Child.close()
        Dir.close()

    def GetFolderQuantity(self):
        lines = 0
        with open('ChildFoldersDir.txt') as f:
            for line in f:
                lines += 1
        return lines

    def GetUploadFiles(self):
        if os.path.exists('token.json'):
            MyDrive = GoogleUpload()
            self.GetMovingFolder()
            f1 = open('ChildFoldersDir.txt', 'r')
            f2 = open('ChildFoldersID.txt', 'r')

            PATH = []
            ID = []

            while True:
                path = f1.readline()
                pathStr = path.strip()
                PATH.append(pathStr)

                if not path:
                    break
            for i in PATH:
                if i == '':
                    PATH.remove(i)

            while True:
                id = f2.readline()
                idStr = id.strip()
                ID.append(idStr)

                if not idStr:
                    break
            for j in ID:
                if j == '':
                    ID.remove(j)

            FQ = UploadApp.GetFolderQuantity(self)
            print(FQ)
            for i in range(0, FQ):
                files = os.listdir(PATH[i])
                count = len(files)
                for j in range(0, count):
                    for item in files:
                        MyDrive.UploadFiles(item, PATH[i], ID[j])
            self.listWidget.addItem('Файлы выгружены')
            f1.close()
            f2.close()
        else:
            self.listWidget.addItem('Необходимо авторизоваться!')



class GoogleUpload():
    # Создание/чтение токен файла (для доступа к аккаунту)
    def __init__(self):
        SCOPES = ['https://www.googleapis.com/auth/drive']
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # Вход в систему пользователем
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Сохранение прав доступа
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        self.service = build('drive', 'v3', credentials=creds)

    # Листинг последних файлов
    def FileListing(self, PageSize=30):
        f = open('listing.txt', 'w')
        results = self.service.files().list(
            pageSize=PageSize, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            f.write('Файлы не найдены.')
        else:
            f.write('Файлы:')
            for item in items:
                f.write(u'{0} ({1})'.format(item['name'], item['id']))
        f.close()

    def UpdateFiles(self, FolderName, path, FolderID):
        media = MediaFileUpload(f"{path}{FolderName}")
        response = self.service.files().list(
            q=f"name='{FolderName}' and parents='{FolderID}'",
            spaces='drive',
            fields='nextPageToken, files(id, name)',
            pageToken=None
        ).execute()
        for file in response.get('files', []):
            UpdateFile = self.service.files().update(fileId=file.get('id'), media_body=media).execute()
            print(f'Файл обновлён.')

    # Загрузкв файлов в облако
    def UploadFiles(self, FolderName, path, FolderID):

        media = MediaFileUpload(f"{path}{FolderName}")

        response = self.service.files().list(
            q=f"name='{FolderName}' and parents='{FolderID}'",
            spaces='drive',
            fields='nextPageToken, files(id, name)',
            pageToken=None
        ).execute()
        if len(response['files']) == 0:
            FileMetadata = {
                'name': FolderName,
                'mimeType': 'application/dat',
                'parents': [FolderID]
            }
            file = self.service.files().create(body=FileMetadata, media_body=media, fields='id').execute()
            print(f"Создан новый файл: {file.get('id')}")

    def CreateDriveFolder(self, DriveFolderName, FolderID=None):
        # Создание папки в облаке и возвращение ID

        body = {
            'name': DriveFolderName,
            'parents': FolderID,
            'mimeType': "application/vnd.google-apps.folder"
        }
        if FolderID:
            body['parents'] = FolderID
        results = self.service.files().create(body=body).execute()
        return results

    def MovingFolder(self, ParentFolderID, ChildFolderID):
        # Получение родительской папки для перемещения
        file = self.service.files().get(fileId=ChildFolderID,
                                        fields='parents').execute()
        previous_parents = ",".join(file.get('parents'))
        # Перемещение папки в новую папку
        file = self.service.files().update(fileId=ChildFolderID,
                                           addParents=ParentFolderID,
                                           removeParents=previous_parents,
                                           fields='id, parents').execute()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = UploadApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    main()

