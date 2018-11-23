%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<HTML>
    <HEAD>
        <TITLE> ToDo List </TITLE>
    </HEAD>
<BODY>
<CENTER>
<p>Current open task:</p>
<table border="1">
<tr>
<th> Task Name </th>
<th> Task Description </th>
<th> Task Score </th>
<th> <a href="/todo/new">New Task</a> </th>
</tr>
%for row in rows:
  <tr>
  %taskid = (str(row[0]))
  %taskrow = (row[1],row[2],row[3])
  %for col in taskrow:
    <td>{{col}}</td>
  %end
  <td><a href="/todo/edit/{{taskid}}">Edit</a></td>
%end
<tr>
    <td>
        <a href="/todo/closedtask">View Closed Task</a>
    </td>
    <td>
        <a href="/todo/download/task.xls">Export to Excel</a>
    </td>
</tr>
</table>
</CENTER>
<table>
    <tr>

    </tr>
    <tr>
    </tr>
    <tr>
    </tr>
</table>
</BODY>
</HTML>
