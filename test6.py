def solution(companies, applicants):
    applying = {}
    for i, applicant in enumerate(applicants):
        applicants[i] = applicant.split(' ')

    for i, applicant in enumerate(applicants):
        cnt = int(applicant[2])
        applying[applicant[0]] = [applicant[1], cnt]

    for app in applying:
        applying[app] = [applying[app][0][1:], applying[app][1]-1]

    print(applying)
    # for i, company in enumerate(companies):


solution(["A fabdec 2", "B cebdfa 2", "C ecfadb 2"], ["a BAC 1",
                                                      "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]	)
