import modifiedDoublyLinkedList, RegexCheck

alphaSet = input("Enter alphabet set: ")
MDLL = modifiedDoublyLinkedList.ModifiedDoublyLinkedList(alphaSet)
regex_code = input("Enter regex expression: ")
validated_regex_code=RegexCheck.lexical_analysis(regex_code)

if validated_regex_code == regex_code :
    for i in regex_code:
        MDLL.addNode(i)

    MDLL.setFinalState()

    MDLL.printList(MDLL.head)

else:

    print(validated_regex_code)
