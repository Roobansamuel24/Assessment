# Copyright (c) 2025, Rooban Samuel and contributors
# For license information, please see license.txt
import frappe
from frappe import _

def columns():
  
    return [
        {
            "label": _("Sales Invoice"),
            "fieldname": "Sales Invoice",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("Posting Date"),
            "fieldname": "Posting Date",
            "fieldtype": "Date",
            "width": 150
        },
        {
            "label": _("Grand Total"),
            "fieldname": "Grand Total",
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "label": _("Territory"),
            "fieldname": "Territory",
            "fieldtype": "Link",
            "options": "Territory",
            "width": 150,
			"align" : "left"
        },
        {
            "label": _("Customer Name"),
            "fieldname": "Customer Name",
            "fieldtype": "Data",
            "width": 200
        }
    ]

def execute(filters=None):

    from_date = filters.get('from_date')
    to_date = filters.get('to_date')
    
    if from_date > to_date:
        frappe.throw(_("From Date should not be greater than To Date."))

    query = """
        SELECT si.name AS 'Sales Invoice',
               si.posting_date AS 'Posting Date',
               si.grand_total AS 'Grand Total',
               c.territory AS 'Territory',
               c.customer_name AS 'Customer Name'
        FROM `tabSales Invoice` si
        LEFT JOIN `tabCustomer` c ON si.customer = c.name
        WHERE si.posting_date BETWEEN %s AND %s AND c.territory = %s
    """
    
    data = frappe.db.sql(query, (from_date, to_date, filters.get('territory')), as_dict=True)

    return columns(), data