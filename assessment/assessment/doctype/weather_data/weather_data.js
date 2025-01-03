// Copyright (c) 2025, Rooban Samuel and contributors
// For license information, please see license.txt

frappe.ui.form.on("Weather Data", {
    refresh: function (frm) {
        frm.add_custom_button('Fetch Weather Data', function () {
            frappe.prompt(
                [
                    {
                        label: 'City',
                        fieldname: 'city',
                        fieldtype: 'Data',
                        reqd: 1, 
                    },
                ],
                function (data) {
                    frappe.call({
                        method: 'assessment.assessment.doctype.weather_data.weather_data.fetch_weather_data',
                        args: { city_name: data.city },
                        callback: function (r) {
                            if (r.message) {
                                frappe.msgprint(r.message);
                                frm.reload_doc(); 
                            }
                        },
                    });
                },
                'Fetch Weather Data', 
                'Fetch' 
            );
        });
    },
});
