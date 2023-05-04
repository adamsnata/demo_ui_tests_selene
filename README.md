## Demo project of UI autotests for staya.dog

<!-- Technologies -->

### Used technologies
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo_stacks/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo_stacks/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo_stacks/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo_stacks/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo_stacks/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo_stacks/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo_stacks/jenkins.png"></code>
  <code><img width="5%" title="Docker" src="images/logo_stacks/docker.png"></code>
  <code><img width="5%" title="Selenoid" src="images/logo_stacks/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo_stacks/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo_stacks/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo_stacks/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo_stacks/tg.png"></code>
</p>


<!-- Test cases -->

### Assertions
* Authorization - Log in
* Authorization - Log out
* Cart - Add product to cart
* Cart - Clear cart
* Filters - Show products by collections
* Filters - Show products by new
* Filters - Show products that participate in charity


<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/logo_stacks/jenkins.png"> Running the project in Jenkins.

### [Job](https://jenkins.autotests.cloud/job/privalov_staya_ui/)

##### Clicking "Build Now" will start building the tests and running them through a virtual machine in Selenoid.
![This is an image](images/screenshots/jenkins.png)


<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/logo_stacks/allure_report.png"> Allure report

##### After running the tests, the results can be viewed in the Allure report, which also contains a link to Jenkins.
![This is an image](images/screenshots/allure_dashboard.png)

##### In the Graphs tab, you can view graphs about test runs, prioritization, time to completion, etc.
![This is an image](images/screenshots/allure_graphs.png)

##### In the Suites tab, you can find collected test cases, which include steps, logs, screenshots, and videos of test runs.
![This is an image](images/screenshots/allure_suites.png)

##### Video of test run
![This is an image](images/screenshots/tests_ui.gif)


<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/logo_stacks/allure_testops.png"> Integration with Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/2113/dashboards)

##### All reporting is also saved in Allure TestOps, where similar graphs are constructed.
![This is an image](images/screenshots/allure_testops_dashboard.png)

#### In the Suites tab, we can:
* Manage all test cases or each one separately
* Restart each test case separately from all tests
* Configure integration with Jira
* Add manual tests, etc.

![This is an image](images/screenshots/allure_testops_suites.png)


<!-- Jira -->

### <img width="3%" title="Jira" src="images/logo_stacks/jira.png"> Jira Integration
##### By setting up integration with Jira through Allure TestOps, you can pass test run results and a list of test cases from Allure to a ticket.

![This is an image](images/screenshots/jira.png)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/logo_stacks/tg.png"> Telegram Integration
##### After running the tests, a message with a graph and some information about the tests is sent to a Telegram bot.

![This is an image](images/screenshots/tg_bot.png)
