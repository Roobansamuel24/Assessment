import frappe
from frappe.utils import now_datetime, add_to_date, get_datetime

def send_event_reminders():

    current_time = now_datetime()
    current_date = current_time.date()
    current_hour = current_time.hour 
    current_minute = current_time.minute

    intervals = {
        "1_hour": add_to_date(current_time, hours=1),
        "1_day": add_to_date(current_time, days=1),
        "1_week": add_to_date(current_time, weeks=1),
    }

    for interval_name, reminder_time in intervals.items():
        events = frappe.get_all(
            "Event",
            filters={
                "custom_enable_reminder": 1,
                "starts_on": [">", reminder_time],
            },
            fields=["name", "starts_on", "subject", "owner"],
        )

        for event in events:
            event_start_time = get_datetime(event["starts_on"])

            if interval_name == "1_hour":
                reminder_time = add_to_date(event_start_time, hours=-1) 
            elif interval_name == "1_day":
                reminder_time = add_to_date(event_start_time, days=-1)
            elif interval_name == "1_week":
                reminder_time = add_to_date(event_start_time, weeks=-1) 

            if (
                reminder_time.date() == current_date and
                reminder_time.hour == current_hour and  
                reminder_time.minute == current_minute
            ):
                send_reminder_notification(event, interval_name)


def send_reminder_notification(event, interval_name):

    message = (
        f"Reminder: Your event '{event['subject']}' is scheduled to start on "
        f"{event['starts_on']} ({interval_name} reminder)."
    )

    # Create a new Notification Log
    notification_log = frappe.new_doc("Notification Log")
    notification_log.subject = f"Event Reminder - {event['subject']}"
    notification_log.for_user = event["owner"]
    notification_log.document_type = "Event"
    notification_log.document_name = event["name"]
    notification_log.type = "Alert"
    notification_log.email_content = message
    notification_log.from_user = event["owner"] 
    notification_log.save(ignore_permissions=True)

    # Optionally, you can still publish a real-time notification
    frappe.publish_realtime(
        event="msgprint",
        message=message,
        user=event["owner"],
    )
