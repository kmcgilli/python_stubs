import re, sys, os
p=re.compile(sys.argv[2], re.IGNORECASE)

#sample input: python err_log_tablenames.py "C:\Users\YourName\Documents\giant_Log.txt" "^2021-07-.*FAILED: SemanticException Unable to fetch table .*"

for line in open(sys.argv[1]).readlines():
    if re.match(p, line):
        m=re.match(p,line)
#        print(m.group())
        tnm=re.split(r'\W+', m.group())
        print(tnm[-2])