import modifiedDoublyLinkedList, RegexCheck

alphabets = input("Enter alphabets: ")
alphaset = set(alphabets)

MDLL = modifiedDoublyLinkedList.ModifiedDoublyLinkedList(alphaset)
regex_code = input("Enter regex expression: ")
validated_regex_code = RegexCheck.lexical_analysis(regex_code)

if validated_regex_code == regex_code :
    for i in regex_code:
        print(i)
        MDLL.addNode(i)
        print(MDLL.orStack,MDLL.paranthesisStack)

    MDLL.setFinalState()

    MDLL.visualizeGraph()

else:
    print(validated_regex_code)