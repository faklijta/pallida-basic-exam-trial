# Create a function that takes a list of GitHub handles as input and returns a
# list of strings that represents
# GitHub url's under Green Fox Academy organization in the following format:
# "https://github.com/greenfox-academy/teststudent"

# example:
# input: ["ghhandle1", "ghhandle2"]
# output: ["https://github.com/greenfox-academy/ghhandle1", "https://github.com/greenfox-academy/ghhandle2"]

names = ["ghhandle1", "ghhandle2"]
# 1st try
output_base = "https://github.com/greenfox-academy/x"
def urls_from_handles(names):
    for i in names:
        output_base[-1] = names[i]
        print(output_base)
urls_from_handles(names)
# print(urls_from_handles(names))
# 2nd try
output_base = "https://github.com/greenfox-academy/"
def urls_from_handles(names):
    for i in names:
        url = output_base + names[i]
        print(url)
urls_from_handles(names)