# <p align="center"> UI tests automation project Swag Labs </p>
### <p align="center"> in <code>Python</code> using <code>Pytest</code> </p>
<p align="center">
<img title="Swag Labs Main Page" src="images/screenshots/swag_labs.png">
</p>

##  Content

> ➠ [Technology Stack](#technology-stack)
>
> ➠ [Covered Functionality](#covered-functionality)
>
> ➠ [Build in Jenkins](#running-tests-remotely-on-jenkins)
>
> ➠ [Allure Report](#overview)
> 
> ➠ [Report in TestOps](#dashboard)
> 
> ➠ [Integration with Jira](#test-caseslaunches-in-testops-are-integrated-with-tasks-in-jira)
>
> ➠ [Notifications in Telegram](#after-the-test-run-is-completed-a-special-bot-created-in-codetelegramcode-automatically-sends-a-notification-with-a-report-on-the-run)

  
## Technology Stack

<p align="center">
<a href="https://www.jetbrains.com/pycharm/"><img src="images/logo/pycharm.svg" width="50" height="50"  alt="PyCharm"/></a>
<a href="https://www.python.com/"><img src="images/logo/python.svg" width="50" height="50"  alt="Python"/></a>
<a href="https://github.com/"><img src="images/logo/github-2.svg" width="50" height="50"  alt="GitHub"/></a>
<a href="https://docs.pytest.org/"><img src="images/logo/pytest.svg" width="50" height="50"  alt="Pytest 5"/></a>
<a href="https://aerokube.com/selenoid/"><img src="images/logo/selenoid.svg" width="50" height="50"  alt="Selenoid"/></a>
<a href="https://github.com/allure-framework/allure2"><img src="images/logo/allure.svg" width="50" height="50"  alt="Allure"/></a>
<a href="https://www.jenkins.io/"><img src="images/logo/jenkins.svg" width="50" height="50"  alt="Jenkins"/></a>
<a href="https://qameta.io/"><img src="images/logo/allure_TO.svg" width="50" height="50"  alt="Allure TestOps"/></a>  
<a href="https://www.atlassian.com/ru/software/jira/"><img src="images/logo/jira.svg" width="50" height="50"  alt="Jira"/></a>  
</p>

>
> <code>Selenoid</code> runs browsers in <code>Docker</code> containers.
>
> <code>Allure Report/Allure TestOps</code> generates reports on the test run results.
>
> <code>Jenkins</code> is used to execute tests remotely.
> 
> After run is completed, notifications are sent using the bot in <code>Telegram</code>.

## Covered Functionality
#### UI tests were designed to check the following scenarios

- [x] Successful login testing
- [x] Unsuccessful login testing
- [x] Product can be added to cart
- [x] Product can be removed from cart
- [x] User can proceed to checkout from the cart
- [x] User can proceed shopping from the cart
- [x] User can open the product description from the inventory page
- [x] Items number in the cart is displayed on the cart icon

## <img src="images/logo/jenkins.svg" width="25" height="25"  alt="Jenkins"/></a> <a target="_blank" href="https://jenkins.autotests.cloud/job/C11-voronirina-diploma-UI/"> Jenkins </a>
#### Running tests remotely on Jenkins

```
python -m venv .venv
source .venv/bin/activate
pip install poetry 
poetry install
pytest "${TEST}"
```
<p align="center">
<img title="Jenkins" src="images/screenshots/jenkins.png">
</p>

## <img src="images/logo/allure.svg" width="25" height="25"  alt="Allure"/></a> <a target="_blank" href="https://jenkins.autotests.cloud/job/C11-voronirina-diploma-UI/46/allure/">Allure Report</a>

####  Overview
<p align="center">
<img title="Allure Dashboard" src="images/screenshots/allure_report_overview.png">
</p>


#### Tests 
<p align="center">
<img title="Allure Tests" src="images/screenshots/allure_report_tests.png">
</p>

## <img src="images/logo/allure_TO.svg" width="25" height="25"  alt="Allure"/></a> <a target="_blank" href="https://allure.autotests.cloud/launch/38541/">TestOps</a>
####  Dashboard
<p align="center">
<img title="Allure Overview Dashboard" src="images/screenshots/TO_dashboards.png">
</p>

####  Test Cases
<p align="center">
<img title="Allure Test Suites" src="images/screenshots/TO_suites.png">
</p>

## <img src="images/logo/jira.svg" width="25" height="25"  alt="Allure"/></a> Integration with <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1206">Jira</a>
#### Test cases/launches in TestOps are integrated with tasks in Jira
<p align="center">
<img title="Jira" src="images/screenshots/jira.png">
</p>

## <img src="images/logo/telegram.svg" width="25" height="25"  alt="Allure"/></a> Notifications in Telegram
#### After the test run is completed, a special bot created in <code>Telegram</code> automatically sends a notification with a report on the run.

<p align="center">
<img title="Telegram Notification" src="images/screenshots/telegram.png" >
</p>

