%#template for editing a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item
<p>Edit the task with ID = {{no}}</p>
<form action="/todo/edit/{{no}}" method="get">
<input type="text" name="task" value="{{old[0]}}" size="40" maxlength="40">
<input type="text" name="taskdescr" value="{{old[1]}}" size="100" maxlength="100">
<select name="status">
<option>open</option>
<option>closed</option>
</select>
<select name="taskscore">
<option>1</option>
<option>2</option>
<option>3</option>
<option>4</option>
</select>
<br/>
<input type="submit" name="save" value="save">
</form>