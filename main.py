import datetime

from network_process import DD_Automation
import time


title = f"A103 - Sunrise DD Change Push Mail Task Completion [{datetime.date.today().strftime('%d-%m-%Y')}] (Automation)"
toolID = "A103"
version = "2.4"
small_note = f"DD Change Push Mail task executed successful.\n New Total Number of DD Version and New Final DD Date."


def main():

    # Initiate Class-Object
    dd_plink = DD_Automation("nwx1116696", "!Huawei123")

    # Login to W3 Account
    dd_plink.w3_login()

    # Create Tasks
    dd_plink.create_task(Title=title, ToolID=toolID, Version=version, Small_Note=small_note)

    # Sleep before exit
    time.sleep(9999)

if __name__ == '__main__':

    main()
