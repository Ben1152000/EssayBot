
from EssayBot import EssayBot

# begin code:
bot = EssayBot()

with open("essay.txt", "r") as essayFile:
	essayText = essayFile.read()
	bot.split(essayText)

