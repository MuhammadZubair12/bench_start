// Copyright (c) 2023, zubair and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bench Manage', {
	// refresh: function(frm) {

	// },
	click: function(frm) {	
		frappe.call({
			method: "bench_start.bench_start.doctype.bench_manage.bench_manage.ops",
		
			// args: {
			// 	"path": frm.doc.path
			// },
			callback:function(r){
				console.log("Result",r)
			}
		})
		
	}
});
