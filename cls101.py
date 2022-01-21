import dropbox

class TransferData:
    def __init__ (self,token):
        self.token=token
    def uploadFiles(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.token)
        f=open(fileFrom,"rb")
        dbx.files_upload(f.read(),fileTo)
    
def main():
    token="sl.BAYlo1h9QKcPTvzm6p4UDMenJgebDvesHxxI7o_vcmNXW_iczdNRhJw9oFNJwmxJJ99I-g9eKBtjcF86A6EmD1OcsyzVDrHaB5PyefcQh8F2sleq1sJXIXM0x75DE_sG5PklP0Q"
    sentData=TransferData(token)
    source=input("Enter The File Path To Transfer= ")
    destination=input("Enter The Full Path To Upload To DropBox= ")
    sentData.uploadFiles(source,destination)
    print("Your File Has Been Moved!!!")
main()