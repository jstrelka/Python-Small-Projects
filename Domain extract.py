# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

# The Domain extract function will strip only the domain of a url.

def domain_name(url):
    comindex = 0
    url = url.replace("https://", "")
    url = url.replace("http://", "")
    url = url.replace("www.", "")
    comindex = url.find(".")
    url = url[:comindex]
    return url

def main():
    domain_name("http://github.com/carbonfive/raygun")
    domain_name("http://www.zombie-bites.com")
    domain_name("https://www.cnet.com")

main()