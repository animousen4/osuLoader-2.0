import ResourceNavigator


class cssLoader():
    def __loadVariables(self):
        var = []
        f = open(ResourceNavigator.StyleNavigator.pathOsuLoaderStyleCSSVariables, "r")
        for line in f:
            varName = line.split("=")[0].replace(" ", "").replace("\n", "")
            varValue = line.split("=")[1].replace(" ", "").replace("\n", "")
            var.append(variable(varName, varValue))
        return var

    def __loadCss(self, variables):
        f = open(ResourceNavigator.StyleNavigator.pathOsuLoaderStyleCSS, "r")
        css = f.read()  # .replace("\n", "")
        for var in variables:
            css = css.replace(var.name, var.value)
        return css
        pass

    def getStyleSheet(self):
        variables = self.__loadVariables()
        css = self.__loadCss(variables)
        return css
        pass


class variable():
    name = "varName"
    value = "varValue"

    def __init__(self, name, value):
        super().__init__()
        self.name = name
        self.value = value

