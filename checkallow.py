from PyFunceble import DomainAvailabilityChecker as checker
import urllib3
urllib3.disable_warnings()

readfile = open("allow", "r")
DOMAINS = []
for line in readfile:
  line_list = line.strip()
  DOMAINS.append(line_list)
readfile.close()

file = open('deadallow', 'a')
for domain in DOMAINS:
    status = checker.set_subject(domain).get_status()
    if status == "INACTIVE":
        file.writelines(f"{domain}\n")
file.close()  
