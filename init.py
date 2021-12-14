'''MAIN SETTINGS'''
def writeSessings(f,dic,title):
    str = ' \n /* ' + title + ' */ \n\n'
    f.write(str)

    for key in dic:
        str = 'const ' + key + ' = "' + dic[key] + '";\n'
        f.write(str)

main_path = {'BASE_URL':'/***/'}
settings_1c = {'USER_1C':'***', 'PASS_1C':'***', 'IP_SERVER_1C': '***', 'URL_1C':'/***/'}
settings_sql = {'IP_SRV':'***','SQL_DB':'***','SQL_USER':'***','SQL_PASS':'***'}

f = open('settings.php','w')
f.write('<?php')

writeSessings(f,main_path,'main')
writeSessings(f,settings_1c,'1C')
writeSessings(f,settings_sql,'SQL')


