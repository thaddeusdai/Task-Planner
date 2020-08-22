function format_inputs(){
    // makes all the task appear in all caps in the todo list
    var input_task = document.getElementById('task').value;
    var new_task = input_task.toUpperCase()
    document.getElementById('task').value = new_task
    // capitalizes the first letter in the description
    var input_text = document.getElementById('description').value;
    var new_text = input_text[0].toUpperCase() + input_text.slice(1);
    document.getElementById('description').value = new_text
    
}

