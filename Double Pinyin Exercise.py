import random

def generate(Initials,Syllables):
	geneInitial=Initials[int(random.uniform(0,len(Initials)-0.01))]
	geneSyllable=Syllables[int(random.uniform(0,len(Syllables)-0.01))]
	return [geneInitial,geneSyllable]

def inputcheck(inputstring,genestring,Pairs):
	InitialLetter=Pairs[genestring[0]]
	SyllableLetter=Pairs[genestring[1]]
	if (InitialLetter+SyllableLetter)==(inputstring):
		return [True,InitialLetter+SyllableLetter]
	else:
		return [False,InitialLetter+SyllableLetter]

def main():
	Initials=['b','p','m','f','d','t','n','l','g','k','h','j','q','x',\
				'zh','ch','sh','r','z','c','s','y','w']
	Syllables=['a','o','e','i','u','v','ai','ei','ui','ao','ou','iu',\
				'ie','ue','er','an','en','in','un','ang','eng','ing','ong']
	Pairs={"q":"q","iu":"q","w":"w","ia":"w","ua":"w","e":"e","r":"r",\
				"uan":"r","er":"r","t":"t","ue":"t","y":"y","uai":"y",\
				"ing":"y","sh":"u","u":"u","ch":"i","i":"i","o":"o",\
				"uo":"o","p":"p","un":"p","a":"a","s":"s","ong":"s",\
				"iong":"s","d":"d","uang":"d","iang":"d","f":"f",\
				"en":"f","g":"g","eng":"g","h":"h","ang":"h","j":"j",\
				"an":"j","k":"k","ao":"k","l":"l","ai":"l","z":"z",\
				"ei":"z","x":"x","ie":"x","c":"c","iao":"c","zh":"v",\
				"ui":"v","v":"v","b":"b","ou":"b","n":"n","in":"n",\
				"m":"m","ian":"m"}
	print("请输入下面对应双拼规则，是用空格隔开，退出输入exit")
	while 1:
		genestring=generate(Initials,Syllables)
		print(genestring)
		str=input()
		if str=='exit':
			break
		result=inputcheck(str,genestring,Pairs)
		if result[0]:
			print("恭喜正确")
		else:
			print("错误，或许可以试试{}".format(result[1]))
	

main()