from selenium import webdriver
import getpass
import time

#codechef credentials for login
username="bhawnagupta"
password=getpass.getpass("Password: ")

#problem code
problem='TEST'

#submission code
code="""
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        if(n==42)
            break;
        cout<<n<<endl;
    }
}
"""

#start a browser session
browser=webdriver.Chrome()

#open link in browser
browser.get("https://codechef.com")

#login
nameElem=browser.find_element_by_id("edit-name")
nameElem.send_keys(username)

passElem=browser.find_element_by_id("edit-pass")
passElem.send_keys(password)

browser.find_element_by_id("edit-submit").click()

#open submission page
browser.get("https://www.codechef.com/submit/TEST")

#sleep function to let web components load in case of slow internet connection
time.sleep(15)

#click on toggle button to open simple text mode
browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()

#submit the code
inputElem=browser.find_element_by_id("edit-program")
browser.find_element_by_xpath('//*[@id="edit-language"]/option[10]').click()
inputElem.send_keys(code)
#sleep function to let web components load in case of slow internet connection
time.sleep(15)

browser.find_element_by_id("edit-submit-1").click()





