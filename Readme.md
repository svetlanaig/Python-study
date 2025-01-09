This is test scope for API and UI testing.

For it need to be installed: playwrite, pytest, response, json schema

API testing scope:

API testing provided for site petstore.swagger.io.
In contains 9 tests in it. Some of them have included parameters changed during execution.
They should be run one by one locally (to recieve correct respons on Delete requests) or via html reports.


UI tests scope:

UI testing for site demoqa.com/text-box.
It contains 5 tests in it. Some of them have included parameters changed during execution.
Some of them open the browser, some - not.
One of cases was intentionally(!) made to be failed (case Test3. This test case click radiobutton 'No' and check it if checked after it)

To run cases: 

1 - download locally and run in IDE all file.
2 - run from the folder pytest --html=reports/report.html
 
