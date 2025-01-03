import frappe

@frappe.whitelist()
def bulk_convert_to_customer(lead_ids):

    lead_ids = frappe.parse_json(lead_ids)
    converted_count = 0

    for lead_id in lead_ids:
        # Fetch the lead document
        lead = frappe.get_doc("Lead", lead_id)

        # Validate if the customer already exists and the lead is converted
        if lead.status == "Converted" or frappe.db.exists("Customer", {"customer_name": lead.lead_name}):
            return {
                "status": "error",
                "message": (
                    f"A customer with the name '{lead.lead_name}' already exists or "
                    f"Lead {lead_id} is already converted to a customer."
                ),
            }

        # Create a new customer from the lead details
        customer = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": lead.lead_name,
            "customer_group": "All Customer Groups",
            "territory": "All Territories"
        })
        customer.insert(ignore_permissions=True)

        lead.status = "Converted"
        lead.save(ignore_permissions=True)
        converted_count += 1

    frappe.db.commit()
    return {"status": "success", "message": f"Converted {converted_count} leads to customers"}


def validate(self, events):
        if self.mobile_no:
            if not self.mobile_no.startswith('+91'):
                frappe.throw("Mobile number must start with the country code +91.")

            if len(self.mobile_no) > 15:
                frappe.throw("Mobile number (including +91) cannot exceed 15 characters.")
