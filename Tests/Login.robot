*** settings ***
Library             SeleniumLibrary
Library             WebDriverManager

*** variables ***
${LOGIN_URL}         http://192.168.0.162:9696/Login.aspx
${BROWSER}           chrome

*** test cases ***
Verify Successful Login to ZPFMS
    [documentation]  This test case verifies that user is able to successfully Login to ZPFMS
    [tags]  Smoke
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window
     Wait Until Element Is Visible  id:txtUser        timeout=10
    input text              id:txtUser                Dbchavan
    Wait Until Element Is Visible  id:txtPass        timeout=10
    input text              id:txtPass              Pass@123
    Wait Until Element Is Visible  xpath://*[@id="btnLogin"]       timeout=10
    Click Element              xpath://*[@id="btnLogin"]
    Click Element              xpath://*[@id='ctl01']/div[contains(@class, 'page-header')]/div[contains(@class, 'page-header-menu')]/div/div/ul/li[3]/a
    Click Element              xpath://*[@id="ctl01"]/div[5]/div[3]/div/div/ul/li[3]/ul/li[1]/a
    Close Browser

*** keywords ***



