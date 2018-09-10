# -*- coding: utf-8 -*-
# MySQL Workbench Python script
# <description>
# Written in MySQL Workbench 6.3.10

import grt
#import mforms

import sqlide_power_import_export_be as export

editor = grt.root.wb.sqlEditors[0]
mod = export.json_module(editor, False)
# set filepaht
mod._filepath='e:\\sundewang\\a.json'
# set select query
mod._user_query = 'select * from tmdatabase.gonggao'
mod.start_export()

