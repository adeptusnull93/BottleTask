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
<th> <a href="new">New Task</a> </th>
</tr>
%for row in rows:
  <tr>
  %taskid = row[0]
  %taskrow = (row[1],row[2])
  %for col in taskrow:
    <td>{{col}}</td>
  %end
  <td><a href="edit/{{taskid}}">Edit</a></td>
%end
<tr><td><a href="/todo">View Open Task</td></tr>
</table>
</CENTER>
<table border="1">
    <tr>

    </tr>
    <tr>
    </tr>
    <tr>
    </tr>
</table>
</BODY>
</HTML>
