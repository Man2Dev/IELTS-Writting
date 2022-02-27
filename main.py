import language_tool_python

# from database import insert_exam

tool = language_tool_python.LanguageTool("en-US")

# input text
text = "a santence with a error in the Hitchhiker’s Guide tot he Galaxy. hallo how are yoo."

matches = tool.check(text)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# printing all mistakes
i = 0
for match in matches:
    # print(f"\nMatch {i+1}:\n")
    # errText
    print("1\nMessage:\n", match.message, "\n")
    # errOffset
    print("2\nOffset:", matches[i].offsetInContext, "\n")
    # errLength
    print("3\nerrorLength:", matches[i].errorLength, "\n")
    # context
    print("4\ncontext:", matches[i].context, "\n")
    # category
    print("5\nCategory:", matches[i].category, "\n")
    # ruleIssue
    print("6\nRule Issue Type:", matches[i].ruleIssueType, "\n")
    # sentence
    print("7\nSentence:", matches[i].sentence, "\n")
    # numberSuggestion, suggestion
    print(
        f"8\nID [{len(matches[i].replacements)} Suggestions]:\n",
        # ruleID
        matches[i].ruleId,
        matches[i].replacements,
        "\n",
    )
    # print("9\nMatche:\n", matches[i])
    print("-" * 90)
    i += 1

print("\n" + 110 * "#")
# numberMistakes
print("Number of mistakes:\t", len(matches))
# inputText
print("Input text:\t\t", text)
# autoCorrected
print("Auto Corrected:\t\t", tool.correct(text))
print("Auto Corrected:\t\t", language_tool_python.utils.correct(text, matches))

print(110 * "#")

tool.close()  # Call `close()` to shut off the server when you're done.