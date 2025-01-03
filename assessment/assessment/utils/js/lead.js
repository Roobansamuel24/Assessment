frappe.listview_settings['Lead'] = {
    onload: function (listview) {
        listview.page.add_actions_menu_item('Bulk Convert to Customer', async function () {
            const selected = listview.get_checked_items();
        
            frappe.confirm(
                `Are you sure you want to convert ${selected.length} Lead(s) to Customer(s)?`,
                async () => {
                    const lead_ids = selected.map(row => row.name);
                    try {
                        const response = await frappe.call({
                            method: 'assessment.assessment.utils.py.lead.bulk_convert_to_customer',
                            args: { lead_ids }
                        });
                        frappe.msgprint(response.message);
                        listview.refresh();
                    } catch (err) {
                        frappe.msgprint(__('An error occurred during conversion.'));
                    }
                }
            );
        });
    },
    
};
