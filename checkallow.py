from PyFunceble import test as PyFunceble

readfile = open("allow", "r")
DOMAINS = []
for line in readfile:
  line_list = line.strip()
  DOMAINS.append(line_list)
readfile.close()


def print_result(subject, status):

    if status == "ACTIVE":
        file = open('checkallow', 'a')
        file.writelines(f"{domain}\n")
        file.close()
    else:
        print(f"{domain} is {status}")

for domain in DOMAINS:
    print_result(domain, PyFunceble (domain))
