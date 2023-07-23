# Copyright (c) 2023, zubair and contributors
# For license information, please see license.txt

import json
import subprocess
import os
import shlex
import sys
from subprocess import PIPE, Popen, check_output
from datetime import datetime,timedelta
import traceback
import frappe
import frappe
import shlex
import re
from subprocess import PIPE, STDOUT, Popen
from digitalocean.digitalocean.utils import _close_the_doc
from digitalocean.digitalocean.utils import safe_decode
from urllib.parse import parse_qs, urlparse

import frappe
from digitalocean.digitalocean.utils import (
	safe_decode,
	verify_whitelisted_call,
)
from frappe.model.document import Document
import json
import os
import dropbox
from rq.timeouts import JobTimeoutException

import frappe
from frappe import _
from frappe.integrations.offsite_backup_utils import (
	get_chunk_site,
	send_email,
	validate_file_size,
)
from frappe.integrations.utils import make_post_request
from frappe.model.document import Document
from frappe.utils import (
	cint,
	encode,
	get_url,
	get_request_site_address,
)
from frappe.utils.background_jobs import enqueue

ignore_list = [".DS_Store"]

class BenchManage(Document):
	pass


@frappe.whitelist()
def checkme(key, caller, alias=None, app_name=None, admin_password=None, mysql_password=None):
	s_name = "erp.upeosoft.com"
	doctype = "TestDi"
	docname = "8f2141b191"
	cname = "cd && ../client-bench;bench get-app hrms"
	commands = {
		"migrate": ["{cname}".format(cname=cname)],
	}
	frappe.enqueue(
		"digitalocean.digitalocean.utils.run_command",
		commands=commands[caller],
		doctype=doctype,
		key=key,
		docname=docname,
	)
	return "executed"
@frappe.whitelist()
def ops():
	d = frappe.get_doc("Bench Manage")
	path = d.path
	ccc = "cd && ../client-bench;bench start"
	cmd = "cd .. && cd {path};bench start".format(path=path)
	subprocess.run(cmd, shell=True)
	# os.system(cmd)
	return cmd

# @frappe.whitelist()
# def run_cmd(commands):
# 	try:
# 		result = subprocess.check_output(commands, shell=True, text=True)
# 		return result
# 	except subprocess.CalledProcessError as e:
# 		return f"Error: {e}"
# @frappe.whitelist()
# def run_cmd(commands):
#     try:
#         result = subprocess.run(commands, shell=True, capture_output=True, text=True)
#         if result.returncode == 0:
#             return result.stdout.strip()
#         else:
#             return f"Error: {result.stderr.strip()}"

#     except Exception as e:
#         return f"Error: {str(e)}"
# @frappe.whitelist()
# def run_cmd(commands, path):
#     try:
#         result = subprocess.run(commands, shell=True, capture_output=True, text=True, cwd=path)
#         if result.returncode == 0:
#             return result.stdout.strip()
#         else:
#             return f"Error: {result.stderr.strip()}"

#     except Exception as e:
#         return f"Error: {str(e)}"

