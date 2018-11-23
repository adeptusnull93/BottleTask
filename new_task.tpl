<p>Add a new task to the ToDo list:</p>
<form action="/todo/new" method="GET">
<input type="text" size="40" maxlength="40" name="task">
<input type="text" size="100" maxlength="100" name="taskdescr">
</select>
<select name="taskscore">
<option>1</option>
<option>2</option>
<option>3</option>
<option>4</option>
</select>
<input type="submit" name="save" value="save">
</form>
<a href="/todo">Cancel</a>