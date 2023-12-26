# Selenium-Testing

**Test Report: Asana Application of Automation**

**Test Script: asana.py**

**Test Environment:**

Operating System: Win 11

Browser: Chrome

Selenium Version: 4.12.0

Python Version: 3.0

**Executive Summary**
The purpose of this test report is to document the execution and results of the automated test script asana.py. This script is designed to automate the login process for the Asana application and validate successful login. Additionally, it checks for the presence of the "My tasks" element on the page post-login. The test execution was carried out in the specified environment, and the results are summarized below.

**Website Test Scenario Identification: www.asana.com**

**Analyzing Asana's Key Features:**

Before identifying test scenarios for www.asana.com, it's crucial to understand the key features of the website. Asana's website serves as the landing page for users, and while it may not have the full functionality of the application, it is essential to identify its primary features. 

**Key features include:**

**Landing Page:** The website's landing page should provide information about Asana, its use cases, and navigation to relevant sections.

**User Registration and Login:** Users can register for new accounts and log in to existing ones. It is important to verify the functionality and security of the login process.

**Product Information:** The website likely provides detailed information about Asana's products, plans, and pricing.

**Case Studies and Testimonials:** Asana may showcase case studies and user testimonials to highlight its effectiveness.

**Resources and Blog:** Users may access resources such as blog articles, webinars, guides, and templates.

**Contact Information:** Contact details and support options should be readily available for users seeking assistance.

**Identifying Critical Test Scenarios:**

Now, let's identify and prioritize critical test scenarios and functionalities that need to be tested on the www.asana.com website using Selenium:

**User Registration and Login:**

                              Test Registration Process: Automate the registration process to create a new user account, ensuring it works smoothly.
                              
                              Test Login Functionality: Automate the login process with a registered account to verify successful login.
                              
                              Test Password Reset: Automate the process of resetting a forgotten password.

**Information Verification:**

                              Verify Product Information: Automate navigation to product information pages and verify the content is accurate.
                              
                              Verify Case Studies and Testimonials: Automate navigation to case studies and testimonials and ensure they are correctly displayed.

**Resource Access:**

                              Test Resource Accessibility: Automate navigation to various resource pages (blog, guides, templates) to ensure they load properly.

**Contact and Support:**

                              Contact Form Testing: Automate the process of filling and submitting a contact form to reach out to Asana's support or sales team.

**Prioritize Test Scenarios:**
                              Test scenarios should be prioritized based on their criticality, frequency of use, and alignment with business goals:

**High Priority:**

Test Login Functionality: Ensuring users can log in is critical to user experience.

Test Registration Process: Verifying users can register is vital for expanding Asana's user base.

Contact Form Testing: A functional contact form is essential for user support and inquiries.

**Medium Priority:**

Test Password Reset: Password reset is crucial for user account management.

Verify Product Information: Ensuring accurate product details is important for potential customers.

Verify Case Studies and Testimonials: To showcase Asana's value, these need to be accurate and accessible.

**Low Priority:**

Test Resource Accessibility: While important, resources can be accessed individually and are less critical for overall functionality.

**Automation Using Selenium:**

For each prioritized test scenario, Selenium can be used to create automated test scripts that simulate user interactions on the www.asana.com website.

**Test Objectives**

1.To automate the login process for the Asana application using valid credentials.

2.To verify successful login by checking if the URL changes after login.

3.To check for the presence of the "My tasks" element on the page after login.

**Test Execution**

**Test Case 1: test_successful_login**

**Description**

This test case automates the login process for the Asana application using valid user credentials and verifies a successful login.

**Test Steps**
                            
                            1.Navigate to the Asana login page (https://app.asana.com/-/login).
                            
                            2.Locate the email input field and enter a valid email address.
                            
                            3.Locate the password input field and enter a valid password.
                            
                            4.Click the login button.
                            
                            5.Capture the previous URL and the current URL.
                            
                            6.Verify that the current URL is different from the previous URL.


**Expected Outcome**
                            
                            The test case is expected to pass, indicating a successful login. The current URL should differ from the previous URL.
**Actual Outcome**

                            The test case passed as expected. The current URL is different from the previous URL, indicating a successful login.

**Test Case 2: test_my_tasks**

**Description**

This test case checks for the presence of the "My tasks" element on the page after a successful login.

**Test Steps**
                           
                            1.Wait for the page to load after successful login.
                            
                            2.Capture the page source.
                            
                            3.Search for the presence of the "My tasks" element in the page source.

**Expected Outcome**

                            The test case is expected to pass, indicating the presence of the "My tasks" element on the page after a successful login.

**Actual Outcome**

                            The test case passed as expected. The "My tasks" element was found on the page after a successful login.

**Test Failures**

No test failures were encountered during the execution of the script. Both test cases passed successfully.

**Test Environment Details**

The test script was executed in the following environment:

Operating System: Windows 11

Web Browser: Google Chrome

Selenium Version: Selenium 4.12.0

Python Version: python 3.0

**Test Execution Details**

The test script, asana.py, was executed with Selenium to automate the login process for the Asana application. The test cases were designed to simulate a user's login journey and validate the login process's success.

**Test Case 1: test_successful_login**

                                The script navigated to the Asana login page using the Chrome web browser.
                                
                                It located and filled in the email and password input fields with valid credentials.
                                
                                The login button was clicked, initiating the login process.
                                
                                The script captured the previous URL and the current URL to check for a change.
                                
                                The test case passed successfully, indicating a successful login.

**Test Case 2: test_my_tasks**

                                After successful login, the script waited for the page to load.
                                
                                It captured the page source to search for the presence of the "My tasks" element.
                                
                                The test case passed as expected, confirming the presence of the "My tasks" element on the page.

**Test Results**

Both test cases, test_successful_login and test_my_tasks, passed successfully without encountering any failures. The test script executed as expected, and the login functionality of the Asana application was validated. Furthermore, the presence of the "My tasks" element after login was verified, confirming that the post-login interface is correctly displayed.

**Test Analysis**

The automated test script asana.py successfully validated the login process of the Asana application. This script can be incorporated into a broader suite of tests to ensure the login functionality remains 
robust as the application evolves.

While the script has been demonstrated to work as expected in the current environment, it is important to conduct regular testing and updates as the application and testing environment may change over time. Additionally, it is advisable to consider further test scenarios, including negative test cases, to cover a wider range of potential issues.

**Recommendations**

Based on the successful execution of the asana.py script, the following recommendations are provided:

1.Continuous Integration (CI): Integrate the automated test script into a CI/CD pipeline to ensure that it is run automatically with each code change.

2.Test Maintenance: Regularly review and update the script to account for changes in the application, user flows, or environment.

3.Additional Test Cases: Consider adding negative test cases to cover scenarios where invalid credentials are used, and the system should handle them appropriately.

4.Parallel Testing: Explore parallel test execution to speed up test runs, especially as the test suite expands.

5.Detailed Logging: Enhance the script's logging to capture more detailed information in case of test failures.

6.Integration with Test Management Tools: Integrate the script with test management and reporting tools for more comprehensive test reporting and tracking.
