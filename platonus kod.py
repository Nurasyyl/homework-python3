
auditornuyi = float(input("орташа  бағасын енгізіңіз (0-ден 100-ге дейін): "))
bir_aralyk_baqylau = float(input("1-аралық бақылау бағасын енгізіңіз (0-ден 100-ге дейін): "))
eki_aralyk_baqylau = float(input("2-аралық бақылау бағасын енгізіңіз (0-ден 100-ге дейін): "))
session_baqasy = float(input("Сессиядан қанша аламын деп ойлайсыз (0-ден 100-ге дейін): "))




qorytyndy_baqa = (auditornuyi * 0.4 +bir_aralyk_baqylau*0.1+eki_aralyk_baqylau *0.1+ session_baqasy * 0.4)


print("Сіздің қорытынды бағаңыз: ", qorytyndy_baqa)



