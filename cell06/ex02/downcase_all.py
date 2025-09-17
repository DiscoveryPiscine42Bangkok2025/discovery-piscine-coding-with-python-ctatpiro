import sys
def downcase_all(words):
    return words.lower()
if len(sys.argv) < 2:
    print("none")
else:
    for i in sys.argv[1:]:
        print(downcase_all(i))