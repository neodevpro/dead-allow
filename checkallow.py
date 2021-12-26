from PyFunceble import DomainAvailabilityChecker
checker = DomainAvailabilityChecker()
import urllib3
urllib3.disable_warnings()

f = open("allow", "r")
o = open("deadallow", "a")
lines = f.readlines()
for line in lines:
    status = checker.set_subject(line).get_status()
    print(f"Checking {line} ?")
    if status.is_inactive() :
       o.write(f"{line}")
f.close()
o.close()
