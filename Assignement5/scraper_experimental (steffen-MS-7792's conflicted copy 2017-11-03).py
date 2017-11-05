import re
import urllib.request

#experimental version trying to solve the last remark about referenced hyperlinks
root = "A"

def find_emails(text):
    """
    function that scans a string "text" and returns
    a list of all "email like" expressions.
    """
    regex = r"([a-zA-Z0-9.#$%&~’*+-/=?‘|{}]+?@[a-zA-Z0-9.#$%&~’*+-/=? ‘|{}_]+?\.[a-zA-Z][a-zA-Z.,_]*?[a-zA-Z](?!jpg)(?<!png))"
    match = re.findall(regex,text)
    return match

def find_hyperlinks(text):
    """
    function that scans a string "text" in HTML format and returns
    a list of all "url like" expressions.
    """
    global root
    regex1 = r"<a href=(['\"])(\w*://\w*?[a-zA-Z][a-zA-Z.,_]*[a-zA-Z]\.[a-zA-Z][a-zA-Z.,_]*[a-zA-Z][\w.~/-]*)\1"
    regex2 = r"<a href=['\"](.*?.html)['\"]" #experimental to catch relative links
    matches1 = re.findall(regex1,text)
    matches1 = [match[1] for match in matches1] # the regex captures an extra empty string
    matches2 = re.findall(regex2,text)
    #print(root)
    matches2 = [root + match[1] for match in matches2] # the regex captures an extra empty string
    #print(matches1 + matches2)
    return matches1

def all_the_emails(url,depth):
    """
    function to recursively search for email adresses on a HTML string.
    The function stores all hyperlinks and email adresses and then follows
    the links to search for more recursively a number of times.

    url: start adress for search
    depth: number of hyperlink layeres to follow (carefull on this one)

    Function stores finds in the files hyperlinks.txt and emails.txt
    """
    # initial
    html = str(url_to_html(url))
    hyperlinks = find_hyperlinks(html)
    emails = find_emails(html)
    length = 0
    i = 0
    global root # yikes "global"
    print("stealing stuff!")
    while i < depth:
        print("sneaking around")
        # Iknow the task specifically ask for a call to
        # itself, but i find this to be an easier implementation
        for k in range(len(hyperlinks)-length): #iterate over all new links
            try:
                html = str(url_to_html(hyperlinks[k]))
                root = str(hyperlinks[k])
                hyperlinks += find_hyperlinks(html)
                emails += find_emails(html)
                hyperlinks = remove_duplicates(hyperlinks)
                emails = remove_duplicates(emails)
                length = len(hyperlinks)
            except urllib.error.HTTPError as e:
                if e.code in (..., 403, ...):
                    continue
            else:
                continue
        i += 1 # depth counter
    hyperlinks = remove_duplicates(hyperlinks)
    emails = remove_duplicates(emails)
    print("found %i hyperlinks" % len(hyperlinks))
    write_list_to_file(hyperlinks, "hyperlinks.txt")
    print("found %i emails" % len(emails))
    write_list_to_file(emails, "emails.txt")

#####additional functions for tidyness#####

def remove_duplicates(mylist):
    """
    removes anny duplicate entries in a list
    """
    newlist = []
    for i in mylist:
        if i not in newlist:
            newlist.append(i)
    return newlist

def url_to_html(url):
    """opens url and copies pure HTML as string"""
    with urllib.request.urlopen(url) as url:
        html = url.read() #from StackOverflow
    return html

def write_list_to_file(list_name, file_name):
    f = open(file_name, 'w')
    for item in list_name:
        f.write(item + "\n")


if __name__ == "__main__":

    #url = "https://vg.no/"
    #depth = 10
    #all_the_emails(url,depth)
    text = """Gard.Steiro@vg.no
Tora.Bakke.Handlykken@vg.no
Jane.Throndsen@vg.no
Hanne.Skartveit@vg.no
2200@vg.no
vektklubb@vg.no
//www.vg.no/tips/?til=kristine.hellesland@vg.no
//minmote.vgc.no/images/touch-icons/Icon-60@2x.png
//minmote.vgc.no/images/touch-icons/Icon-76@2x.png
godt@vg.no
//f14a5738998a4c3ba5f5a71fc46095fa@sentry.tu.no
tips@tek.no
diskusjon@vg.no
gard.steiro@vg.no
per.valebrokk@e24dinepenger.no
henrik.valstad@e24dinepenger.no
andreas.wolden.fredriksen@e24dinepenger.no
oyvind.henriksen@dinepenger.no
tips@dinepenger.no
abonnement@dinepenger.no
oyvind.henriksen@e24.no
pent@vg.no
jane.throndsen@vg.no
VGPartnerstudio@vg.no
marthe.reienes@vg.no
familieklubben@vg.no
jari.bakken@vg.no
//vglive.no/img/og/vglive-fb@2x.jpg
personvern@vg.no
Tips@tek.no
niklas@tek.no
kurt@tek.no
stein@tek.no
xa0niklas@tek.no
//presse.no/wp-content/themes/riiskit-lite/style/img/logo-pfu@2x.png
//presse.no/wp-content/themes/riiskit-lite/style/img/icons/icon-fontsizing@2x.png
//presse.no/wp-content/themes/riiskit-lite/style/img/icons/icon-menu@2x.png
51-1024x393@2x.jpg
51-300x115@2x.jpg
51-960x368@2x.jpg
//presse.no/wp-content/themes/riiskit-lite/style/img/logo-footer-np@2x.png
np@presse.no
pfu@presse.no
pou@presse.no
5-1024x393@2x.jpg
5-300x115@2x.jpg
5-960x368@2x.jpg
//presse.no/wp-content/themes/riiskit-lite/style/img/logo-np@2x.png
//presse.no/wp-content/uploads/2014/06/galopp-1024x393@2x.jpg
//presse.no/wp-content/uploads/2017/08/PFU-29-08-2017--295x167@2x.jpg
//presse.no/wp-content/uploads/2017/08/PFU-29-08-2017--17x11@2x.jpg
//presse.no/wp-content/uploads/2017/06/PFU-20-06-2017-295x167@2x.jpg
//presse.no/wp-content/uploads/2017/06/PFU-20-06-2017-17x11@2x.jpg
ola.stenberg@vg.no
abonnement@aftenposten.no
taa@hsmedia.no
sammenligning%20sparem%C3%A5ter@2x_NY2.png
post@prisguide.no
faktura@prisguide.no
kundeservice@chilimobil.no
magnus.braaten@vg.no
/Templates/FrontNew/img/hero-1920@2x.jpg
epost@forskning.no
mathilde.sundet.ruud@schibsted.com
xdf@WM.VL
xe4@%.AD
xf0.N@q.Tn
tg@L.NGO
xeb@Z.yL
x80A@n.fK
oslo@ipr.no
post@ipr.no
historisk@vg.no
"""

    print(find_emails(text))
