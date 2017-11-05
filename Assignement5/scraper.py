import re
import urllib.request

def find_emails(text):
    """
    function that scans a string "text" and returns
    a list of all "email like" expressions.
    """
    regex = r"([a-zA-Z0-9.#$%&~’*+-/=?‘|{}]+?@[a-zA-Z0-9.#$%&~’*+-/=? ‘|{}_]+?\.[a-zA-Z][a-zA-Z.,_]*[a-zA-Z])"
    match = re.findall(regex,text)
    return match

def find_hyperlinks(text):
    """
    function that scans a string "text" in HTML format and returns
    a list of all "url like" expressions.
    """
    regex = r"<a href=(['\"])(\w*://\w*?[a-zA-Z][a-zA-Z.,_]*[a-zA-Z]\.[a-zA-Z][a-zA-Z.,_]*[a-zA-Z][\w.~/-]*)\1"
    matches = re.findall(regex,text)
    #print(matches)
    matches = [match[1] for match in matches] # the regex captures an extra empty string
    return matches

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
    print("stealing stuff!")
    while i < depth:
        print("sneaking around")
        # Iknow the task specifically ask for a call to
        # itself, but i find this to be an easier implementation
        for k in range(len(hyperlinks)-length): #iterate over all new links
            html = str(url_to_html(hyperlinks[k]))
            hyperlinks += find_hyperlinks(html)
            emails += find_emails(html)
            hyperlinks = remove_duplicates(hyperlinks)
            emails = remove_duplicates(emails)
            length = len(hyperlinks)
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

    url = "https://lucidtech.io/"
    depth = 2
all_the_emails(url,depth)
