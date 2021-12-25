from PyFunceble import DomainAvailabilityChecker
import urllib3
urllib3.disable_warnings()
checker = DomainAvailabilityChecker()
status = checker.set_subject(domain).get_status()

readfile = open("allow", "r")
DOMAINS = []
for line in readfile:
  line_list = line.strip()
  DOMAINS.append(line_list)
readfile.close()

file = open('deadallow', 'a')
for domain in DOMAINS:
    if status = "INACTIVE":
        file.writelines(f"{domain}\n")
file.close()  
