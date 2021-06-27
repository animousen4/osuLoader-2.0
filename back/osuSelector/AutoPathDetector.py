import winreg


def __foo(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)

            if winreg.QueryValueEx(asubkey, "DisplayName")[0] == "osu!":
                #print("Found!")
                iconPath = str(winreg.QueryValueEx(asubkey, "DisplayIcon")[0])
                path = iconPath.replace("\osu!.exe", "").replace("\\", "/")

                return path
        except EnvironmentError:
            continue

    return None

def getOsuPath():
    try:
        return __foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY)
    except Exception:
        return None

