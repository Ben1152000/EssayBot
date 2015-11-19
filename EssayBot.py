import re

class EssayBot:

	def split(self, essayTxt):
		paragraphs = removeEmptyStrings(re.split(r"\n", essayTxt))
		for i in range(len(paragraphs)):
			sentences = removeEmptyStrings(re.split(r"\.|\?|!|;", paragraphs[i]))
			
			for j in range(len(sentences)):
				
				
				words = removeEmptyStrings(re.split(r"\W", sentences[j]))
				print("    words    " + str(words))
				sentences[i] = words
				
			paragraphs[i] = sentences
			
		return paragraphs

def removeEmptyStrings(list):
	newList = []
	for string in list:
		if len(re.findall(r"\w", string)) > 0:
			newList.append(string)
	return newList

	