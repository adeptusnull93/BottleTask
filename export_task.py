import sqlite3
import xlwt
from xlwt import Borders, Pattern, Alignment
from datetime import datetime


def get_width(num_characters):
    colsize = len(num_characters)
    return int((1+colsize) * 256)

def export_excel():
    """
        Generate Excel from from task table

    """
    dbdir = str('todo.db')

    conn = sqlite3.connect(dbdir)
    c = conn.cursor()
    c.execute("SELECT task, taskdescr,score FROM todo WHERE status LIKE '1' order by score asc")
    result = c.fetchall()
    c.close()

    font0 = xlwt.Font()
    font0.name = 'Arial Black'
    font0.colour_index = 0
    font0.bold = True
    alignment = Alignment()
    borders = Borders()
    bordersthin = Borders()
    pattern = Pattern()

    alignment.HORZ_JUSTIFIED
    alignment.VERT_JUSTIFIED
    pattern.pattern = Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 0x2C
    pattern.pattern_back_colour = 0x00
    borders.left = Borders.THICK
    borders.right = Borders.THICK
    borders.top = Borders.THICK
    borders.bottom = Borders.THIN
    bordersthin.left = Borders.THIN
    bordersthin.right = Borders.THIN
    bordersthin.top = Borders.THIN
    bordersthin.bottom = Borders.THIN

    datestyle = xlwt.XFStyle()
    datestyle.num_format_str = 'D-MMM-YY'
    style0 = xlwt.XFStyle()
    style0.font = font0
    style0.borders = borders
    style0.pattern = pattern
    style0.alignment = alignment
    style1 = xlwt.XFStyle()
    style1.borders = bordersthin
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Task List')
    x = 0
    y = 1
    #
    ws.write(0,0, 'TaskName ', style0)
    ws.write(0,1, 'TaskDescription ', style0)
    ws.write(0,2, 'TaskScore ', style0)
    ws.write(0, 4,'  Generated ' + str(datetime.now()), datestyle)
    for rows in result:
        for col in rows:
            countwidth = get_width(str(col))
            ws.write(y,x, col, style1)
            currentwidth = ws.col(x).width
            if countwidth > currentwidth:
                ws.col(x).width = int(30+countwidth)
            x = x + 1
            # Add 1 to Y to jump to new row. Set x to 0 to start on first column
        y = y + 1
        x = 0
    wb.save('./download/task.xls')

export_excel()
