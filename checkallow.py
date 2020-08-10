from PyFunceble import test as PyFunceble

readfile = open("allow", "r")
DOMAINS = []
for line in readfile:
  line_list = line.strip()
  DOMAINS.append(line_list)
readfile.close()


def print_result(subject, status):

    if status == "ACTIVE":
        print(f"{domain} is {status}")
    else:
        file = open('deadallow', 'a')
        file.writelines(f"{domain}\n")
        file.close()        

for domain in DOMAINS:
    print_result(domain, PyFunceble (domain))
