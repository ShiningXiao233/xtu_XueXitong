from bs4 import BeautifulSoup
import re
import sys

def xuanzt(qus, ans, out):
    out.write((str(qus.span.text) + str(qus.contents[2])).strip() + "\n")
    # print(str(qus.contents[2]))
    option = qus.find_all("li")
    for a in option:
        ftg = a.find_all("em")
        # print(str(ftg[0].text) + str(ftg[1].cc.text) + "\n")
        out.write(str(ftg[0].text) + str(ftg[1].cc.text) + "\n")
    
    anst = ans.find_all("p", class_="fr")
    out.write(str(anst[0].text)[2:] + "\n\n")


def tiankong(qus, ans, out):
    out.write((str(qus.span.text) + str(qus.contents[2])).strip() + "\n")
    # print(str(qus.contents[2]))
    anst = ans.find_all("p")
    out.write("答案：" + str(anst[0].text) + "\n\n")
    pass

def panduan(qus, ans, out):
    out.write((str(qus.span.text) + str(qus.contents[2])).strip() + "\n")
    # print(str(qus.contents[2]))
    out.write("答案：" + str(ans.p.span.text) + "\n\n")
    pass

if __name__ == "__main__":
# (inhtml, outhtml) = input().split(" ")
    # print(inhtml)
    # print(outhtml)
    inhtml = sys.argv[1]
    outhtml = sys.argv[2]
    with open(inhtml, "r", encoding="utf-8") as f:
        html_text = f.read()

    print(inhtml + " in ok!")
    bs_1 = BeautifulSoup(html_text, "html5lib")
    qus = bs_1.find_all("div", class_="zm_ask")
    ans = bs_1.find_all("div", class_=re.compile('^zr_bg'))
    rmg = bs_1.find_all("ul", class_="zr_icon")
    for i in rmg:
        i.decompose()
        
    # print(qus[87].contents[2])    
    # print(ans[87].p.span.text)
        
    # print(ans[0]['class'][0])
    with open(outhtml, "w", encoding="utf-8") as out:
        for i in range(len(qus)):
            if ans[i]['class'][0] == "zr_bg1":
                tiankong(qus[i], ans[i], out)
            elif len(qus[i].find_all("li")) == 0:
                panduan(qus[i], ans[i], out)
            else:
                xuanzt(qus[i], ans[i], out)
            # xianzt(qus[i], ans[i], out)
            # out.write(str(qus[i]))
            # # out.write(str(ans[i]))
            # if ans[i]['class'][0] == "zr_bg":
            #     out.write(str(ans[i].p))
            # else:
            #     out.write(str(ans[i].div))
            # out.write("<p>----------------</p>")
            # print(str(i) + 'ok')
    print(outhtml + ' out ok!')    