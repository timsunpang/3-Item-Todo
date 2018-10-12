import React from 'react'

class Todo extends React.Component {
	constructor(props) {
		super(props)
		console.log(props)
	}

	render() {
		return (
			<div>
				<h2>{this.props.todo.title}</h2>
				<p>{this.props.todo.description}</p>
				<p>{this.props.todo.completed ? 'x' : 'o'}</p>
			</div>
		)
	}
}

export default Todo