from Condition import *

class require(Condition):
    def checkPreCondition(self):
        return self.condition(self.args)

    def makePreConditionErrorString(self):
        string = f"""
            Requirement failed at {self.getContractFileLocation()}
            {self.args}
            {self.makeFormattedDescription()}
        """
        return cleandoc(string)

    def makeFormattedDescription(self):
        return super().makeFormattedDescription(args = self.args)