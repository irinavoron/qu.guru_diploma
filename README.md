# <p align="center"> UI tests automation project www.saucedemo.com in <code>Python</code> using <code>Pytest</code> </p>
<p align="center">
<img title="Allure Overview Dashboard" src="images/screens/jw.PNG">
</p>

##  Content

> ➠ [Technology Stack](#classical_building-технологический-стек)
>
> ➠ [Covered Functionality](#earth_africa-покрытый-функционал)
>
> ➠ [Сборка в Jenkins](#earth_africa-Jenkins-job)
>
> ➠ [Запуск из терминала](#earth_africa-Запуск-тестов-из-терминала)
>
> ➠ [Примеры использования](#earth_africa-Allure-отчет)
>
> ➠ [Allure отчет](#earth_africa-Allure-отчет)
> 
> ➠ [Интеграция с Jira](#earth_africa-Allure-отчет)
>
> ➠ [Отчет в Telegram](#earth_africa-Уведомление-в-Telegram-при-помощи-бота)
>
> ➠ [Видео примеры прохождения тестов](#earth_africa-Примеры-видео-о-прохождении-тестов)

  
## Technology Stack

<p align="center">
<a href="https://www.jetbrains.com/pycharm/"><img src="images/logo/pycharm.svg" width="50" height="50"  alt="PyCharm"/></a>
<a href="https://www.python.com/"><img src="images/logo/python.svg" width="50" height="50"  alt="Python"/></a>
<a href="https://github.com/"><img src="images/logo/github.svg" width="50" height="50"  alt="GitHub"/></a>
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
### UI tests were designed to check the following scenarios

- [x] Successful login testing
- [x] Unsuccessful login testing
- [x] Product can be added to cart
- [x] Product can be removed from cart
- [x] User can proceed to checkout from the cart
- [x] User can proceed shopping from the cart
- [x] User can open the product description from the inventory page
- [x] Items number in the cart is displayed on the cart icon

## <img src="images/logo/jenkins.svg" width="25" height="25"  alt="Jenkins"/></a> Jenkins <a target="_blank" href="https://jenkins.autotests.cloud/job/C11-voronirina-diploma-UI/"> project link </a>
<p align="center">
<a href="https://jenkins.autotests.cloud/job/C11-voronirina-diploma-UI/"><img src="images/screenshots/jenkins.PNG" alt="Jenkins"/></a>
</p>

### Удаленный запуск тестов на Jenkins

```
clean
test
-Duser=${USER}
-Dpassword=${PASSWORD}
-DremoteBrowser=${REMOTE_DRIVER_URL}
-Dbrowser=${BROWSER}
-Dsize=${BROUSERSIZE}
-Dversion=${VERSION}
```
##  Запуск тестов из терминала
Локальный запуск:
```
gradle clean test
```

# Примеры использования

### Для запуска удаленных тестов необходимо заполнить remote.properties или передать значение:

* browser (default chrome)
* browserVersion (default 89.0)
* browserSize (default 1920x1080)
* browserMobileView (mobile device name, for example iPhone X)
* remoteDriverUrl (url address from selenoid or grid)
* videoStorage (url address where you should get video)
* threads (number of threads)


Запускайте тесты с заполненным remote.properties:
```bash
gradle clean test
```

Запускайте тесты с незаполненным remote.properties:
```bash
gradle clean -DremoteDriverUrl=https://%s:%s@selenoid.autotests.cloud/wd/hub/ -DvideoStorage=https://selenoid.autotests.cloud/video/ -Dthreads=1 test
```

Сгенерировать отчет:
```bash
allure serve build/allure-results
```
## <img src="images/logo/Allure.svg" width="25" height="25"  alt="Allure"/></a> Отчет в <a target="_blank" href="https://jenkins.autotests.cloud/job/Johnnie_Walker_UI_tests/7/allure/">Allure report</a>

###  Основной отчет
<p align="center">
<img title="Allure Overview Dashboard" src="images/screens/Alrep.PNG">
</p>


### Тесты 
<p align="center">
<img title="Allure Tests" src="images/screens/Altests.PNG">
</p>

## <img src="images/logo/Allure_TO.svg" width="25" height="25"  alt="Allure"/></a> Отчет в <a target="_blank" href="https://allure.autotests.cloud/launch/15301">Allure TestOps</a>
<p align="center">
<img title="Allure Overview Dashboard" src="images/screens/AllureTestOps.PNG">
</p>
<p align="center">
<img title="Allure Overview Dashboard" src="images/screens/AllureTestOps2.PNG">
</p>

## <img src="images/logo/Jira.svg" width="25" height="25"  alt="Allure"/></a> Интеграция с <a target="_blank" href="https://jira.autotests.cloud/browse/AUTO-1303">Jira</a>
<p align="center">
<img title="Allure Overview Dashboard" src="images/screens/JiraTicket.PNG">
</p>

## <img src="images/logo/Telegram.svg" width="25" height="25"  alt="Allure"/></a> Уведомление в Telegram при помощи бота
> После завершения сборки специальный бот, созданный в <code>Telegram</code>, автоматически обрабатывает и отправляет сообщение с отчетом о прогоне.

<p align="center">
<img title="Allure Overview Dashboard" src="images/screens/bot.PNG" >
</p>

## Примеры запуска тестов в Selenoid
### <img src="images/logo/Selenoid.svg" width="25" height="25" alt="Jenkins"/></a> Видео <a target="_blank" href="https://selenoid.autotests.cloud/video/ef6f0961cd61bebe69b39d6591b8a072.mp4">прохождения тестов </a>
<p align="center">
<img title="Local launch example" src="images/gif/video.gif">
</p>

