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
        osuExeFileName = "osu.exe"

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


        buttonImportAllText = "Import all"
        buttonDeleteAllText = "Delete all"

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
  border: none;
  background-color: transparent;
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
  border: 2px solid @textDarkColor;
  background: transparent;
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
ImportAllButton{
  border: 2px solid @greenColor;
}

DeleteAllButton{
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
@greenColor = #73AD21
@redColor = #AD2121
"""