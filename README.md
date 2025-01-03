## Assessment

Task 1: Bulk Conversion in Lead Doctype
Objective:
Add a submenu option in the Actions section of the Lead doctype list view to facilitate bulk conversion.
Details:
In the Lead doctype, when multiple lead records are selected from the list view, a new option will appear in the Actions submenu titled "Bulk Convert to Customer".
Upon selecting this option, the chosen leads will be converted to Customer records in the Customer doctype.
The Lead status will be automatically updated to Converted.


Task 2: Event Reminder Notifications
Objective:
Implement automatic reminder notifications for events based on the event's start date.
Details:
In the Events doctype, a reminder functionality will be added.
If the Start Date of the event is set, system notifications and real-time notifications will be triggered as follows:
1 hour before the event.
1 day before the event.
1 week before the event.
Notifications will appear in the Notification Bell Icon.


Task 3: Additional Features for Experienced Developers
A. Custom Sales Report Generation
Objective:
Create a custom report for sales data based on specified filters.
Details:
The report will be named Sales Report.
Filters for Start Date, End Date, and Territory will be provided.
The data displayed can be downloaded in PDF, Excel, or CSV formats.
Download as PDF: Click the three-dot icon in the top-right corner and select the PDF option.
Download as Excel/CSV: Click the Export option and select Excel or CSV format.


B. Weather Data Integration
Objective:
Create an integration to fetch and display weather data for a given city.
Details:
A new doctype, Weather Data, will be created.
A Fetch Weather Data button will be added to the doctype.
Upon clicking the button, the user will enter a City Name, and the corresponding weather details will be populated in the respective fields of the doctype.


C. Custom Field Validation in Lead Doctype
Objective:
Add a validation rule to the Mobile No field in the Lead doctype.
Details:
The Mobile No field will be validated to ensure:
It starts with a country code.
It does not exceed 15 characters.