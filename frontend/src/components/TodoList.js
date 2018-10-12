import React from 'react'
import Todo from './Todo'

class TodoList extends React.Component {

	renderTodos() {
		return this.props.todos.map(todo => (<Todo key={todo.id} todo={todo}/>))
	}

	render() {
		return (
			<div>
				TodoList
				{this.renderTodos()}
			</div>
		)
	}
}

export default TodoList