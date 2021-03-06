class MaterialNavigator:
    icoCloseWindow = "material/ico/closeWinWhiteV2.png"
    icoLogo = "material/ico/logo.png"

    icoCancelDownload = "material/ico/cancelDownloadWhite.png"
    icoImportFile = "material/ico/importWhiteV4.png"
    icoDeleteFile = "material/ico/deleteWhite.png"


class StyleNavigator:
    pathOsuLoaderStyleCSS = "style/osuLoaderStyles.css"
    pathOsuLoaderStyleCSSVariables = "style/variables.txt"


class PropertiesNavigator:
    pathOsuLoaderPropertiesJSON = "properties/properties.json"
    pathOsuLoaderProperties = "properties/"


class FontsNavigator:
    fontExoRegular = "fonts/exo2/static/Exo2-Regular.ttf"
    fontExoThin = "fonts/exo2/static/Exo2-Thin.ttf"
    fontExoBold = "fonts/exo2/static/Exo2-Bold.ttf"


class Local:
    class Url:
        beatMapUrl = "https://osu.ppy.sh/beatmapsets"

    class Path:
        songPath = "Songs/"
        tempPath = "temp/"
        stylePath = "style/"
        propertiesPath = "properties/"
        osuExeFileName = "osu!.exe"

    class Song:
        format = "osz"

    class Osu:
        songPath = "Songs/"


class Variables:
    class Strings:
        osuLoaderWindowName = "osu!Loader 2.0"
        osuPathSelectorWindowName = "First run"
        labelTextFirstRun = "Please select osu folder below"
        labelTextFirstRunDialog = "Select osu folder"
        labelInputOsuPathTip = "osu! path"

        startOsuFolderText = "Select folder"
        warnNotOsuFolderText = "Osu folder should contains osu!.exe file. Please, choose another folder"
        findOsuFolderText = "Everything is fine"

        buttonImportAllText = "Import all"
        buttonDeleteAllText = "Delete all"

        buttonNext = "Next"
        buttonExit = "Exit"

        labelDownloads = "Downloads"

    class Integers:
        pass


class Structure:
    class DefaultProperties:
        stdProperties = {
            "app": {
                "window": {
                    "windowTitle": "osu! Loader 2.0",
                    "windowResolution": {
                        "x": 1280,
                        "y": 720
                    }
                },
                "osu": {
                    "osuPath": None
                }
            }
        }


    class StyleSheet:
        css = """QFrame{
  background-color: @windowColor;
}

QWidget{
  background-color: @windowColor;
}
QLabel{
  background-color: @windowColor;
  color: @textColor;
}
QPushButton{
  color: @textColor;
  background-color: transparent;
}
IconButton{
  border: none;
}
StandardButton{
  border: 2px solid;
  border-radius: 8;
  padding: 5%;
}
StandardButton:enabled{
  border-color: @textColor;
  color: @textColor;
}
StandardButton:disabled{
  border-color: @textDisabled;
  color: @textDisabled;
}
SimpleInputLabel{
  color: @textColor;
}
QVBoxLayout{
  margin-bottom: 0px;
  margin-top: 0px;
  margin-left: 0px;
  margin-right: 0px;
  border-radius: 10px;
}

QHBoxLayout{
  margin-bottom: 0;
  margin-top: 0;
  margin-left: 0;
  margin-right: 0;
}

ImportDelAllButton{
  font: 14pt 'Exo 2 Bold';
  color: @textColor;
  background-color: transparent;
  border-radius: 8;
  border: 2px solid;
  background: transparent;
}
ImportDelAllButton:disabled{
  border-color: @textDarkColor;
}

DownloadProgressBar{
  border: 2px solid grey;
  border-radius: 5px;
  background: @windowColor;
  text-align: center;
}

DownloadProgressBar::chunk{
  background-color: #b8b8b8;
  width: 1px;
}
ImportAllButton:enabled{
  border: 2px solid @greenColor;
}

DeleteAllButton:enabled{
  border: 2px solid @redColor;
}

LargeLabel{
  font: 14pt 'Exo 2 Bold';
}

SmallLabel{
  font: 10pt 'Exo 2 Bold';
}
        """

        variables = """@windowColor = #303030
@barColor = #262626
@browserColor = #1f1f1f
@textColor = #ababab
@textDarkColor = #8f8f8f
@textDisabled = #5e5e5e
@greenColor = #73AD21
@redColor = #AD2121
"""