*** settings ***

Library             SeleniumLibrary
Library             WebDriverManager
*** variables ***
${LOGIN_URL}         https://letcode.in/
${BROWSER}           chrome
*** test cases ***
Verify Successful Login to LETCODE
    [documentation]  This test case verifies that user is able to successfully Login to ZPFMS
    [tags]  Smoke
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window
#    Wait Until Element Is Visible  xpath://*[text()='Log in']        timeout=10
#    Click Element              xpath://*[text()='Log in']
#    Wait Until Element Is Visible  name:email        timeout=10
#    input text              name:email               demo12345@gmail.com
#    Wait Until Element Is Visible  name:password        timeout=10
#    input text              name:password               Pass@123
#    Wait Until Element Is Visible  xpath://*[text()='LOGIN']        timeout=10
#    Click Element              xpath://*[text()='LOGIN']
#     Wait Until Element Is Visible  xpath://*[text()='New Course!']       timeout=10
    Click Element               id:testing
    Close Browser

*** keywords ***



